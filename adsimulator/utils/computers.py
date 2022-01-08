from adsimulator.templates.computers import VULNERABLE_OS_LIST


def get_cn(name):
    return str(name).upper().split(".")[0]


def get_computer_dn(name, ldap_path):
    cn = get_cn(name)
    return "CN=" + cn + "," + ldap_path


def get_computer_name(name, domain_name):
    return f"{name}.{domain_name}"


def generate_client_service_pricipal_names(name):
    cn = get_cn(name)
    return f"TERMSRV/{name},TERMSRV/{name},RestrictedKrbHost/{cn},HOST/{cn},RestrictedKrbHost/{name},HOST/{name}"


def generate_server_service_pricipal_names(name, domain_name):
    cn = get_cn(name)
    domain_cn = get_cn(domain_name)
    return f"Dfsr-12F9A27C-BF97-4787-9364-D31B6C55EB04/{name},ldap/{name}/ForestDnsZones.{domain_name},ldap/{name}/DomainDnsZones.{domain_name},TERMSRV/{name},TERMSRV/{name},DNS/{name},GC/{name}/{domain_name},RestrictedKrbHost/{name},RestrictedKrbHost/{cn},RPC/794cea05-ab54-42e3-aa9e-f4b3d116117a._msdcs.{domain_name},HOST/{cn}/{domain_cn},HOST/{name}/{domain_cn},HOST/{cn},HOST/{name},HOST/{name}/{domain_name},E3514235-4B06-11D1-AB04-00C04FC2DCD2/794cea05-ab54-42e3-aa9e-f4b3d116117a/{domain_name},ldap/{cn}/{domain_cn},ldap/794cea05-ab54-42e3-aa9e-f4b3d116117a._msdcs.{domain_name},ldap/{name}/{domain_cn},ldap/{cn},ldap/{name},ldap/{name}/{domain_name}"


def is_os_vulnerable(os):
    for vulnerable_os in VULNERABLE_OS_LIST:
        if vulnerable_os in os:
            return True
    else:
        return False