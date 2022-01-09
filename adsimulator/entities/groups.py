from adsimulator.templates.groups import STANDARD_GROUPS


def get_forest_default_groups_list(domain_name, domain_sid, old_domain_name):
    groups_list = STANDARD_GROUPS
    for group in groups_list:
        group = set_group_attributes(group, domain_name, domain_sid, old_domain_name)
    return groups_list


def get_forest_default_group_members_list(domain_name, domain_sid, old_domain_name):
    forest_members_list = []
    groups_list = get_forest_default_groups_list(domain_name, domain_sid, old_domain_name)
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


def set_group_attributes(group, domain_name, domain_sid, old_domain_name):
    # TODO add old_sid
    domain_name_splitted = str(domain_name).split(".")
    if old_domain_name is not None:
        old_domain_name_splitted = str(old_domain_name).split(".")
        group["Properties"]["name"] = str(group["Properties"]["name"]).replace(str(old_domain_name), str(domain_name).upper())
    else:
        group["Properties"]["name"] = str(group["Properties"]["name"]).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    try:
        group["Properties"]["domain"] = str(domain_name).upper()
    except KeyError:
        pass
    if old_domain_name is not None:
        group["ObjectIdentifier"] = str(group["ObjectIdentifier"]).replace(str(old_domain_name).upper(), str(domain_name).upper())
    else:
        group["ObjectIdentifier"] = str(group["ObjectIdentifier"]).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    group["ObjectIdentifier"] = str(group["ObjectIdentifier"]).replace("DOMAIN_SID", domain_sid)
    try:
        if old_domain_name is not None:
            group["Properties"]["distinguishedname"] = str(group["Properties"]["distinguishedname"]).replace(str(old_domain_name_splitted[1]).upper(), str(domain_name_splitted[1]).upper())
            group["Properties"]["distinguishedname"] = str(group["Properties"]["distinguishedname"]).replace(str(old_domain_name_splitted[0]).upper(), str(domain_name_splitted[0]).upper())
        else:
            group["Properties"]["distinguishedname"] = str(group["Properties"]["distinguishedname"]).replace("DOMAIN_SUFFIX", str(domain_name_splitted[1]).upper())
            group["Properties"]["distinguishedname"] = str(group["Properties"]["distinguishedname"]).replace("DOMAIN_NAME", str(domain_name_splitted[0]).upper())
    except KeyError:
        pass
    return group


def get_group_member_id(member_id, domain_name, domain_sid):
    member_id = str(member_id).replace("DOMAIN_SID", domain_sid)
    member_id = str(member_id).replace("DOMAIN_NAME.DOMAIN_SUFFIX", str(domain_name).upper())
    return member_id