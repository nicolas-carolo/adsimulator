from adsimulator.templates.users import GUEST_USER, DEFAULT_ACCOUNT, ADMINISTRATOR, KRBTGT


def get_guest_user(domain_name, domain_sid): 
    return set_user_attributes(GUEST_USER, domain_name, domain_sid)


def get_default_account(domain_name, domain_sid): 
    return set_user_attributes(DEFAULT_ACCOUNT, domain_name, domain_sid)


def get_administrator_user(domain_name, domain_sid): 
    return set_user_attributes(ADMINISTRATOR, domain_name, domain_sid)


def get_krbtgt_user(domain_name, domain_sid): 
    return set_user_attributes(KRBTGT, domain_name, domain_sid)


def set_user_attributes(user, domain_name, domain_sid):
    domain_name_splitted = str(domain_name).split(".")
    user["Properties"]["name"] = str(user["Properties"]["name"]).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    user["Properties"]["domain"] = str(domain_name).upper()
    user["ObjectIdentifier"] = str(user["ObjectIdentifier"]).replace("DOMAIN_SID", domain_sid)
    user["Properties"]["distinguishedname"] = str(user["Properties"]["distinguishedname"]).replace("DOMAIN_SUFFIX", str(domain_name_splitted[1]).upper())
    user["Properties"]["distinguishedname"] = str(user["Properties"]["distinguishedname"]).replace("DOMAIN_NAME", str(domain_name_splitted[0]).upper())
    return user


def get_standard_users_list():
    return [GUEST_USER, DEFAULT_ACCOUNT, ADMINISTRATOR, KRBTGT]


def get_forest_user_sid_list(domain_name, domain_sid):
    user_sid_list = []
    domain_users_list = []
    for user in get_standard_users_list():
        domain_users_list.append(set_user_attributes(user, domain_name, domain_sid))
    for user in domain_users_list:
        item = {
            "DomainId": domain_sid,
            "DomainName": str(domain_name).upper(),
            "ObjectId": user["ObjectIdentifier"],
            "ObjectType": "User"
        }
        user_sid_list.append(item)
    return user_sid_list