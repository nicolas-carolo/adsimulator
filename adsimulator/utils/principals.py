def get_name(name, domain_name):
    return f"{name}@{domain_name}"


def get_cn(name):
    return str(name).upper().split("@")[0]


def get_sid_from_rid(rid, domain_sid):
    return f"{domain_sid}-{str(rid)}"


def get_dn(name, ldap_path):
    cn = get_cn(name)
    return "CN=" + cn + "," + ldap_path
