from adsimulator.utils.principals import get_cn


def get_ou_dn(ou_name, domain_dn):
    return "OU=" + get_cn(ou_name) + "," + domain_dn