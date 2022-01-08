from adsimulator.templates.groups import STANDARD_GROUPS


def get_forest_default_groups_list(domain_name, domain_sid):
    groups_list = STANDARD_GROUPS
    for group in groups_list:
        group = set_group_attributes(group, domain_name, domain_sid)
    return groups_list


def get_forest_default_group_members_list(domain_name, domain_sid):
    forest_members_list = []
    groups_list = get_forest_default_groups_list(domain_name, domain_sid)
    for group in groups_list:
        domain_members_list = group["Members"]
        for member in domain_members_list:
            item = {
                "GroupId": group["ObjectIdentifier"],
                "GroupName": group["Properties"]["name"],
                "MemberId": get_group_member_id(member["MemberId"], domain_name, domain_sid),
                "MemberType": member["MemberType"]
            }
            forest_members_list.append(item)
        """
        if str(group["ObjectIdentifier"]).startswith("S-1-5-21") and str(group["ObjectIdentifier"]).endswith("-513"):
            add_domain_users_membership(group, domains_json, ous_json, forest_members_list)
        if str(group["ObjectIdentifier"]).startswith("S-1-5-21") and str(group["ObjectIdentifier"]).endswith("-514"):
            add_domain_guests_membership(group, domains_json, forest_members_list)
        if str(group["ObjectIdentifier"]).startswith("S-1-5-21") and str(group["ObjectIdentifier"]).endswith("-515"):
            add_domain_computers_membership(group, domains_json, ous_json, forest_members_list)
        if str(group["ObjectIdentifier"]).startswith("S-1-5-21") and str(group["ObjectIdentifier"]).endswith("-516"):
            add_domain_controllers_membership(group, ous_json, forest_members_list)
        """
    return forest_members_list


def set_group_attributes(group, domain_name, domain_sid):
    domain_name_splitted = str(domain_name).split(".")
    group["Properties"]["name"] = str(group["Properties"]["name"]).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    try:
        group["Properties"]["domain"] = str(domain_name).upper()
    except KeyError:
        pass
    group["ObjectIdentifier"] = str(group["ObjectIdentifier"]).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    group["ObjectIdentifier"] = str(group["ObjectIdentifier"]).replace("DOMAIN_SID", domain_sid)
    try:
        group["Properties"]["distinguishedname"] = str(group["Properties"]["distinguishedname"]).replace("DOMAIN_SUFFIX", str(domain_name_splitted[1]).upper())
        group["Properties"]["distinguishedname"] = str(group["Properties"]["distinguishedname"]).replace("DOMAIN_NAME", str(domain_name_splitted[0]).upper())
    except KeyError:
        pass
    return group


def get_group_member_id(member_id, domain_name, domain_sid):
    member_id = str(member_id).replace("DOMAIN_SID", domain_sid)
    member_id = str(member_id).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    return member_id