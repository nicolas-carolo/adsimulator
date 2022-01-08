import json
from adsimulator.templates.default_values import DEFAULT_VALUES


def print_all_parameters(parameters):
    print("")
    print("New Settings:")
    print(json.dumps(parameters, indent=4, sort_keys=True))


def get_perc_param_value(node, key, parameters):
    try:
        if 0 <= parameters[node][key] <= 100:
            return parameters[node][key]
        else:
            return 100
    except:
        return DEFAULT_VALUES[node][key]


def get_dict_param_value(node, key, parameters):
    try:
        value = parameters[node][key]
        if type(value) == dict:
            return value
        else:
            return DEFAULT_VALUES[node][key]
    except:
        return DEFAULT_VALUES[node][key]


def get_int_param_value(node, key, parameters):
    try:
        value = parameters[node][key]
        if type(value) == int and value > 0:
            return value
        else:
            return DEFAULT_VALUES[node][key]
    except:
        return DEFAULT_VALUES[node][key]


def get_int_param_value_with_upper_limit(node, key, parameters, max_value):
    try:
        value = parameters[node][key]
        if type(value) == int and 0 < value <= max_value:
            return value
        if type(value) == int and value > max_value:
            return max_value
        else:
            return DEFAULT_VALUES[node][key]
    except:
        return DEFAULT_VALUES[node][key]


def print_computer_generation_parameters(enabled, has_laps, unconstrained_delegation, prob):
    print("\t- Enabled computer probability:", str(enabled), "%")
    print("\t- HasLaps computer probability:", str(has_laps), "%")
    print("\t- Unconstrained delegation computer probability:", str(unconstrained_delegation), "%")
    
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        prob = DEFAULT_VALUES["Computer"]["osProbability"]
    print("\t- Computer OS probability:")
    print("\t\t- Windows XP Professional Service Pack 3:", str(prob["Windows XP Professional Service Pack 3"]), "%")
    print("\t\t- Windows 7 Professional Service Pack 1:", str(prob["Windows 7 Professional Service Pack 1"]), "%")
    print("\t\t- Windows 7 Ultimate Service Pack 1:", str(prob["Windows 7 Ultimate Service Pack 1"]), "%")
    print("\t\t- Windows 7 Enterprise Service Pack 1:", str(prob["Windows 7 Enterprise Service Pack 1"]), "%")
    print("\t\t- Windows 10 Pro:", str(prob["Windows 10 Pro"]), "%")
    print("\t\t- Windows 10 Enterprise:", str(prob["Windows 10 Enterprise"]), "%")



def print_dc_generation_parameters(enabled, has_laps, prob):
    print("\t- Enabled DC probability:", str(enabled), "%")
    print("\t- HasLaps DC probability:", str(has_laps), "%")
    
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        prob = DEFAULT_VALUES["DC"]["osProbability"]
    print("\t- Domain Controller OS probability:")
    print("\t\t- Windows Server 2003 Enterprise Edition:", str(prob["Windows Server 2003 Enterprise Edition"]), "%")
    print("\t\t- Windows Server 2008 Standard:", str(prob["Windows Server 2008 Standard"]), "%")
    print("\t\t- Windows Server 2008 Datacenter:", str(prob["Windows Server 2008 Datacenter"]), "%")
    print("\t\t- Windows Server 2008 Enterprise:", str(prob["Windows Server 2008 Enterprise"]), "%")
    print("\t\t- Windows Server 2008 R2 Standard:", str(prob["Windows Server 2008 R2 Standard"]), "%")
    print("\t\t- Windows Server 2008 R2 Datacenter:", str(prob["Windows Server 2008 R2 Datacenter"]), "%")
    print("\t\t- Windows Server 2008 R2 Enterprise:", str(prob["Windows Server 2008 R2 Enterprise"]), "%")
    print("\t\t- Windows Server 2012 Standard:", str(prob["Windows Server 2012 Standard"]), "%")
    print("\t\t- Windows Server 2012 Datacenter:", str(prob["Windows Server 2012 Datacenter"]), "%")
    print("\t\t- Windows Server 2012 R2 Standard:", str(prob["Windows Server 2012 R2 Standard"]), "%")
    print("\t\t- Windows Server 2012 R2 Datacenter:", str(prob["Windows Server 2012 R2 Datacenter"]), "%")
    print("\t\t- Windows Server 2016 Standard:", str(prob["Windows Server 2016 Standard"]), "%")
    print("\t\t- Windows Server 2016 Datacenter:", str(prob["Windows Server 2016 Datacenter"]), "%")


def print_user_generation_parameters(enabled, dontreqpreauth, hasspn, passwordnotreqd, pwdneverexpires, unconstraineddelegation, sidhistory):
    print("\t- Enabled user probability:", str(enabled), "%")
    print("\t- Dontreqpreauth user probability:", str(dontreqpreauth), "%")
    print("\t- Dontreqpreauth user probability:", str(dontreqpreauth), "%")
    print("\t- Hasspn user probability:", str(hasspn), "%")
    print("\t- Passwordnotreqd user probability:", str(passwordnotreqd), "%")
    print("\t- Pwdneverexpires user probability:", str(pwdneverexpires), "%")
    print("\t- Unconstrained delegation user probability:", str(unconstraineddelegation), "%")
    print("\t- User has SID History probability:", str(sidhistory), "%")


def print_domain_generation_parameters(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        prob = DEFAULT_VALUES["Domain"]["functionalLevelProbability"]
    print("\t- Functional level probability:")
    print("\t\t- 2008:", str(prob["2008"]), "%")
    print("\t\t- 2008 R2:", str(prob["2008 R2"]), "%")
    print("\t\t- 2012:", str(prob["2012"]), "%")
    print("\t\t- 2012 R2:", str(prob["2012 R2"]), "%")
    print("\t\t- 2016:", str(prob["2016"]), "%")
    print("\t\t- Unknown:", str(prob["Unknown"]), "%")


def print_departments_parameters(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        prob = DEFAULT_VALUES["Group"]["departmentProbability"]
    print("\t- Department probability:")
    print("\t\t- IT:", str(prob["IT"]), "%")
    print("\t\t- HR:", str(prob["HR"]), "%")
    print("\t\t- MARKETING:", str(prob["MARKETING"]), "%")
    print("\t\t- OPERATIONS:", str(prob["OPERATIONS"]), "%")
    print("\t\t- BIDNESS:", str(prob["BIDNESS"]), "%")


def print_acls_parameters(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        prob = DEFAULT_VALUES["ACLs"]["ACLsProbability"]
    print("\t- ACLs probability:")
    print("\t\t- GenericAll:", str(prob["GenericAll"]), "%")
    print("\t\t- GenericWrite:", str(prob["GenericWrite"]), "%")
    print("\t\t- WriteOwner:", str(prob["WriteOwner"]), "%")
    print("\t\t- WriteDacl:", str(prob["WriteDacl"]), "%")
    print("\t\t- AddMember:", str(prob["AddMember"]), "%")
    print("\t\t- ForceChangePassword:", str(prob["ForceChangePassword"]), "%")
    print("\t\t- ReadLAPSPassword:", str(prob["ReadLAPSPassword"]), "%")