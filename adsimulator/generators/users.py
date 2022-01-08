import random
from adsimulator.utils.principals import get_cn, get_sid_from_rid, get_dn
from adsimulator.utils.users import get_user_timestamp, generate_sid_history
from adsimulator.utils.boolean import generate_boolean_value
from adsimulator.utils.parameters import get_perc_param_value, print_user_generation_parameters
from adsimulator.entities.users import get_guest_user, get_default_account, get_administrator_user, get_krbtgt_user,\
    get_forest_user_sid_list
from adsimulator.templates.default_values import get_complementary_value


def generate_guest_user(session, domain_name, domain_sid, parameters):
    guest_user = get_guest_user(domain_name, domain_sid)
    generate_user(session, guest_user, parameters)


def generate_default_account(session, domain_name, domain_sid, parameters):
    default_account = get_default_account(domain_name, domain_sid) 
    generate_user(session, default_account, parameters)


def generate_administrator(session, domain_name, domain_sid, parameters):
    administrator_user = get_administrator_user(domain_name, domain_sid)
    generate_user(session, administrator_user, parameters)


def generate_krbtgt_user(session, domain_name, domain_sid, parameters):
    krbtgt_user = get_krbtgt_user(domain_name, domain_sid)
    generate_user(session, krbtgt_user, parameters)


def generate_user(session, user, parameters):
    if get_cn(user["Properties"]["name"]) == "GUEST":
        enabled_property = random.choice([True, False])
        pwdneverexpires_property = random.choice([True, False])
    else:
        enabled_property = user["Properties"]["enabled"]
        pwdneverexpires_property = user["Properties"]["pwdneverexpires"]

    # New properties
    savedcredentials_perc = get_perc_param_value("User", "savedcredentials", parameters)
    savedcredentials = generate_boolean_value(savedcredentials_perc, get_complementary_value(savedcredentials_perc))

    session.run(
        """
        MERGE (n:Base {name: $name}) SET n:User, n.objectid=$sid,
        n.highvalue=$highvalue, n.domain=$domain,
        n.distinguishedname=$distinguishedname,
        n.description=$description, n.admincount=$admincount,
        n.dontreqpreauth=$dontreqpreauth, n.passwordnotreqd=$passwordnotreqd,
        n.unconstraineddelegation=$unconstraineddelegation,
        n.sensitive=$sensitive, n.enabled=$enabled,
        n.pwdneverexpires=$pwdneverexpires, n.lastlogon=$lastlogon,
        n.lastlogontimestamp=$lastlogontimestamp, n.pwdlastset=$pwdlastset,
        n.serviceprincipalnames=$serviceprincipalnames, n.hasspn=$hasspn,
        n.displayname=$displayname, n.email=$email, n.title=$title,
        n.homedirectory=$homedirectory, n.userpassword=$userpassword,
        n.sidhistory=$sidhistory, n.savedcredentials=$savedcredentials
        """,
        name=user["Properties"]["name"],
        sid=user["ObjectIdentifier"],
        highvalue=user["Properties"]["highvalue"],
        domain=user["Properties"]["domain"],
        distinguishedname=user["Properties"]["distinguishedname"],
        description=user["Properties"]["description"],
        admincount=user["Properties"]["admincount"],
        dontreqpreauth=user["Properties"]["dontreqpreauth"],
        passwordnotreqd=user["Properties"]["passwordnotreqd"],
        unconstraineddelegation=user["Properties"]["unconstraineddelegation"],
        sensitive=user["Properties"]["sensitive"],
        enabled=enabled_property,
        pwdneverexpires=pwdneverexpires_property,
        lastlogon=user["Properties"]["lastlogon"],
        lastlogontimestamp=user["Properties"]["lastlogontimestamp"],
        pwdlastset=user["Properties"]["pwdlastset"],
        serviceprincipalnames=user["Properties"]["serviceprincipalnames"],
        hasspn=user["Properties"]["hasspn"],
        displayname=user["Properties"]["displayname"],
        email=user["Properties"]["email"],
        title=user["Properties"]["title"],
        homedirectory=user["Properties"]["homedirectory"],
        userpassword=user["Properties"]["userpassword"],
        sidhistory=user["Properties"]["sidhistory"],
        savedcredentials=savedcredentials
    )


def link_default_users_to_domain(session, domain_name, domain_sid):
    standard_users_list = get_forest_user_sid_list(domain_name, domain_sid)
    for user in standard_users_list:
        add_contains_object_on_domain_relationship(session, user)


def add_contains_object_on_domain_relationship(session, ad_object):
        query = "MATCH (objectItem:" + ad_object["ObjectType"] + " {objectid: '" + ad_object["ObjectId"] + "'}), (domainItem:Domain {objectid: '" + ad_object["DomainId"] + "'})"
        query = query + "\nMERGE (domainItem)-[:Contains {isacl:false}]->(objectItem)"
        session.run(query)


def generate_users(session, domain_name, domain_sid, num_nodes, current_time, first_names, last_names, users, ridcount, parameters):
    user_properties_list = []
    group_name = "DOMAIN USERS@{}".format(domain_name)
    enabled_perc = get_perc_param_value("User", "enabled", parameters)
    dontreqpreauth_perc = get_perc_param_value("User", "dontreqpreauth", parameters)
    hasspn_perc = get_perc_param_value("User", "hasspn", parameters)
    passwordnotreqd_perc = get_perc_param_value("User", "passwordnotreqd", parameters)
    pwdneverexpires_perc = get_perc_param_value("User", "pwdneverexpires", parameters)
    unconstraineddelegation_perc = get_perc_param_value("User", "unconstraineddelegation", parameters)
    sidhistory_perc = get_perc_param_value("User", "sidhistory", parameters)

    # New properties
    savedcredentials_perc = get_perc_param_value("User", "savedcredentials", parameters)

    print_user_generation_parameters(enabled_perc, dontreqpreauth_perc, hasspn_perc, passwordnotreqd_perc, pwdneverexpires_perc, unconstraineddelegation_perc, sidhistory_perc)
    props = []
    for i in range(1, num_nodes + 1):
        first = random.choice(first_names)
        last = random.choice(last_names)
        user_name = "{}{}{:05d}@{}".format(first[0], last, i, domain_name).upper()
        user_name = user_name.format(first[0], last, i).upper()
        users.append(user_name)
        dispname = "{} {}".format(first, last)
        enabled = generate_boolean_value(enabled_perc, get_complementary_value(enabled_perc))
        dontreqpreauth = generate_boolean_value(dontreqpreauth_perc, get_complementary_value(dontreqpreauth_perc))
        hasspn = generate_boolean_value(hasspn_perc, get_complementary_value(hasspn_perc))
        passwordnotreqd = generate_boolean_value(passwordnotreqd_perc, get_complementary_value(passwordnotreqd_perc))
        pwdneverexpires = generate_boolean_value(pwdneverexpires_perc, get_complementary_value(pwdneverexpires_perc))
        unconstraineddelegation = generate_boolean_value(unconstraineddelegation_perc, get_complementary_value(unconstraineddelegation_perc))
        sidhistory = generate_sid_history(sidhistory_perc, get_complementary_value(sidhistory_perc))
        pwdlastset = get_user_timestamp(current_time, enabled)
        lastlogon = get_user_timestamp(current_time, enabled)
        objectsid = get_sid_from_rid(ridcount, domain_sid)

        # New properties
        savedcredentials = generate_boolean_value(savedcredentials_perc, get_complementary_value(savedcredentials_perc))

        ridcount += 1

        user_property = {
            'id': objectsid,
            'props': {
                'displayname': dispname,
                'name': user_name,
                'enabled': enabled,
                'pwdlastset': pwdlastset,
                'lastlogon': lastlogon,
                'lastlogontimestamp': lastlogon,
                'highvalue': False,
                'dontreqpreauth': dontreqpreauth,
                'hasspn': hasspn,
                'passwordnotreqd': passwordnotreqd,
                'pwdneverexpires': pwdneverexpires,
                'sensitive': False,
                'serviceprincipalnames': "",
                'sidhistory': sidhistory,
                'unconstraineddelegation': unconstraineddelegation,
                "description": "null",
                "admincount": False,
                "savedcredentials": savedcredentials
            }
        }
        props.append(user_property)
        user_properties_list.append(user_property)
        if (len(props) > 500):
            session.run('UNWIND $props as prop MERGE (n:Base {objectid:prop.id}) SET n:User, n += prop.props WITH n MATCH (m:Group {name:$gname}) WITH n,m MERGE (n)-[:MemberOf]->(m)', props=props, gname=group_name)
            props = []

    session.run('UNWIND $props as prop MERGE (n:Base {objectid:prop.id}) SET n:User, n += prop.props WITH n MATCH (m:Group {name:$gname}) WITH n,m MERGE (n)-[:MemberOf {isacl:false}]->(m)', props=props, gname=group_name)
    return user_properties_list, users, ridcount


def assign_kerberoastable_users(session, it_users):
    i = random.randint(10, 20)
    i = min(i, len(it_users))
    for user in random.sample(it_users, i):
        session.run('MATCH (n:User {name:$user}) SET n.hasspn=true', user=user)


def set_user_dn(session, user_name, ou_dn):
    user_dn = get_dn(user_name, ou_dn)
    query = "MATCH (n:User { name: '" + user_name + "' }) SET n.distinguishedname = '" + user_dn + "' RETURN n.name, n.distinguishedname"
    session.run(query)
