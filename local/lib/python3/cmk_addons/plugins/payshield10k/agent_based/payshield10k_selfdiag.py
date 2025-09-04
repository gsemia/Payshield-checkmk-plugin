#!/usr/bin/env python3

# OIDs used:
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldHealthDiagSelfTestOK.0	.1.3.6.1.4.1.4096.2.2.10000.11.1.2.0
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldHealthDiagSelfTestList.0	.1.3.6.1.4.1.4096.2.2.10000.11.1.4.0
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_selfdiag.py

from cmk.agent_based.v2 import (
    CheckPlugin,
    CheckResult,
    startswith,
    DiscoveryResult,
    Result,
    Service,
    SimpleSNMPSection,
    SNMPTree,
    State,
    StringTable,
)

def parse_payshield_selfdiag(string_table):
    result = {}
    result["payShieldHealthDiagSelfTestOK"] = string_table[0][0]
    result["payShieldHealthDiagSelfTestList"] = string_table[0][1]
    return result

def discover_payshield_selfdiag(section):
    yield Service()

def check_payshield_selfdiag(section):
    if section["payShieldHealthDiagSelfTestOK"] == "1":
        yield Result(state=State.OK, summary=f"OK - Testresult: {section["payShieldHealthDiagSelfTestOK"]}", details = f"OK - Test List: {section["payShieldHealthDiagSelfTestList"]}")
    else:
        yield Result(state=State.CRIT, summary=f"CRIT - Testresult: {section["payShieldHealthDiagSelfTestOK"]}", details = f" CRITICAL - Test List: {section["payShieldHealthDiagSelfTestList"]}")


snmp_section_payshield_selfdiag_setup = SimpleSNMPSection(
    name = "payshield10k_selfdiag",
    parse_function = parse_payshield_selfdiag,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
                        "11.1.2",    # payShieldHealthDiagSelfTestOK.0
                        "11.1.4",    # payShieldHealthDiagSelfTestList.0
        ],
    ),
)

check_plugin_payshield_selfdiag = CheckPlugin(
    name = "payshield10k_selfdiag",
    sections = [ "payshield10k_selfdiag" ],
    service_name = "Payshield Self Diagnostic",
    discovery_function = discover_payshield_selfdiag,
    check_function = check_payshield_selfdiag,
)
