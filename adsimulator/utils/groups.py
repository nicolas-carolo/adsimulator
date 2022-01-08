import re
from adsimulator.utils.principals import get_cn


def get_group_dn(name, domain_dn):
    cn = get_cn(name)
    return "CN=" + cn + ",CN=Builtin," + domain_dn


def generate_group_description(name):
    cn = get_cn(name)
    group_type_list = re.split("[^a-zA-Z]*", cn)
    group_type = ""
    for char in group_type_list:
        group_type += char
    group_type = str(group_type).lower()
    if len(group_type) == 2:
        group_type = str(group_type).upper()
    if str(group_type).lower().startswith(("a", "e", "i", "o", "u")):
        return f"This is an {group_type} group"
    else:
        return f"This is a {group_type} group"
    