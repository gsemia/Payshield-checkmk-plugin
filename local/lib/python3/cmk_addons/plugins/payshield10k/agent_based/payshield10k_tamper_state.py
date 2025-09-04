#!/usr/bin/env python3

# OIDs used:
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateTamperState.0   .1.3.6.1.4.1.4096.2.2.10000.3.2.1.0
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateTamperDate.0    .1.3.6.1.4.1.4096.2.2.10000.3.2.2.0
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateTamperCause.0   .1.3.6.1.4.1.4096.2.2.10000.3.2.3.0
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_tamper_state.py

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

def parse_payshield_tamper_state(string_table):
    result = {}
    result["payShieldStateTamperState"] = string_table[0][0]
    result["payShieldStateTamperDate"] = string_table[0][1]
    result["payShieldStateTamperCause"] = string_table[0][2]
    return result

def discover_payshield_tamper_state(section):
    yield Service()

def check_payshield_tamper_state(section):
    if section["payShieldStateTamperState"] == "3":
        yield Result(state=State.CRIT, summary=f"Tamper detected: {section["payShieldStateTamperDate"]} {section["payShieldStateTamperCause"]}")
    elif section["payShieldStateTamperState"] == "1":
        yield Result(state=State.CRIT, summary=f"Tamper state reported as unknown: {section["payShieldStateTamperDate"]} {section["payShieldStateTamperCause"]}")
    elif section["payShieldStateTamperState"] == "2":
        yield Result(state=State.OK, summary=f"No Tamber detected: {section["payShieldStateTamperDate"]} {section["payShieldStateTamperCause"]}")
    else:
        yield Result(state=State.UNKNOWN, summary=f"cannot determine Payshield Tamper State - UNKNOWN value: {section["payShieldStateTamperState"]}")


snmp_section_payshield_tamper_state_setup = SimpleSNMPSection(
    name = "payshield10k_tamper_state",
    parse_function = parse_payshield_tamper_state,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "2.2.1.0", #payShieldStateTamperState.0
            "2.2.2.0", #payShieldStateTamperDate.0
            "2.2.3.0"  #payShieldStateTamperCause.0
        ],
    ),
)

check_plugin_payshield_tamper_state = CheckPlugin(
    name = "payshield10k_tamper_state",
    sections = [ "payshield10k_tamper_state" ],
    service_name = "Payshield Tamper State check",
    discovery_function = discover_payshield_tamper_state,
    check_function = check_payshield_tamper_state,
)
