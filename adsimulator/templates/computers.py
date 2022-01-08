import random


CLIENT_OS_LIST = ["Windows 7 Professional Service Pack 1"] * 7 + ["Windows 7 Ultimate Service Pack 1"] * 5 +\
            ["Windows 7 Enterprise Service Pack 1"] * 15 + \
            ["Windows 10 Pro"] * 30 + ["Windows 10 Enterprise"] * 40 +\
            ["Windows XP Professional Service Pack 3"] * 3


SERVER_OS_LIST = ["Windows Server 2003 Enterprise Edition"] * 1 + ["Windows Server 2008 Standard"] * 1 +\
            ["Windows Server 2008 Enterprise"] * 1 + ["Windows Server 2008 Datacenter"] * 1 +\
            ["Windows Server 2008 R2 Standard"] * 2 +\
            ["Windows Server 2008 R2 Enterprise"] * 3 + ["Windows Server 2008 R2 Datacenter"] * 3 +\
            ["Windows Server 2012 Standard"] * 4 + ["Windows Server 2012 Datacenter"] * 4 +\
            ["Windows Server 2012 R2 Standard"] * 10 + ["Windows Server 2012 R2 Datacenter"] * 10 +\
            ["Windows Server 2016 Datacenter"] * 25 + ["Windows Server 2016 Standard"] * 35


VULNERABLE_OS_LIST = ["Windows XP", "Windows 7", "Windows Server 2003", "Windows Server 2008"]


def get_client_os_list(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        return CLIENT_OS_LIST
    try:
        return ["Windows 7 Professional Service Pack 1"] * prob["Windows 7 Professional Service Pack 1"] +\
            ["Windows 7 Ultimate Service Pack 1"] * prob["Windows 7 Ultimate Service Pack 1"] +\
            ["Windows 7 Enterprise Service Pack 1"] * prob["Windows 7 Enterprise Service Pack 1"] +\
            ["Windows 10 Pro"] * prob["Windows 10 Pro"] +\
            ["Windows 10 Enterprise"] * prob["Windows 10 Enterprise"] +\
            ["Windows XP Professional Service Pack 3"] * prob["Windows XP Professional Service Pack 3"]
    except:
        return CLIENT_OS_LIST


def get_server_os_list(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        return SERVER_OS_LIST
    try:
        return ["Windows Server 2003 Enterprise Edition"] * prob["Windows Server 2003 Enterprise Edition"] +\
            ["Windows Server 2008 Standard"] * prob["Windows Server 2008 Standard"] +\
            ["Windows Server 2008 Enterprise"] * prob["Windows Server 2008 Enterprise"] +\
            ["Windows Server 2008 Datacenter"] * prob["Windows Server 2008 Datacenter"] +\
            ["Windows Server 2008 R2 Standard"] * prob["Windows Server 2008 R2 Standard"] +\
            ["Windows Server 2008 R2 Enterprise"] * prob["Windows Server 2008 R2 Enterprise"] +\
            ["Windows Server 2008 R2 Datacenter"] * prob["Windows Server 2008 R2 Datacenter"] +\
            ["Windows Server 2012 Standard"] * prob["Windows Server 2012 Standard"] +\
            ["Windows Server 2012 Datacenter"] * prob["Windows Server 2012 Datacenter"] +\
            ["Windows Server 2012 R2 Standard"] * prob["Windows Server 2012 R2 Standard"] +\
            ["Windows Server 2012 R2 Datacenter"] * prob["Windows Server 2012 R2 Datacenter"] +\
            ["Windows Server 2016 Datacenter"] * prob["Windows Server 2016 Datacenter"] +\
            ["Windows Server 2016 Standard"] * prob["Windows Server 2016 Standard"]
    except:
        return SERVER_OS_LIST


def get_main_dc_os(functional_level):
    if functional_level == "2008":
        return random.choice(["Windows Server 2008 Standard", "Windows Server 2008 Enterprise", "Windows Server 2008 Datacenter"])
    elif functional_level == "2008 R2":
        return random.choice(["Windows Server 2008 R2 Standard", "Windows Server 2008 R2 Enterprise", "Windows Server 2008 R2 Datacenter"])
    elif functional_level == "2012":
        return random.choice(["Windows Server 2012 Standard", "Windows Server 2012 Datacenter"])
    elif functional_level == "2012 R2":
        return random.choice(["Windows Server 2012 R2 Standard", "Windows Server 2012 R2 Datacenter"])
    elif functional_level == "2016":
        return random.choice(["Windows Server 2016 Standard", "Windows Server 2016 Datacenter"])
    else:
        return random.choice(SERVER_OS_LIST)
