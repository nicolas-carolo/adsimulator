import random
import math
import uuid
from adsimulator.utils.principals import get_name
from adsimulator.utils.lists import split_seq
from adsimulator.utils.ous import get_ou_dn
from adsimulator.templates.ous import STATES
from adsimulator.generators.users import set_user_dn
from adsimulator.generators.computers import set_computer_dn


def generate_domain_controllers_ou(session, domain_name, domain_dn, dcou):
    ou_dn = get_ou_dn("Domain Controllers", domain_dn)
    description = "Default container for domain controllers"
    session.run(
        """
        MERGE (n:Base {name:$ou, objectid:$guid, blocksInheritance: false, highvalue: false, distinguishedname:$dn, description:$description})
        SET n:OU
        """,
        ou=get_name("DOMAIN CONTROLLERS", domain_name),
        guid=dcou,
        dn=ou_dn,
        description=description
    )


def generate_computer_ous(session, domain_name, domain_dn, computers, ou_guid_map, ou_properties_list, split_num, num_states):
    temp_comps = computers
    random.shuffle(temp_comps)
    
    split_comps = list(split_seq(temp_comps, split_num))
    props = []
    for i in range(0, num_states):
        state = STATES[i]
        try:
            ou_comps = split_comps[i]
            ouname = "{}_COMPUTERS@{}".format(state, domain_name)
            guid = str(uuid.uuid4()).upper()
            ou_guid_map[ouname] = guid
            ou_dn = get_ou_dn(ouname, domain_dn)
            for c in ou_comps:
                set_computer_dn(session, c, ou_dn)
                ou_properties = {
                    'compname': c,
                    'ouguid': guid,
                    'ouname': ouname,
                    'dn': ou_dn,
                    'description': state + " computers"
                }
                props.append(ou_properties)
                ou_properties_list.append(ou_properties)
                if len(props) > 500:
                    session.run(
                        """
                        UNWIND $props as prop
                        MERGE (n:Computer {name:prop.compname})
                        WITH n,prop MERGE (m:Base {objectid:prop.ouguid, name:prop.ouname, blocksInheritance: false, highvalue: false, distinguishedname:prop.dn, description:prop.description})
                        SET m:OU WITH n,m,prop
                        MERGE (m)-[:Contains {isacl:false}]->(n)
                        """,
                        props=props)
                    props = []
        except IndexError:
            ouname = "{}_COMPUTERS@{}".format(state, domain_name)
            guid = str(uuid.uuid4()).upper()
            ou_guid_map[ouname] = guid
            ou_dn = get_ou_dn(ouname, domain_dn)
            ou_properties = {
                'ouguid': guid,
                'ouname': ouname,
                'dn': ou_dn,
                'description': state + " computers"
            }
            ou_properties_list.append(ou_properties)
            session.run("""
                CREATE (n:Base {objectid:$sid})
                SET n:OU,n.name=$name, n.blocksInheritance=false,
                n.highvalue=false, n.distinguishedname=$distinguishedname, n.description=$description
                """,
                sid=ou_properties["ouguid"],
                name=ou_properties["ouname"],
                distinguishedname=ou_properties["dn"],
                description=ou_properties["description"]
            )

    session.run(
        """
        UNWIND $props as prop
        MERGE (n:Computer {name:prop.compname})
        WITH n,prop
        MERGE (m:Base {objectid:prop.ouguid, name:prop.ouname, blocksInheritance: false, highvalue: false, distinguishedname:prop.dn, description:prop.description})
        SET m:OU WITH n,m,prop
        MERGE (m)-[:Contains {isacl:false}]->(n)""",
        props=props
    )
    return ou_properties_list, ou_guid_map


def generate_user_ous(session, domain_name, domain_dn, users, ou_guid_map, ou_properties_list, split_num, num_states):
    temp_users = users
    random.shuffle(temp_users)
    split_users = list(split_seq(temp_users, split_num))
    props = []

    for i in range(0, num_states):
        state = STATES[i]
        try:
            ou_users = split_users[i]
            ouname = "{}_USERS@{}".format(state, domain_name)
            guid = str(uuid.uuid4()).upper()
            ou_guid_map[ouname] = guid
            ou_dn = get_ou_dn(ouname, domain_dn)
            for c in ou_users:
                set_user_dn(session, c, ou_dn)
                ou_properties = {
                    'username': c,
                    'ouguid': guid,
                    'ouname': ouname,
                    'dn': ou_dn,
                    'description': state + " users"
                }
                props.append(ou_properties)
                ou_properties_list.append(ou_properties)
                if len(props) > 500:
                    session.run(
                        """
                        UNWIND $props as prop MERGE (n:User {name:prop.username})
                        WITH n,prop MERGE (m:Base {objectid:prop.ouguid, name:prop.ouname, blocksInheritance: false, highvalue: false, distinguishedname:prop.dn, description:prop.description})
                        SET m:OU WITH n,m,prop
                        MERGE (m)-[:Contains {isacl:false}]->(n)
                        """,
                        props=props
                    )
                    props = []
        except IndexError:
            ouname = "{}_USERS@{}".format(state, domain_name)
            guid = str(uuid.uuid4()).upper()
            ou_guid_map[ouname] = guid
            ou_dn = get_ou_dn(ouname, domain_dn)
            ou_properties = {
                'ouguid': guid,
                'ouname': ouname,
                'dn': ou_dn,
                'description': state + " computers"
            }
            ou_properties_list.append(ou_properties)
            session.run("""
                CREATE (n:Base {objectid:$sid})
                SET n:OU,n.name=$name, n.blocksInheritance=false,
                n.highvalue=false, n.distinguishedname=$distinguishedname, n.description=$description
                """,
                sid=ou_properties["ouguid"],
                name=ou_properties["ouname"],
                distinguishedname=ou_properties["dn"],
                description=ou_properties["description"]
            )

    session.run(
        """
        UNWIND $props as prop
        MERGE (n:User {name:prop.username})
        WITH n,prop
        MERGE (m:Base {objectid:prop.ouguid, name:prop.ouname, blocksInheritance: false, highvalue: false, distinguishedname:prop.dn, description:prop.description})
        SET m:OU
        WITH n,m,prop
        MERGE (m)-[:Contains {isacl:false}]->(n)""",
        props=props
    )
    return ou_properties_list, ou_guid_map


def link_ous_to_domain(session, domain_name, ou_guid_map):
    props = []
    for x in list(ou_guid_map.keys()):
        guid = ou_guid_map[x]
        props.append({'b': guid})

    session.run(
        """
        UNWIND $props as prop
        MERGE (n:OU {objectid:prop.b})
        WITH n
        MERGE (m:Domain {name:$domain})
        WITH n,m MERGE (m)-[:Contains {isacl:false}]->(n)""",
        props=props,
        domain=domain_name
    )
