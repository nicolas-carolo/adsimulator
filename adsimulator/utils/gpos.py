def get_gpo_dn(cn, domain_dn):
    return "CN=" + cn + ",CN=Policies,CN=System," + domain_dn


def get_gpc_path(cn, domain_name):
    return "\\\\" + domain_name + "\\sysvol\\" + domain_name + "\\Policies\\" + cn