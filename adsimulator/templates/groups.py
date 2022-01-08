DEPARTMENTS_LIST = ["IT"] * 20 + ["HR"] * 20 + \
            ["MARKETING"] * 20 + ["OPERATIONS"] * 20 + ["BIDNESS"] * 20


STANDARD_GROUPS = [
    {
        "Properties": {
        "highvalue": True,
        "name": "ADMINISTRATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
        "distinguishedname": "CN=Administrators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Administrators have complete and unrestricted access to the computer/domain",
        "admincount": True
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-512",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-519",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-500",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "REMOTE DESKTOP USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-555",
        "distinguishedname": "CN=Remote Desktop Users,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members in this group are granted the right to logon remotely",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-555",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "PRINT OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-550",
        "distinguishedname": "CN=Print Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members can administer printers installed on domain controllers",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-550",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "IIS_IUSRS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-568",
        "distinguishedname": "CN=IIS_IUSRS,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Built-in group used by Internet Information Services.",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-17",
          "MemberType": "Group"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-568",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "BACKUP OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-551",
        "distinguishedname": "CN=Backup Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Backup Operators can override security restrictions for the sole purpose of backing up or restoring files",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-551",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "NETWORK CONFIGURATION OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-556",
        "distinguishedname": "CN=Network Configuration Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members in this group can have some administrative privileges to manage configuration of networking features",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-556",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "PERFORMANCE MONITOR USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-558",
        "distinguishedname": "CN=Performance Monitor Users,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can access performance counter data locally and remotely",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-558",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "REPLICATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-552",
        "distinguishedname": "CN=Replicator,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Supports file replication in a domain",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-552",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DISTRIBUTED COM USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-562",
        "distinguishedname": "CN=Distributed COM Users,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members are allowed to launch, activate and use Distributed COM objects on this machine.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-562",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "PERFORMANCE LOG USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-559",
        "distinguishedname": "CN=Performance Log Users,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-559",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "CRYPTOGRAPHIC OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-569",
        "distinguishedname": "CN=Cryptographic Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members are authorized to perform cryptographic operations.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-569",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "EVENT LOG READERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-573",
        "distinguishedname": "CN=Event Log Readers,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can read event logs from local machine",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-573",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "GUESTS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-546",
        "distinguishedname": "CN=Guests,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-514",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-501",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-546",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "SYSTEM MANAGED ACCOUNTS GROUP@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "S-1-5-32-581",
        "distinguishedname": "CN=System Managed Accounts Group,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group are managed by the system.",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-503",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "S-1-5-32-581",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-545",
        "distinguishedname": "CN=Users,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Users are prevented from making accidental or intentional system-wide changes and can run most applications",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-513",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-11",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-4",
          "MemberType": "Group"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-545",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "CERTIFICATE SERVICE DCOM ACCESS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-574",
        "distinguishedname": "CN=Certificate Service DCOM Access,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group are allowed to connect to Certification Authorities in the enterprise",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-574",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "RDS REMOTE ACCESS SERVERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-575",
        "distinguishedname": "CN=RDS Remote Access Servers,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Servers in this group enable users of RemoteApp programs and personal virtual desktops access to these resources. In Internet-facing deployments, these servers are typically deployed in an edge network. This group needs to be populated on servers running RD Connection Broker. RD Gateway servers and RD Web Access servers used in the deployment need to be in this group.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-575",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "RDS ENDPOINT SERVERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-576",
        "distinguishedname": "CN=RDS Endpoint Servers,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Servers in this group run virtual machines and host sessions where users RemoteApp programs and personal virtual desktops run. This group needs to be populated on servers running RD Connection Broker. RD Session Host servers and RD Virtualization Host servers used in the deployment need to be in this group.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-576",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "RDS MANAGEMENT SERVERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-577",
        "distinguishedname": "CN=RDS Management Servers,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Servers in this group can perform routine administrative actions on servers running Remote Desktop Services. This group needs to be populated on all servers in a Remote Desktop Services deployment. The servers running the RDS Central Management service must be included in this group.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-577",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "HYPER-V ADMINISTRATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-578",
        "distinguishedname": "CN=Hyper-V Administrators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group have complete and unrestricted access to all features of Hyper-V.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-578",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "ACCESS CONTROL ASSISTANCE OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-579",
        "distinguishedname": "CN=Access Control Assistance Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can remotely query authorization attributes and permissions for resources on this computer.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-579",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "REMOTE MANAGEMENT USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-580",
        "distinguishedname": "CN=Remote Management Users,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces that grant access to the user.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-580",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "CERT PUBLISHERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-517",
        "distinguishedname": "CN=Cert Publishers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group are permitted to publish certificates to the directory",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-517",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "SERVER OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-549",
        "distinguishedname": "CN=Server Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members can administer domain servers",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-549",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "ACCOUNT OPERATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
        "distinguishedname": "CN=Account Operators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members can administer domain user and group accounts",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "PRE-WINDOWS 2000 COMPATIBLE ACCESS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-554",
        "distinguishedname": "CN=Pre-Windows 2000 Compatible Access,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "A backward compatibility group which allows read access on all users and groups in the domain",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-11",
          "MemberType": "Group"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-554",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "WINDOWS AUTHORIZATION ACCESS GROUP@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-560",
        "distinguishedname": "CN=Windows Authorization Access Group,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group have access to the computed tokenGroupsGlobalAndUniversal attribute on User objects",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-9",
          "MemberType": "Group"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-560",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DENIED RODC PASSWORD REPLICATION GROUP@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-572",
        "distinguishedname": "CN=Denied RODC Password Replication Group,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members in this group cannot have their passwords replicated to any read-only domain controllers in the domain",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-521",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-520",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-512",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-517",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-519",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-518",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-516",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-502",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-572",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "SCHEMA ADMINS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-518",
        "distinguishedname": "CN=Schema Admins,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Designated administrators of the schema",
        "admincount": True
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-500",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-518",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "ENTERPRISE ADMINS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-519",
        "distinguishedname": "CN=Enterprise Admins,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Designated administrators of the enterprise",
        "admincount": True
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-500",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-519",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "DOMAIN ADMINS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-512",
        "distinguishedname": "CN=Domain Admins,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Designated administrators of the domain",
        "admincount": True
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-500",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-512",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "RAS AND IAS SERVERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-553",
        "distinguishedname": "CN=RAS and IAS Servers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Servers in this group can access remote access properties of users",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-553",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "INCOMING FOREST TRUST BUILDERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-557",
        "distinguishedname": "CN=Incoming Forest Trust Builders,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can create incoming, one-way trusts to this forest",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-557",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "TERMINAL SERVER LICENSE SERVERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-561",
        "distinguishedname": "CN=Terminal Server License Servers,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can update user accounts in Active Directory with information about license issuance, for the purpose of tracking and reporting TS Per User CAL usage",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-561",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "ALLOWED RODC PASSWORD REPLICATION GROUP@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-571",
        "distinguishedname": "CN=Allowed RODC Password Replication Group,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members in this group can have their passwords replicated to all read-only domain controllers in the domain",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-571",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DNSADMINS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-1101",
        "distinguishedname": "CN=DnsAdmins,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "DNS Administrators Group",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-1101",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "DOMAIN CONTROLLERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-516",
        "distinguishedname": "CN=Domain Controllers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "All domain controllers in the domain",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-516",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DOMAIN COMPUTERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-515",
        "distinguishedname": "CN=Domain Computers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "All workstations and servers joined to the domain",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-515",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DOMAIN USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-513",
        "distinguishedname": "CN=Domain Users,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "All domain users",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-503",
          "MemberType": "User"
        },
        {
          "MemberId": "DOMAIN_SID-500",
          "MemberType": "User"
        },
        {
          "MemberId": "DOMAIN_SID-502",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-513",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": True,
        "name": "GROUP POLICY CREATOR OWNERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-520",
        "distinguishedname": "CN=Group Policy Creator Owners,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members in this group can modify group policy for the domain",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-500",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-520",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DOMAIN GUESTS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-514",
        "distinguishedname": "CN=Domain Guests,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "All domain guests",
        "admincount": False
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-501",
          "MemberType": "User"
        }
      ],
      "ObjectIdentifier": "DOMAIN_SID-514",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "READ-ONLY DOMAIN CONTROLLERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-521",
        "distinguishedname": "CN=Read-only Domain Controllers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group are Read-Only Domain Controllers in the domain",
        "admincount": True
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-521",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": False
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "ENTERPRISE READ-ONLY DOMAIN CONTROLLERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-498",
        "distinguishedname": "CN=Enterprise Read-only Domain Controllers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group are Read-Only Domain Controllers in the enterprise",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-498",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "CLONEABLE DOMAIN CONTROLLERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-522",
        "distinguishedname": "CN=Cloneable Domain Controllers,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group that are domain controllers may be cloned.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-522",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "PROTECTED USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-525",
        "distinguishedname": "CN=Protected Users,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group are afforded additional protections against authentication security threats. See http://go.microsoft.com/fwlink/?LinkId=298939 for more information.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-525",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "KEY ADMINS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-526",
        "distinguishedname": "CN=Key Admins,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can perform administrative actions on key objects within the domain.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-526",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "ENTERPRISE KEY ADMINS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-527",
        "distinguishedname": "CN=Enterprise Key Admins,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group can perform administrative actions on key objects within the forest.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-527",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "DNSUPDATEPROXY@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-1102",
        "distinguishedname": "CN=DnsUpdateProxy,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "DNS clients who are permitted to perform dynamic updates on behalf of some other clients (such as DHCP servers).",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_SID-1102",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "highvalue": False,
        "name": "STORAGE REPLICA ADMINISTRATORS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "S-1-5-32-582",
        "distinguishedname": "CN=Storage Replica Administrators,CN=Builtin,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Members of this group have complete and unrestricted access to all features of Storage Replica.",
        "admincount": False
      },
      "Members": [],
      "ObjectIdentifier": "S-1-5-32-582",
      "Aces": [
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "Owner",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-548",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-512",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": False
        },
        {
          "PrincipalSID": "DOMAIN_SID-519",
          "PrincipalType": "Group",
          "RightName": "GenericAll",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteDacl",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "WriteOwner",
          "AceType": "",
          "IsInherited": True
        },
        {
          "PrincipalSID": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-544",
          "PrincipalType": "Group",
          "RightName": "GenericWrite",
          "AceType": "",
          "IsInherited": True
        }
      ]
    },
    {
      "Properties": {
        "name": "ENTERPRISE DOMAIN CONTROLLERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX"
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-1000",
          "MemberType": "Computer"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-9",
      "Aces": []
    },
    {
      "Properties": {
        "name": "EVERYONE@DOMAIN_NAME.DOMAIN_SUFFIX"
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-515",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-513",
          "MemberType": "Group"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-1-0",
      "Aces": []
    },
    {
      "Properties": {
        "name": "AUTHENTICATED USERS@DOMAIN_NAME.DOMAIN_SUFFIX"
      },
      "Members": [
        {
          "MemberId": "DOMAIN_SID-515",
          "MemberType": "Group"
        },
        {
          "MemberId": "DOMAIN_SID-513",
          "MemberType": "Group"
        }
      ],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-11",
      "Aces": []
    },
    {
      "Properties": {
        "name": "USERS@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX"
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-32-545",
      "Aces": []
    },
    {
      "Properties": {
        "name": "THIS ORGANIZATION@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX"
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-17",
      "Aces": []
    },
    {
      "Properties": {
        "name": "INTERACTIVE@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX"
      },
      "Members": [],
      "ObjectIdentifier": "DOMAIN_NAME.DOMAIN_SUFFIX-S-1-5-4",
      "Aces": []
    }
  ]


def get_departments_list(prob):
  sum = 0
  for key in prob.keys():
      sum += prob[key]
  if sum != 100:
    return DEPARTMENTS_LIST
  try:
    return ["IT"] * prob["IT"] + ["HR"] * prob["HR"] + ["MARKETING"] * prob["MARKETING"] +\
    ["OPERATIONS"] * prob["OPERATIONS"] + ["BIDNESS"] * prob["BIDNESS"]
  except:
    return DEPARTMENTS_LIST
 
