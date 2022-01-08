import random
from adsimulator.templates.domains import get_functional_level_list, TLD_LIST
from adsimulator.templates.default_values import get_complementary_value
from adsimulator.utils.boolean import generate_boolean_value
from adsimulator.utils.parameters import get_dict_param_value, get_perc_param_value, print_domain_generation_parameters
from adsimulator.utils.domains import generate_trust_sid


def generate_domain(session, domain_name, domain_sid, domain_dn, parameters):
    prob = get_dict_param_value("Domain", "functionalLevelProbability", parameters)
    functional_level = random.choice(get_functional_level_list(prob))
    print_domain_generation_parameters(prob)
    session.run(
        """
        MERGE (n:Base {name:$domain}) SET n:Domain, n.highvalue=true, n.objectid=$objectid,
        n.distinguishedname=$dn, n.functionallevel=$fl
        """,
        domain=domain_name,
        objectid=domain_sid,
        dn=domain_dn,
        fl=functional_level
    )
    return functional_level


def generate_trusts(session, domain_name, domain_names, parameters):
    available_names = domain_names
    current_domain_name = str(domain_name).split(".")[0]
    if current_domain_name in available_names:
        available_names.remove(current_domain_name)
    sid_filtering_perc = get_perc_param_value("Domain", "Trusts", parameters)["SIDFilteringProbability"]
    n_trust = get_dict_param_value("Domain", "Trusts", parameters)
    if len(available_names) < n_trust["Inbound"]:
        n_trust["Inbound"] = len(available_names)
    print("Generating", str(n_trust["Inbound"]), "inbound domain trusts (sidfiltering probability:", sid_filtering_perc, "%)")
    for i in range(0, n_trust["Inbound"]):
        available_names = generate_inbound_trust(session, domain_name, available_names, sid_filtering_perc)
    if len(available_names) < n_trust["Outbound"]:
        n_trust["Outbound"] = len(available_names)
    print("Generating", str(n_trust["Outbound"]), "outbound domain trusts (sidfiltering probability:", sid_filtering_perc, "%)")
    for i in range(0, n_trust["Outbound"]):
        available_names = generate_outbound_trust(session, domain_name, available_names, sid_filtering_perc)
    if len(available_names) < n_trust["Bidirectional"]:
        n_trust["Bidirectional"] = len(available_names)
    print("Generating", str(n_trust["Bidirectional"]), "bidirectional domain trusts (sidfiltering probability:", sid_filtering_perc, "%)")
    for i in range(0, n_trust["Bidirectional"]):
        available_names = generate_bidirectional_trust(session, domain_name, available_names, sid_filtering_perc)


def generate_inbound_trust(session, domain_name, available_names, sid_filtering_perc):
    sid_filtering = generate_boolean_value(sid_filtering_perc, get_complementary_value(sid_filtering_perc))
    name = random.choice(available_names)
    available_names.remove(name)
    trust_name = name + random.choice(TLD_LIST)
    trust_sid = generate_trust_sid()
    session.run(
        """
        MERGE (n:Domain {name:$domainname})
        WITH n
        MERGE (m: Domain {name:$trustname, objectid:$trustsid})
        WITH n,m
        MERGE (n)-[:TrustedBy {isacl:false, sidfiltering: $sidfiltering, transitive: 'false', trusttype: 'Forest'}]->(m)
        """,
        trustname=trust_name,
        trustsid=trust_sid,
        domainname=domain_name,
        sidfiltering=sid_filtering
    )
    return available_names


def generate_outbound_trust(session, domain_name, available_names, sid_filtering_perc):
    sid_filtering = generate_boolean_value(sid_filtering_perc, get_complementary_value(sid_filtering_perc))
    name = random.choice(available_names)
    available_names.remove(name)
    trust_name = name + random.choice(TLD_LIST)
    trust_sid = generate_trust_sid()
    session.run(
        """
        MERGE (n:Domain {name:$domainname})
        WITH n
        MERGE (m: Domain {name:$trustname, objectid:$trustsid})
        WITH n,m
        MERGE (m)-[:TrustedBy {isacl:false, sidfiltering: $sidfiltering, transitive: 'false', trusttype: 'Forest'}]->(n)
        """,
        trustname=trust_name,
        trustsid=trust_sid,
        domainname=domain_name,
        sidfiltering=sid_filtering
    )
    return available_names


def generate_bidirectional_trust(session, domain_name, available_names, sid_filtering_perc):
    sid_filtering = generate_boolean_value(sid_filtering_perc, get_complementary_value(sid_filtering_perc))
    name = random.choice(available_names)
    available_names.remove(name)
    trust_name = name + "." + domain_name
    trust_sid = generate_trust_sid()
    session.run(
        """
        MERGE (n:Domain {name:$domainname})
        WITH n
        MERGE (m: Domain {name:$trustname, objectid:$trustsid})
        WITH n,m
        MERGE (n)-[:TrustedBy {isacl:false, sidfiltering: $sidfiltering, transitive: 'true', trusttype: 'ParentChild'}]->(m)
        MERGE (m)-[:TrustedBy {isacl:false, sidfiltering: $sidfiltering, transitive: 'true', trusttype: 'ParentChild'}]->(n)
        """,
        trustname=trust_name,
        trustsid=trust_sid,
        domainname=domain_name,
        sidfiltering=sid_filtering
    )
    return available_names
