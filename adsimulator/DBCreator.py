# Requirements - pip install neo4j-driver
# This script is used to create randomized sample databases.
# Commands
# 	dbconfig - Set the credentials and URL for the database you're connecting too
#	connect - Connects to the database using supplied credentials
# 	setparams - Set the settings JSON file
# 	setdomain - Set the domain name
# 	cleardb - Clears the database and sets the schema properly
#	generate - Connects to the database, clears the DB, sets the schema, and generates random data

from neo4j import GraphDatabase
import cmd
import math
from collections import defaultdict
import uuid
import time
import random
import os
from adsimulator.generators.groups import generate_default_groups
from adsimulator.generators.domains import generate_domain, generate_trusts
from adsimulator.generators.gpos import generate_default_gpos, link_default_gpos, generate_gpos, link_gpos_to_ous,\
    gplink_domain_to_ous
from adsimulator.generators.ous import generate_domain_controllers_ou, generate_computer_ous, generate_user_ous, link_ous_to_domain
from adsimulator.generators.acls import generate_enterprise_admins_acls, generate_administrators_acls, generate_domain_admins_acls,\
    generate_default_groups_acls, generate_local_admin_rights, generate_default_dc_groups_acls, generate_default_users_acls,\
    generate_all_extended_rights, generate_generic_write, generate_owns,\
    generate_write_dacl, generate_write_owner, generate_generic_all, generate_outbound_acls
from adsimulator.generators.computers import generate_computers, generate_dcs, generate_default_admin_to,\
    generate_can_rdp_relationships_on_it_users, generate_dcom_relationships_on_it_users,\
    generate_can_rdp_relationships_on_it_groups, generate_dcom_relationships_on_it_groups,\
    generate_allowed_to_delegate_relationships_on_it_users, generate_sessions,\
    generate_allowed_to_delegate_relationships_on_computers, assign_unconstrained_delegation,\
    generate_can_ps_remote_relationships_on_it_users, generate_can_ps_remote_relationships_on_it_groups
from adsimulator.generators.users import generate_guest_user, generate_default_account, generate_administrator, generate_krbtgt_user,\
    generate_users, link_default_users_to_domain, assign_kerberoastable_users
from adsimulator.generators.groups import generate_groups, generate_domain_administrators, generate_default_member_of, nest_groups,\
    assign_users_to_group
from adsimulator.utils.data import get_names_pool, get_surnames_pool, get_parameters_from_json, get_domains_pool
from adsimulator.utils.domains import get_domain_dn
from adsimulator.utils.parameters import print_all_parameters, get_int_param_value, get_int_param_value_with_upper_limit,\
    get_perc_param_value
from adsimulator.templates.default_values import DEFAULT_VALUES
from adsimulator.utils.updates import install_updates
from adsimulator.utils.about import print_software_information


class Messages():
    def title(self):
        print("==================================================================")
        print(
        """

      ,.,
      MMMM_    ,..,
        \"_ \"__"MMMMM          ,...,,
 ,..., __.\" --\"    ,.,     _-\"MMMMMMM
MMMMMM"___ "_._   MMM"_."" _ """"""         _     _                 _       _               
 \"\"\"\"\"    \"\" , \_.   \"_. .\"  __ _  __| |___(_)_ __ ___  _   _| | __ _| |_ ___  _ __    
        ,., _"__ \__./ ."   / _` |/ _` / __| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|   
       MMMMM_"  "_    ./   | (_| | (_| \__ \ | | | | | | |_| | | (_| | || (_) | | 
        ''''      (    )    \__,_|\__,_|___/_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|  
 ._______________.-'____\"---._.
  \                          /
   \________________________/
   (_)                    (_)

                                                         
                                                          
        """
        )
        print(" A realistic simulator of Active Directory domains\n")
        print("==================================================================")


    def input_default(self, prompt, default):
        return input("%s [%s] " % (prompt, default)) or default


    def input_yesno(self, prompt, default):
        temp = input(prompt + " " + ("Y" if default else "y") + "/" + ("n" if default else "N") + " ")
        if temp == "y" or temp == "Y":
            return True
        elif temp == "n" or temp == "N":
            return False
        return default



class MainMenu(cmd.Cmd):

    def __init__(self):
        self.m = Messages()
        self.url = "bolt://localhost:7687"
        self.username = "neo4j"
        self.password = "password"
        self.use_encryption = False
        self.driver = None
        self.connected = False
        self.old_domain = None
        self.domain = "TESTLAB.LOCAL"
        self.current_time = int(time.time())
        self.base_sid = "S-1-5-21-883232822-274137685-4173207997"
        self.first_names = get_names_pool()
        self.last_names = get_surnames_pool()
        self.domain_names = get_domains_pool()
        self.parameters_json_path = "DEFAULT"
        self.parameters = DEFAULT_VALUES
        self.json_file_name = None

        cmd.Cmd.__init__(self)


    def cmdloop(self):
        while True:
            self.m.title()
            self.do_help("")
            try:
                cmd.Cmd.cmdloop(self)
            except KeyboardInterrupt:
                if self.driver is not None:
                    self.driver.close()
                raise KeyboardInterrupt


    def help_dbconfig(self):
        print("Configure database connection parameters")


    def help_connect(self):
        print("Test connection to the database and verify credentials")

 
    def help_setdomain(self):
        print("Set domain name (default 'TESTLAB.LOCAL')")

 
    def help_cleardb(self):
        print("Clear the database and set constraints")

 
    def help_generate(self):
        print("Connect to the database, clear the db, set the schema, and generate random data")


    def help_setparams(self):
        print("Import the settings JSON file containing the parameters for the graph generation")
    

    def help_update(self):
        print("Check for available updates")


    def help_about(self):
        print("View information about adsimulator")

 
    def help_exit(self):
        print("Exit")
    

    def do_update(self, args):
        install_updates()
        
    

    def do_about(self, args):
        print_software_information()

 
    def do_dbconfig(self, args):
        print("Current Settings:")
        print("DB Url: {}".format(self.url))
        print("DB Username: {}".format(self.username))
        print("DB Password: {}".format(self.password))
        print("Use encryption: {}".format(self.use_encryption))
        print("")
        self.url = self.m.input_default("Enter DB URL", self.url)
        self.username = self.m.input_default(
            "Enter DB Username", self.username)
        self.password = self.m.input_default(
            "Enter DB Password", self.password)

        self.use_encryption = self.m.input_yesno(
            "Use encryption?", self.use_encryption)
        print("")
        print("New Settings:")
        print("DB Url: {}".format(self.url))
        print("DB Username: {}".format(self.username))
        print("DB Password: {}".format(self.password))
        print("Use encryption: {}".format(self.use_encryption))
        print("")
        print("Testing DB Connection")
        self.test_db_conn()

 
    def do_setdomain(self, args):
        passed = args
        if passed != "":
            try:
                self.domain = passed.upper()
                return
            except ValueError:
                pass

        self.domain = self.m.input_default("Domain", self.domain).upper()
        print("")
        print("New Settings:")
        print("Domain: {}".format(self.domain))


    def do_exit(self, args):
        raise KeyboardInterrupt

 
    def do_connect(self, args):
        self.test_db_conn()


    def do_cleardb(self, args):
        if not self.connected:
            print("Not connected to database. Use connect first")
            return

        print("Clearing Database")
        d = self.driver
        session = d.session()

        session.run("match (a) -[r] -> () delete a, r")
        session.run("match (a) delete a")

        session.close()

        print("DB Cleared and Schema Set")
    

    def do_setparams(self, args):
        passed = args
        if passed != "":
            try:
                json_path = passed
                self.parameters = get_parameters_from_json(json_path)
                self.parameters_json_path = json_path
                print_all_parameters(self.parameters)
                return
            except ValueError:
                pass

        json_path = self.m.input_default("Parameters JSON file", self.parameters_json_path)
        self.parameters = get_parameters_from_json(json_path)
        if self.parameters == DEFAULT_VALUES:
            self.parameters_json_path = "DEFAULT"
        else:
            self.parameters_json_path = json_path
        self.parameters = get_parameters_from_json(json_path)
        print_all_parameters(self.parameters)


    def test_db_conn(self):
        self.connected = False
        if self.driver is not None:
            self.driver.close()
        try:
            self.driver = GraphDatabase.driver(
                self.url, auth=(self.username, self.password), encrypted=self.use_encryption)
            self.connected = True
            print("Database Connection Successful!")
        except:
            self.connected = False
            print("Database Connection Failed. Check your settings.")


    def do_generate(self, args):
        passed = args
        if passed != "":
            try:
                self.json_file_name = passed
            except ValueError:
                self.json_file_name = None

        self.test_db_conn()
        self.do_cleardb("a")
        self.generate_data()
        self.old_domain = self.domain

 
    def generate_data(self):
        if not self.connected:
            print("Not connected to database. Use connect first")
            return
        
        domain_dn = get_domain_dn(self.domain)

        computers = []
        computer_properties_list = []
        dc_properties_list = []
        groups = []
        users = []
        user_properties_list = []
        gpos = []
        gpos_properties_list = []
        ou_guid_map = {}
        ou_properties_list = []
        
        session = self.driver.session()

        print("Starting data generation")

        print("Generating the", self.domain, "domain")
        functional_level = generate_domain(session, self.domain, self.base_sid, domain_dn, self.parameters)
        
        print("Generating the default domain groups")
        generate_default_groups(session, self.domain, self.base_sid, self.old_domain)   

        ddp = str(uuid.uuid4()).upper()
        ddcp = str(uuid.uuid4()).upper()
        dcou = str(uuid.uuid4()).upper()
    
        print("Generating default GPOs")
        generate_default_gpos(session, self.domain, domain_dn, ddp, ddcp)

        print("Generating Domain Controllers OU")
        generate_domain_controllers_ou(session, self.domain, domain_dn, dcou)

        print("Linking Default GPOs")
        link_default_gpos(session, self.domain, ddp, ddcp, dcou)

        print("Generating Enterprise Admins ACLs")
        generate_enterprise_admins_acls(session, self.domain)

        print("Generating Administrators ACLs")
        generate_administrators_acls(session, self.domain)

        print("Generating Domain Admins ACLs")
        generate_domain_admins_acls(session, self.domain)

        print("Generating DC groups ACLs")
        generate_default_dc_groups_acls(session, self.domain)

        num_computers = get_int_param_value("Computer", "nComputers", self.parameters)
        print("Generating", str(num_computers), "computers")
        computer_properties_list, computers, ridcount = generate_computers(session, self.domain, self.base_sid, num_computers, computers, self.current_time, self.parameters)

        num_ous = get_int_param_value_with_upper_limit("OU", "nOUs", self.parameters, 50)
        if not num_ous % 2 == 0:
            num_ous = num_ous - 1
        num_states = int(num_ous / 2)

        print("Generating", str(num_states), "Domain Controllers")
        dc_properties_list, ridcount = generate_dcs(session, self.domain, self.base_sid, domain_dn, num_states, dcou, ridcount, self.current_time, self.parameters, functional_level)
        
        print("Generating default users")
        generate_guest_user(session, self.domain, self.base_sid, self.parameters)
        generate_default_account(session, self.domain, self.base_sid, self.parameters)
        generate_administrator(session, self.domain, self.base_sid, self.parameters)
        generate_krbtgt_user(session, self.domain, self.base_sid, self.parameters)
        link_default_users_to_domain(session, self.domain, self.base_sid)

        num_users = get_int_param_value("User", "nUsers", self.parameters)
        print("Generating", str(num_users), "users")
        user_properties_list, users, ridcount = generate_users(session, self.domain, self.base_sid, num_users, self.current_time, self.first_names, self.last_names, users, ridcount, self.parameters)

        num_groups = get_int_param_value("Group", "nGroups", self.parameters)
        print("Generating groups")
        group_properties_list, groups, ridcount = generate_groups(session, self.domain, self.base_sid, domain_dn, num_groups, groups, ridcount, self.parameters)
        
        print("Adding Domain Admins to Local Admins of Computers")
        generate_default_admin_to(session, self.base_sid)

        das = generate_domain_administrators(session, self.domain, num_users, users)

        print("Adding members to default groups")
        generate_default_member_of(session, self.domain, self.base_sid, self.old_domain)

        nesting_perc = get_perc_param_value("Group", "nestingGroupProbability", self.parameters)
        print("Applying random group nesting (nesting probability:", str(nesting_perc), "%)")
        nest_groups(session, num_groups, groups, nesting_perc)

        print("Adding users to groups")
        it_users = assign_users_to_group(session, num_users, users, groups, das, self.parameters)

        print("Adding local admin rights")
        it_groups = generate_local_admin_rights(session, groups, computers)

        print("Adding ACLs for default groups")
        generate_default_groups_acls(session, self.domain, self.base_sid)
        
        print("Adding ACLs for default users")
        generate_default_users_acls(session, self.domain, self.base_sid)
        
        print("Adding AllExtendedRights")
        generate_all_extended_rights(session, self.domain, self.base_sid, user_properties_list, das)
        
        can_rdp_users_perc = get_perc_param_value("Computer", "CanRDPFromUserPercentage", self.parameters)
        count = int(math.floor(len(computers) * (can_rdp_users_perc / 100)))
        print("Adding a maximum of", str(count), "CanRDP from users")
        generate_can_rdp_relationships_on_it_users(session, computers, it_users, count)
        
        can_rdp_groups_perc = get_perc_param_value("Computer", "CanRDPFromGroupPercentage", self.parameters)
        count = int(math.floor(len(computers) * (can_rdp_groups_perc / 100)))
        print("Adding a maximum of", str(count), "CanRDP from groups")
        generate_can_rdp_relationships_on_it_groups(session, computers, it_groups, count)
        
        dcom_users_perc = get_perc_param_value("Computer", "ExecuteDCOMFromUserPercentage", self.parameters)
        count = int(math.floor(len(computers) * (dcom_users_perc / 100)))
        print("Adding a maximum of", str(count), "ExecuteDCOM from users")
        generate_dcom_relationships_on_it_users(session,computers, it_users, count)
        
        dcom_groups_perc = get_perc_param_value("Computer", "ExecuteDCOMFromGroupPercentage", self.parameters)
        count = int(math.floor(len(computers) * (dcom_groups_perc / 100)))
        print("Adding a maximum of", str(count), "ExecuteDCOM from groups")
        generate_dcom_relationships_on_it_groups(session, computers, it_groups, count)
        
        allowed_to_delegate_users_perc = get_perc_param_value("Computer", "AllowedToDelegateFromUserPercentage", self.parameters)
        count = int(math.floor(len(computers) * (allowed_to_delegate_users_perc / 100)))
        print("Adding a maximum of", str(count), "AllowedToDelegate from users")
        generate_allowed_to_delegate_relationships_on_it_users(session, computers, it_users, count)
        
        allowed_to_delegate_computers_perc = get_perc_param_value("Computer", "AllowedToDelegateFromComputerPercentage", self.parameters)
        count = int(math.floor(len(computers) * (allowed_to_delegate_computers_perc / 100)))
        print("Adding a maximum of", str(count), "AllowedToDelegate from computers")
        generate_allowed_to_delegate_relationships_on_computers(session, computers, count)
        
        ps_remote_users_perc = get_perc_param_value("Computer", "CanPSRemoteFromUserPercentage", self.parameters)
        count = int(math.floor(len(computers) * (ps_remote_users_perc / 100)))
        print("Adding a maximum of", str(count), "CanPSRemote from users")
        generate_can_ps_remote_relationships_on_it_users(session, computers, it_users, count)
        
        ps_remote_groups_perc = get_perc_param_value("Computer", "CanPSRemoteFromGroupPercentage", self.parameters)
        count = int(math.floor(len(computers) * (ps_remote_groups_perc / 100)))
        print("Adding a maximum of", str(count), "CanPSRemote from groups")
        generate_can_ps_remote_relationships_on_it_groups(session, computers, it_groups, count)

        print("Adding sessions")
        generate_sessions(session, num_users, computers, users, das)

        print("Generating", str(num_ous), "OUs")
        split_num_computers = int(math.ceil(num_computers / num_states))
        split_num_users = int(math.ceil(num_users / num_states))
        ou_properties_list, ou_guid_map = generate_computer_ous(session, self.domain, domain_dn, computers, ou_guid_map, ou_properties_list, split_num_computers, num_states)
        ou_properties_list, ou_guid_map = generate_user_ous(session, self.domain, domain_dn, users, ou_guid_map, ou_properties_list, split_num_users, num_states)
        link_ous_to_domain(session, self.domain, ou_guid_map)

        num_gpos = get_int_param_value_with_upper_limit("GPO", "nGPOs", self.parameters, 2 * num_states)
        print("Creating", str(num_gpos), "GPOs")
        gpos, gpos_properties_list = generate_gpos(session, self.domain, domain_dn, gpos, gpos_properties_list, num_gpos, self.parameters)

        print("Generating GpLink")
        ou_names = list(ou_guid_map.keys())
        link_gpos_to_ous(session, gpos, ou_names, ou_guid_map)
        gplink_domain_to_ous(session, self.domain, ou_names, ou_guid_map)

        gpos.append("DEFAULT DOMAIN POLICY@{}".format(self.domain))
        gpos.append("DEFAULT DOMAIN CONTROLLERS POLICY@{}".format(self.domain))

        print("Adding GenericWrite")
        generate_generic_write(session, computer_properties_list, user_properties_list, group_properties_list, gpos_properties_list, das, self.domain, self.base_sid)
        print("Adding Owns")
        generate_owns(session, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, self.domain, self.base_sid)
        print("Adding WriteDacl")
        generate_write_dacl(session, dcou, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, self.domain, self.base_sid)
        print("Adding WriteOwner")
        generate_write_owner(session, dcou, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, self.domain, self.base_sid)
        print("Adding GenericAll")
        generate_generic_all(session, dcou, dc_properties_list, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, self.domain, self.base_sid)

        acl_principals_perc = get_perc_param_value("ACLs", "ACLPrincipalsPercentage", self.parameters)
        num_acl_principals = int(round(len(it_groups) * (acl_principals_perc / 100)))
        generate_outbound_acls(session, num_acl_principals, it_groups, it_users, gpos, computers, self.parameters)

        session.run('MATCH (n) SET n.domain=$domain', domain=self.domain)

        self.domain_names = get_domains_pool()
        generate_trusts(session, self.domain, self.domain_names, self.parameters)

        session.run('MATCH (n:User) SET n.owned=false')

        owned_user = random.choice(users)
        print("Compromised user:", owned_user)

        session.run('MATCH (n:User {name: $owneduser}) SET n.owned=true', owneduser=owned_user)
        session.run('MATCH (n:User {name: $owneduser}) SET n:Compromised', owneduser=owned_user)

        session.run('MATCH (n:Computer) SET n.owned=false')

        if self.json_file_name is not None:
            self.write_json(session)

        session.close()

        print("Database Generation Finished!")


    def write_json(self, session):
        json_path = os.getcwd() + "/" + self.json_file_name
        query = "CALL apoc.export.json.all('" + json_path + "',{useTypes:true})"
        session.run(query)
        print("Graph exported in", json_path)