GUEST_USER = {
      "Properties": {
        "highvalue": False,
        "name": "GUEST@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-501",
        "distinguishedname": "CN=Guest,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Built-in account for guest access to the computer/domain",
        "dontreqpreauth": False,
        "passwordnotreqd": True,
        "unconstraineddelegation": False,
        "sensitive": False,
        "enabled": False,
        "pwdneverexpires": True,
        "lastlogon": -1,
        "lastlogontimestamp": -1,
        "pwdlastset": -1,
        "serviceprincipalnames": [],
        "hasspn": False,
        "displayname": "null",
        "email": "null",
        "title": "null",
        "homedirectory": "null",
        "userpassword": "null",
        "admincount": False,
        "sidhistory": []
      },
      "AllowedToDelegate": [],
      "SPNTargets": [],
      "PrimaryGroupSid": "DOMAIN_SID-514",
      "HasSIDHistory": [],
      "ObjectIdentifier": "DOMAIN_SID-501",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
    }


DEFAULT_ACCOUNT = {
      "Properties": {
        "highvalue": False,
        "name": "DEFAULTACCOUNT@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-503",
        "distinguishedname": "CN=DefaultAccount,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "A user account managed by the system.",
        "dontreqpreauth": False,
        "passwordnotreqd": True,
        "unconstraineddelegation": False,
        "sensitive": False,
        "enabled": False,
        "pwdneverexpires": True,
        "lastlogon": -1,
        "lastlogontimestamp": -1,
        "pwdlastset": -1,
        "serviceprincipalnames": [],
        "hasspn": False,
        "displayname": "null",
        "email": "null",
        "title": "null",
        "homedirectory": "null",
        "userpassword": "null",
        "admincount": False,
        "sidhistory": []
      },
      "AllowedToDelegate": [],
      "SPNTargets": [],
      "PrimaryGroupSid": "DOMAIN_SID-513",
      "HasSIDHistory": [],
      "ObjectIdentifier": "DOMAIN_SID-503",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
    }


ADMINISTRATOR = {
      "Properties": {
        "highvalue": False,
        "name": "ADMINISTRATOR@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-500",
        "distinguishedname": "CN=Administrator,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Built-in account for administering the computer/domain",
        "dontreqpreauth": False,
        "passwordnotreqd": False,
        "unconstraineddelegation": False,
        "sensitive": False,
        "enabled": True,
        "pwdneverexpires": True,
        "lastlogon": 1601019126,
        "lastlogontimestamp": 1600849229,
        "pwdlastset": 1588772520,
        "serviceprincipalnames": [],
        "hasspn": False,
        "displayname": "null",
        "email": "null",
        "title": "null",
        "homedirectory": "null",
        "userpassword": "null",
        "admincount": True,
        "sidhistory": []
      },
      "AllowedToDelegate": [],
      "SPNTargets": [],
      "PrimaryGroupSid": "DOMAIN_SID-513",
      "HasSIDHistory": [],
      "ObjectIdentifier": "DOMAIN_SID-500",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
    }


KRBTGT = {
      "Properties": {
        "highvalue": False,
        "name": "KRBTGT@DOMAIN_NAME.DOMAIN_SUFFIX",
        "domain": "DOMAIN_NAME.DOMAIN_SUFFIX",
        "objectid": "DOMAIN_SID-502",
        "distinguishedname": "CN=krbtgt,CN=Users,DC=DOMAIN_NAME,DC=DOMAIN_SUFFIX",
        "description": "Key Distribution Center Service Account",
        "dontreqpreauth": False,
        "passwordnotreqd": False,
        "unconstraineddelegation": False,
        "sensitive": False,
        "enabled": False,
        "pwdneverexpires": False,
        "lastlogon": -1,
        "lastlogontimestamp": -1,
        "pwdlastset": 1584136849,
        "serviceprincipalnames": [
          "kadmin/changepw"
        ],
        "hasspn": True,
        "displayname": "null",
        "email": "null",
        "title": "null",
        "homedirectory": "null",
        "userpassword": "null",
        "admincount": True,
        "sidhistory": []
      },
      "AllowedToDelegate": [],
      "SPNTargets": [],
      "PrimaryGroupSid": "DOMAIN_SID-513",
      "HasSIDHistory": [],
      "ObjectIdentifier": "DOMAIN_SID-502",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
          "RightName": "ExtendedRight",
          "AceType": "All",
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
    }
