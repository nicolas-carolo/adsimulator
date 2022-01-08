DEFAULT_VALUES = {
    "Domain": {
        "functionalLevelProbability": {
            "2008": 4,
            "2008 R2": 5,
            "2012": 10,
            "2012 R2": 30,
            "2016": 50,
            "Unknown": 1
        },
        "Trusts": {
            "SIDFilteringProbability": 50,
            "Inbound": 1,
            "Outbound": 1,
            "Bidirectional": 1
        }
    },
    "Computer": {
        "nComputers": 100,
        "CanRDPFromUserPercentage": 10,
        "CanRDPFromGroupPercentage": 10,
        "CanPSRemoteFromUserPercentage": 10,
        "CanPSRemoteFromGroupPercentage": 10,
        "ExecuteDCOMFromUserPercentage": 10,
        "ExecuteDCOMFromGroupPercentage": 10,
        "AllowedToDelegateFromUserPercentage": 10,
        "AllowedToDelegateFromComputerPercentage": 10,
        "enabled": 90,
        "haslaps": 10,
        "unconstraineddelegation": 10,
        "osProbability": {
            "Windows XP Professional Service Pack 3": 3,
            "Windows 7 Professional Service Pack 1": 7,
            "Windows 7 Ultimate Service Pack 1": 5,
            "Windows 7 Enterprise Service Pack 1": 15,
            "Windows 10 Pro": 30,
            "Windows 10 Enterprise": 40
        },
        "privesc": 30,
        "creddump": 40,
        "exploitable": 40
    },
    "DC": {
        "enabled": 90,
        "haslaps": 10,
        "osProbability": {
            "Windows Server 2003 Enterprise Edition": 1,
            "Windows Server 2008 Standard": 1,
            "Windows Server 2008 Datacenter": 1,
            "Windows Server 2008 Enterprise": 1,
            "Windows Server 2008 R2 Standard": 2,
            "Windows Server 2008 R2 Datacenter": 3,
            "Windows Server 2008 R2 Enterprise": 3,
            "Windows Server 2012 Standard": 4,
            "Windows Server 2012 Datacenter": 4,
            "Windows Server 2012 R2 Standard": 10,
            "Windows Server 2012 R2 Datacenter": 10,
            "Windows Server 2016 Standard": 35,
            "Windows Server 2016 Datacenter": 25
        }
    },
    "User": {
        "nUsers": 100,
        "enabled": 85,
        "dontreqpreauth": 5,
        "hasspn": 10,
        "passwordnotreqd": 5,
        "pwdneverexpires": 50,
        "sidhistory": 10,
        "unconstraineddelegation": 20,
        "savedcredentials": 40
    },
    "OU": {
        "nOUs": 20
    },
    "Group": {
        "nGroups": 100,
        "nestingGroupProbability": 30,
        "departmentProbability": {
            "IT": 20,
            "HR": 20,
            "MARKETING": 20,
            "OPERATIONS": 20,
            "BIDNESS": 20
        }
    },
    "GPO": {
        "nGPOs": 20,
        "exploitable": 30
    },
    "ACLs": {
        "ACLPrincipalsPercentage": 50,
        "ACLsProbability": {
            "GenericAll": 10,
            "GenericWrite": 15,
            "WriteOwner": 15,
            "WriteDacl": 15,
            "AddMember": 30,
            "ForceChangePassword": 15,
            "ReadLAPSPassword": 10
        }
    }
}


def get_complementary_value(value):
    return 100 - value