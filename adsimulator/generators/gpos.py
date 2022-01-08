import random
import uuid
from adsimulator.utils.principals import get_name
from adsimulator.utils.gpos import get_gpo_dn, get_gpc_path
from adsimulator.utils.parameters import get_perc_param_value
from adsimulator.utils.boolean import generate_boolean_value
from adsimulator.templates.default_values import get_complementary_value


def generate_default_gpos(session, domain_name, domain_dn, ddp, ddcp):
    base_statement = "MERGE (n:Base {name:$gpo, objectid:$guid, highvalue:false, distinguishedname:$dn, gpcpath:$gpc}) SET n:GPO"
    cn = "{" + str(uuid.uuid4()).upper() + "}"
    session.run(
        base_statement,
        gpo=get_name("DEFAULT DOMAIN POLICY", domain_name),
        guid=ddp,
        dn=get_gpo_dn(cn, domain_dn),
        gpc=get_gpc_path(cn, domain_name),
        exploitable=False
    )
    cn = "{" + str(uuid.uuid4()).upper() + "}"
    session.run(
        base_statement,
        gpo=get_name("DEFAULT DOMAIN CONTROLLERS POLICY", domain_name),
        guid=ddcp,
        dn=get_gpo_dn(cn, domain_dn),
        gpc=get_gpc_path(cn, domain_name),
        exploitable=False
    )


def link_default_gpos(session, domain_name, ddp, ddcp, dcou):
    gpo_name = "DEFAULT DOMAIN POLICY@{}".format(domain_name)
    session.run('MERGE (n:GPO {name:$gpo}) MERGE (m:Domain {name:$domain}) MERGE (n)-[:GpLink {isacl:false, enforced:toBoolean(false)}]->(m)', gpo=gpo_name, domain=domain_name)
    session.run('MERGE (n:Domain {name:$domain}) MERGE (m:OU {objectid:$guid}) MERGE (n)-[:Contains {isacl:false}]->(m)', domain=domain_name, guid=dcou)
    gpo_name = "DEFAULT DOMAIN CONTROLLERS POLICY@{}".format(domain_name)
    session.run('MERGE (n:GPO {objectid:$gpoguid}) MERGE (m:OU {objectid:$ouguid}) MERGE (n)-[:GpLink {isacl:false, enforced:toBoolean(false)}]->(m)', gpoguid=ddcp, ouguid=dcou)


def generate_gpos(session, domain_name, domain_dn, gpos, gpos_properties_list, num_gpos, parameters):
    for i in range(1, num_gpos + 1):
        gpo_name = "GPO_{}@{}".format(i, domain_name)
        guid = str(uuid.uuid4()).upper()
        cn = "{" + str(uuid.uuid4()).upper() + "}"
        gpo_dn = get_gpo_dn(cn, domain_dn)
        gpo_gpc_path = get_gpc_path(cn, domain_name)

        # New params
        exploitable_perc = get_perc_param_value("GPO", "exploitable", parameters)
        exploitable = generate_boolean_value(exploitable_perc, get_complementary_value(exploitable_perc))

        gpo_properties = {
            'id': guid,
            'name': gpo_name,
            'exploitable': exploitable
        }
        session.run(
            """
            MERGE (n:Base {name:$gponame})
            SET n:GPO, n.objectid=$guid, n.highvalue=false, n.distinguishedname=$dn,
            n.gpcpath=$gpc, n.exploitable=$exploitable
            """,
            gponame=gpo_name,
            guid=guid,
            dn=gpo_dn,
            gpc=gpo_gpc_path,
            exploitable=exploitable
        )
        gpos.append(gpo_name)
        gpos_properties_list.append(gpo_properties)
    return gpos, gpos_properties_list


def link_gpos_to_ous(session, gpos, ou_names, ou_guid_map):
    for g in gpos:
        num_links = random.randint(1, 3)
        linked_ous = random.sample(ou_names, num_links)
        for l in linked_ous:
            guid = ou_guid_map[l]
            session.run("MERGE (n:GPO {name:$gponame}) WITH n MERGE (m:OU {objectid:$guid}) WITH n,m MERGE (n)-[r:GpLink {isacl:false, enforced:toBoolean(false)}]->(m)", gponame=g, guid=guid)


def gplink_domain_to_ous(session, domain_name, ou_names, ou_guid_map):
    num_links = random.randint(1, 3)
    linked_ous = random.sample(ou_names, num_links)
    for l in linked_ous:
        guid = ou_guid_map[l]
        session.run("MERGE (n:Domain {name:$gponame}) WITH n MERGE (m:OU {objectid:$guid}) WITH n,m MERGE (n)-[r:GpLink {isacl:false, enforced:toBoolean(false)}]->(m)", gponame=domain_name, guid=guid)