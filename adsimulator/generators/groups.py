import random
import math
from adsimulator.entities.groups import get_forest_default_groups_list, get_forest_default_group_members_list
from adsimulator.templates.groups import get_departments_list
from adsimulator.utils.principals import get_sid_from_rid, get_name
from adsimulator.utils.groups import get_group_dn, generate_group_description
from adsimulator.utils.boolean import generate_boolean_value
from adsimulator.templates.default_values import get_complementary_value
from adsimulator.utils.parameters import get_dict_param_value, print_departments_parameters



def generate_default_groups(session, domain_name, domain_sid, old_domain_name):
    default_groups_list = get_forest_default_groups_list(domain_name, domain_sid, old_domain_name)
    for default_group in default_groups_list:
        try:
            session.run(
                """
                MERGE (n:Base {name: $gname}) SET n:Group, n.objectid=$sid,
                n.highvalue=$highvalue, n.domain=$domain,
                n.distinguishedname=$distinguishedname,
                n.description=$description, n.admincount=$admincount
                """,
                gname=default_group["Properties"]["name"],
                sid=default_group["ObjectIdentifier"],
                highvalue=default_group["Properties"]["highvalue"],
                domain=default_group["Properties"]["domain"],
                distinguishedname=default_group["Properties"]["distinguishedname"],
                description=default_group["Properties"]["description"],
                admincount=default_group["Properties"]["admincount"]
            )
        except KeyError:
            default_group_properties = default_group["Properties"]
            if not "highvalue" in default_group_properties:
                highvalue = "null"
            else:
                highvalue = default_group["Properties"]["highvalue"]
            if not "distinguishedname" in default_group_properties:
                dn = "null"
            else:
                dn = default_group["Properties"]["distinguishedname"]
            if not "description" in default_group_properties:
                description = "null"
            else:
                description = default_group["Properties"]["description"]
            if not "admincount" in default_group_properties:
                admincount = "null"
            else:
                admincount = default_group["Properties"]["admincount"]
            if not "domain" in default_group_properties:
                domain = "null"
            else:
                domain = default_group["Properties"]["domain"]
            
            session.run(
                """
                MERGE (n:Base {name: $gname}) SET n:Group, n.objectid=$sid,
                n.highvalue=$highvalue, n.domain=$domain,
                n.distinguishedname=$distinguishedname,
                n.description=$description, n.admincount=$admincount
                """,
                gname=default_group["Properties"]["name"],
                sid=default_group["ObjectIdentifier"],
                highvalue=highvalue,
                domain=domain,
                distinguishedname=dn,
                description=description,
                admincount=admincount
            )


def generate_groups(session, domain_name, domain_sid, domain_dn, num_nodes, groups, ridcount, parameters):
    departments_probs = get_dict_param_value("Group", "departmentProbability", parameters)
    departments_list = get_departments_list(departments_probs)
    props = []
    group_properties_list = []
    print_departments_parameters(departments_probs)
    for i in range(1, num_nodes + 1):
        dept = random.choice(departments_list)
        group_name = "{}{:05d}@{}".format(dept, i, domain_name)
        groups.append(group_name)
        sid = get_sid_from_rid(ridcount, domain_sid)
        ridcount += 1
        group_properties = {
            'name': group_name,
            'id': sid,
            'dn': get_group_dn(group_name, domain_dn),
            'admincount': False,
            'description': generate_group_description(group_name),
            'highvalue': False
        }
        props.append(group_properties)
        group_properties_list.append(group_properties)
        if len(props) > 500:
            session.run(
                """
                UNWIND $props as prop
                MERGE (n:Base {objectid:prop.id})
                SET n:Group, n.name=prop.name, n.distinguishedname=prop.dn, n.admincount=prop.admincount,
                n.description=prop.description, n.highvalue=prop.highvalue
                """,
                props=props
            )
            props = []

    session.run(
        """
        UNWIND $props as prop
        MERGE (n:Base {objectid:prop.id})
        SET n:Group, n.name=prop.name, n.distinguishedname=prop.dn, n.admincount=prop.admincount,
        n.description=prop.description, n.highvalue=prop.highvalue
        """,
        props=props
    )
    return group_properties_list, groups, ridcount


def generate_domain_administrators(session, domain_name, num_nodes, users):
    dapctint = random.randint(3, 5)
    dapct = float(dapctint) / 100
    danum = int(math.ceil(num_nodes * dapct))
    danum = min([danum, 30])
    print("Generating {} Domain Admins ({}% of users capped at 30)".format(danum, dapctint))
    das = random.sample(users, danum)
    for da in das:
        session.run(
            """
            MERGE (n:User {name:$name})
            WITH n
            MERGE (m:Group {name:$gname})
            WITH n,m
            MERGE (n)-[:MemberOf {isacl:false}]->(m)
            SET n.admincount = true
            """,
            name=da,
            gname=get_name("DOMAIN ADMINS", domain_name))
    return das


def generate_default_member_of(session, domain_name, domain_sid, old_domain_name):
    standard_group_members_list = get_forest_default_group_members_list(domain_name, domain_sid, old_domain_name)
    for group_member in standard_group_members_list:
        add_member_of_relationship(session, group_member)


def add_member_of_relationship(session, ad_object):
    query = "MATCH (memberItem:" + ad_object["MemberType"] + " {objectid: '" + ad_object["MemberId"] + "'}), (groupItem:Group {objectid: '" + ad_object["GroupId"] + "'})"
    query = query + "\nMERGE (memberItem)-[:MemberOf {isacl:false}]->(groupItem)"
    session.run(query)


def nest_groups(session, num_nodes, groups, nesting_perc):
    max_nest = int(round(math.log10(num_nodes)))
    props = []
    for group in groups:
        if generate_boolean_value(nesting_perc, get_complementary_value(nesting_perc)):
            try:
                num_nest = random.randrange(1, max_nest)
            except ValueError:
                num_nest = 1
            dept = group[0:-19]
            dpt_groups = [x for x in groups if dept in x]
            if num_nest > len(dpt_groups):
                num_nest = random.randrange(1, len(dpt_groups))
            to_nest = random.sample(dpt_groups, num_nest)
            for g in to_nest:
                if not g == group:
                    props.append({'a': group, 'b': g})

        if (len(props) > 500):
            session.run('UNWIND $props AS prop MERGE (n:Group {name:prop.a}) WITH n,prop MERGE (m:Group {name:prop.b}) WITH n,m MERGE (n)-[:MemberOf {isacl:false}]->(m)', props=props)
            props = []

    session.run('UNWIND $props AS prop MERGE (n:Group {name:prop.a}) WITH n,prop MERGE (m:Group {name:prop.b}) WITH n,m MERGE (n)-[:MemberOf {isacl:false}]->(m)', props=props)


def assign_users_to_group(session, num_nodes, users, groups, das, parameters):
    props = []
    a = math.log10(num_nodes)
    a = math.pow(a, 2)
    a = math.floor(a)
    a = int(a)
    num_groups_base = a
    variance = int(math.ceil(math.log10(num_nodes)))
    it_users = []

    print("Calculated {} groups per user with a variance of - {}".format(num_groups_base, variance*2))
    departments_probs = get_dict_param_value("Group", "departmentProbability", parameters)
    departments_list = get_departments_list(departments_probs)
    for user in users:
        dept = random.choice(departments_list)
        if dept == "IT":
            it_users.append(user)
        possible_groups = [x for x in groups if dept in x]

        sample = num_groups_base + random.randrange(-(variance*2), 0)
        if (sample > len(possible_groups)):
            sample = int(math.floor(float(len(possible_groups)) / 4))

        if (sample <= 1):
            continue

        to_add = random.sample(possible_groups, sample)

        for group in to_add:
            props.append({'a': user, 'b': group})

        if len(props) > 500:
            session.run('UNWIND $props AS prop MERGE (n:User {name:prop.a}) WITH n,prop MERGE (m:Group {name:prop.b}) WITH n,m MERGE (n)-[:MemberOf {isacl:false}]->(m)', props=props)
            props = []

    session.run('UNWIND $props AS prop MERGE (n:User {name:prop.a}) WITH n,prop MERGE (m:Group {name:prop.b}) WITH n,m MERGE (n)-[:MemberOf {isacl:false}]->(m)', props=props)

    it_users = it_users + das
    it_users = list(set(it_users))
    return it_users
