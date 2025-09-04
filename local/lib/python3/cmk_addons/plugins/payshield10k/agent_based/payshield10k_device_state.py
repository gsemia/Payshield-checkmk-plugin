#!/usr/bin/env python3

# OIDs used:
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateDevice.0        .1.3.6.1.4.1.4096.2.2.10000.2.1.0
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_device_state.py



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

def parse_payshield_state(string_table):
    result = {}
    result["payShieldStateDevice"] = string_table[0][0]
    return result

def discover_payshield_state(section):
    yield Service()

def check_payshield_state(section):
    if section["payShieldStateDevice"] == "0":
        yield Result(state=State.WARN, summary=f"Payshield Device State - Secure (two Keys are turned)")
    elif section["payShieldStateDevice"] == "1":
        yield Result(state=State.WARN, summary=f"Payshield Device State - Offline (One Key is turned)")
    elif section["payShieldStateDevice"] == "2":
        yield Result(state=State.OK, summary=f"Payshield Device State -  Online (USB Serial console offline - No Key is turned)")
    elif section["payShieldStateDevice"] == "4":
        yield Result(state=State.OK, summary=f"Payshield Device State -  Online (USB Serial Console connected - No Key is turned)")
    else:
        yield Result(state=State.UNKNOWN, summary=f"cannot determine Payshield Device State - UNKNOWN value {section["payShieldStateDevice"]}")



snmp_section_payshield_device_state_setup = SimpleSNMPSection(
    name = "payshield10k_device_state",
    parse_function = parse_payshield_state,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "2.1.0",   #payShieldStateDevice.0
        ],
    ),
)

check_plugin_payshield_device_state = CheckPlugin(
    name = "payshield10k_device_state",
    sections = [ "payshield10k_device_state" ],
    service_name = "Payshield Device State",
    discovery_function = discover_payshield_state,
    check_function = check_payshield_state,
)
