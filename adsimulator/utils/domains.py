import random


def get_domain_dn(name):
    splitted_name = str(name).split(".")
    dn = "DC=" + splitted_name[0]
    for word in splitted_name[1:]:
        dn = dn + ",DC=" + word
    return dn


def generate_trust_sid():
    #"S-1-5-21-883232822-274137685-4173207997"
    return "S-1-5-21-" + str(random.randint(100000000, 999999999)) + "-" + str(random.randint(100000000, 999999999)) + "-" + str(random.randint(1000000000, 9999999999)) 
