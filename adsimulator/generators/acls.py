import random
import math
from adsimulator.entities.acls import get_default_group_aces_list, get_default_user_aces_list,\
    get_default_all_extended_rights, get_default_generic_write, get_default_owns, get_default_write_dacl,\
    get_default_write_owner, get_default_generic_all
from adsimulator.templates.acls import get_acls_list
from adsimulator.utils.parameters import get_dict_param_value, print_acls_parameters



def generate_enterprise_admins_acls(session, domain_name):
    # Ent Admins -> Domain Node
    group_name = "ENTERPRISE ADMINS@{}".format(domain_name)
    session.run('MERGE (n:Domain {name:$domain}) MERGE (m:Group {name:$gname}) MERGE (m)-[:GenericAll {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)


def generate_administrators_acls(session, domain_name):
    # Administrators -> Domain Node
    group_name = "ADMINISTRATORS@{}".format(domain_name)
    session.run('MERGE (n:Domain {name:$domain}) MERGE (m:Group {name:$gname}) MERGE (m)-[:Owns {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:WriteOwner {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:WriteDacl {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:GetChanges {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:GetChangesAll {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)


def generate_domain_admins_acls(session, domain_name):
    # Domain Admins -> Domain Node
    group_name = "DOMAIN ADMINS@{}".format(domain_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:WriteOwner {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:WriteDacl {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)


def generate_default_dc_groups_acls(session, domain_name):
    # DC Groups -> Domain Node
    group_name = "ENTERPRISE DOMAIN CONTROLLERS@{}".format(domain_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:GetChanges {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    group_name = "ENTERPRISE READ-ONLY DOMAIN CONTROLLERS@{}".format(domain_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:GetChanges {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)
    group_name = "DOMAIN CONTROLLERS@{}".format(domain_name)
    session.run('MERGE (n:Domain {name:$domain}) WITH n MERGE (m:Group {name:$gname}) WITH n,m MERGE (m)-[:GetChangesAll {isacl:true, isinherited: false}]->(n)', domain=domain_name, gname=group_name)


def generate_local_admin_rights(session, groups, computers):
    it_groups = [x for x in groups if "IT" in x]
    random.shuffle(it_groups)

    if len(it_groups) < 4:
        max_lim = len(it_groups)
    else:
        max_lim = 4
   
    super_groups = random.sample(it_groups, max_lim)
    super_group_num = int(math.floor(len(computers) * .85))
    it_groups = [x for x in it_groups if not x in super_groups]
    total_it_groups = len(it_groups)
    dista = int(math.ceil(total_it_groups * .6))
    distb = int(math.ceil(total_it_groups * .3))
    distc = int(math.ceil(total_it_groups * .07))
    distd = int(math.ceil(total_it_groups * .03))

    distribution_list = [1] * dista + [2] * distb + [10] * distc + [50] * distd

    props = []
    for x in range(0, total_it_groups):
        g = it_groups[x]
        dist = distribution_list[x]

        to_add = random.sample(computers, dist)
        for a in to_add:
            props.append({'a': g, 'b': a})

        if len(props) > 500:
            session.run('UNWIND $props AS prop MERGE (n:Group {name:prop.a}) WITH n,prop MERGE (m:Computer {name:prop.b}) WITH n,m MERGE (n)-[:AdminTo {isacl:false, fromgpo:false}]->(m)', props=props)
            props = []

    for x in super_groups:
        for a in random.sample(computers, super_group_num):
            props.append({'a': x, 'b': a})

        if len(props) > 500:
            session.run('UNWIND $props AS prop MERGE (n:Group {name:prop.a}) WITH n,prop MERGE (m:Computer {name:prop.b}) WITH n,m MERGE (n)-[:AdminTo {isacl:false, fromgpo:false}]->(m)', props=props)
            props = []

    session.run('UNWIND $props AS prop MERGE (n:Group {name:prop.a}) WITH n,prop MERGE (m:Computer {name:prop.b}) WITH n,m MERGE (n)-[:AdminTo {isacl:false, fromgpo:false}]->(m)', props=props)
    return it_groups


def generate_default_groups_acls(session, domain_name, domain_sid):
    standard_group_aces_list = get_default_group_aces_list(domain_name, domain_sid)
    for ace in standard_group_aces_list:
        add_right_relationship(session, ace)


def generate_default_users_acls(session, domain_name, domain_sid):
    standard_user_aces_list = get_default_user_aces_list(domain_name, domain_sid)
    for ace in standard_user_aces_list:
        add_right_relationship(session, ace)


def generate_all_extended_rights(session, domain_name, domain_sid, user_properties_list, das):
    all_extended_rights_aces_list = get_default_all_extended_rights(user_properties_list, das, domain_name, domain_sid)
    for ace in all_extended_rights_aces_list:
        add_right_relationship(session, ace)


def generate_generic_write(session, computer_properties_list, user_properties_list, group_properties_list, gpos_properties_list, das, domain_name, domain_sid):
    generic_write_aces_list = get_default_generic_write(computer_properties_list, user_properties_list, group_properties_list, gpos_properties_list, das, domain_name, domain_sid)
    for ace in generic_write_aces_list:
        add_right_relationship(session, ace)


def generate_owns(session, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, domain_name, domain_sid):
    owns_aces_list = get_default_owns(computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, domain_name, domain_sid)
    for ace in owns_aces_list:
        add_right_relationship(session, ace)


def generate_write_dacl(session, dcou, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, domain_name, domain_sid):
    write_dacl_aces_list = get_default_write_dacl(dcou, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, domain_name, domain_sid)
    for ace in write_dacl_aces_list:
        add_right_relationship(session, ace)


def generate_write_owner(session, dcou, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, domain_name, domain_sid):
    write_owner_aces_list = get_default_write_owner(dcou, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, domain_name, domain_sid)
    for ace in write_owner_aces_list:
        add_right_relationship(session, ace)


def generate_generic_all(session, dcou, dc_properties_list, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, domain_name, domain_sid):
    generic_all_aces_list = get_default_generic_all(dcou, dc_properties_list, computer_properties_list, user_properties_list, group_properties_list, ou_properties_list, gpos_properties_list, das, domain_name, domain_sid)
    for ace in generic_all_aces_list:
        add_right_relationship(session, ace)


def generate_outbound_acls(session, num_acl_principals, it_groups, it_users, gpos, computers, parameters):
    print("Adding outbound ACLs to {} objects".format(num_acl_principals))
    acls_probs = get_dict_param_value("ACLs", "ACLsProbability", parameters)
    acls_list = get_acls_list(acls_probs)
    acl_groups = random.sample(it_groups, num_acl_principals)
    all_principals = it_users + it_groups
    props = []
    print_acls_parameters(acls_probs)
    for i in acl_groups:
        ace = random.choice(acls_list)
        ace_string = '[r:' + ace + '{isacl:true, isinherited:false}]'
        if ace == "GenericAll" or ace == 'GenericWrite' or ace == 'WriteOwner' or ace == 'WriteDacl':
            p = random.choice(all_principals)
            p2 = random.choice(gpos)
            session.run('MERGE (n:Group {name:$group}) MERGE (m {name:$principal}) MERGE (n)-' + ace_string + '->(m)', group=i, principal=p)
            session.run('MERGE (n:Group {name:$group}) MERGE (m:GPO {name:$principal}) MERGE (n)-' + ace_string + '->(m)', group=i, principal=p2)
        elif ace == 'AddMember':
            p = random.choice(it_groups)
            session.run('MERGE (n:Group {name:$group}) MERGE (m:Group {name:$principal}) MERGE (n)-' + ace_string + '->(m)', group=i, principal=p)
        elif ace == 'ReadLAPSPassword':
            p = random.choice(all_principals)
            targ = random.choice(computers)
            session.run('MERGE (n {name:$principal}) MERGE (m:Computer {name:$target}) MERGE (n)-' + ace_string + '->(m)', target=targ, principal=p)
        else:
            p = random.choice(it_users)
            session.run('MERGE (n:Group {name:$group}) MERGE (m:User {name:$principal}) MERGE (n)-' + ace_string + '->(m)', group=i, principal=p)


def add_right_relationship(session, ad_object):
    query = "MATCH (identityReferenceItem:" + ad_object["IdentityReferenceType"] + " {objectid: '" + ad_object["IdentityReferenceId"] + "'}), (objectItem:" + ad_object["ObjectType"] + " {objectid: '" + ad_object["ObjectId"] + "'})"
    query = query + "\nMERGE (identityReferenceItem)-[:" + ad_object["Right"] + " {isacl: true, isinherited: " + str(ad_object["IsInherited"]) + "}]->(objectItem)"
    session.run(query)