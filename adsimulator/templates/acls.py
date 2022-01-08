ACLS_LIST = ["GenericAll"] * 10 + ["GenericWrite"] * 15 + ["WriteOwner"] * 15 + ["WriteDacl"] * \
            15 + ["AddMember"] * 30 + ["ForceChangePassword"] * \
            15 + ["ReadLAPSPassword"] * 10


def get_acls_list(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        return ACLS_LIST
    try:
        return ["GenericAll"] * prob["GenericAll"] +\
            ["GenericWrite"] * prob["GenericWrite"] +\
            ["WriteOwner"] * prob["WriteOwner"] +\
            ["WriteDacl"] * prob["WriteDacl"] +\
            ["Addmember"] * prob["AddMember"] +\
            ["ForceChangePassword"] * prob["ForceChangePassword"] +\
            ["ReadLAPSPassword"] * prob["ReadLAPSPassword"]
    except:
        return ACLS_LIST