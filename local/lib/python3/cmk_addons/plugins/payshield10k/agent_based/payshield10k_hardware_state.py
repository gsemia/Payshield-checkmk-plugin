#!/usr/bin/env python3

# OIDs used:
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateFanSerialNum.1			.1.3.6.1.4.1.4096.2.2.10000.2.3.1.1.2.1 = STRING: "xxxx"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateFanSerialNum.2			.1.3.6.1.4.1.4096.2.2.10000.2.3.1.1.2.2 = STRING: "xxxx"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateFanState.1			    .1.3.6.1.4.1.4096.2.2.10000.2.3.1.1.3.1 = INTEGER: 1
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateFanState.2			    .1.3.6.1.4.1.4096.2.2.10000.2.3.1.1.3.2 = INTEGER: 1
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStatePSUSerialNum.1			.1.3.6.1.4.1.4096.2.2.10000.2.4.1.1.2.1 = STRING: "yyyy"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStatePSUSerialNum.2			.1.3.6.1.4.1.4096.2.2.10000.2.4.1.1.2.2 = STRING: "yyyy"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStatePSUState.1			    .1.3.6.1.4.1.4096.2.2.10000.2.4.1.1.3.1 = INTEGER: 1
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStatePSUState.2			    .1.3.6.1.4.1.4096.2.2.10000.2.4.1.1.3.2 = INTEGER: 1
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldStateBattery.0			    .1.3.6.1.4.1.4096.2.2.10000.2.5.0 = INTEGER: 1
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_hardware_state.py

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

def parse_payshield_hardware_state(string_table):
    parsed = {}
    column_names = [
        "payShieldStateFan1SerialNum",
        "payShieldStateFan2SerialNum",
        "payShieldStateFan1State",
        "payShieldStateFan2State",
        "payShieldStatePSU1SerialNum",
        "payShieldStatePSU2SerialNum",
        "payShieldStatePSU1State", 
        "payShieldStatePSU2State",
        "payShieldStateBattery"
    ]
    for line in string_table:
        for n in range(0, len(column_names)):
            parsed[column_names[n]] = line[n]
    return parsed

def discover_payshield_hardware_state(section):
    yield Service(item="Fan 1")
    yield Service(item="Fan 2")
    yield Service(item="PSU 1")
    yield Service(item="PSU 2")
    yield Service(item="Battery")

def check_payshield_hardware_state(item, section):
    if 'Fan 1' in item:
        if section["payShieldStateFan1State"] == "1":
            yield Result(state=State.OK, summary=f"OK - Fan 1 with Serial {section["payShieldStateFan1SerialNum"]} is OK: State {section["payShieldStateFan1State"]}")
        else:
            yield Result(state=State.CRIT, summary=f"CRIT - Fan 1 with Serial {section["payShieldStateFan1SerialNum"]} is Critical: State {section["payShieldStateFan1State"]}")

    elif 'Fan 2' in item:
        if section["payShieldStateFan2State"] == "1":
            yield Result(state=State.OK, summary=f"OK - Fan 2 with Serial {section["payShieldStateFan2SerialNum"]} is OK: State {section["payShieldStateFan2State"]}")
        else:
            yield Result(state=State.CRIT, summary=f"CRIT - Fan 2 with Serial {section["payShieldStateFan2SerialNum"]} is Critical: State {section["payShieldStateFan2State"]}")

    elif 'PSU 1' in item:
        if section["payShieldStatePSU1State"] == "1":
            yield Result(state=State.OK, summary=f"OK - PSU 1 with Serial {section["payShieldStatePSU1SerialNum"]} is OK: State {section["payShieldStatePSU1State"]}")
        else:
            yield Result(state=State.CRIT, summary=f"CRIT - PSU 1 with Serial {section["payShieldStatePSU1SerialNum"]} is Critical: State {section["payShieldStatePSU1State"]}")

    elif 'PSU 2' in item:
        if section["payShieldStatePSU2State"] == "1":
            yield Result(state=State.OK, summary=f"OK - PSU 2 with Serial {section["payShieldStatePSU2SerialNum"]} is OK: State {section["payShieldStatePSU2State"]}")
        else:
            yield Result(state=State.CRIT, summary=f"CRIT - PSU 2 with Serial {section["payShieldStatePSU2SerialNum"]} is Critical: State {section["payShieldStatePSU2State"]}")
            
    elif 'Battery' in item:
        if section["payShieldStateBattery"] == "1":
            yield Result(state=State.OK, summary=f"OK - Battery is OK: State {section["payShieldStateBattery"]}" )
        else:
            yield Result(state=State.CRIT, summary=f"CRIT - Battery Critical: State {section["payShieldStateBattery"]}")


snmp_section_payshield_hardware_state_setup = SimpleSNMPSection(
    name = "payshield10k_hardware_state",
    parse_function = parse_payshield_hardware_state,

    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "2.3.1.1.2.1", #payShieldStateFanSerialNum.1
            "2.3.1.1.2.2", #payShieldStateFanSerialNum.2
            "2.3.1.1.3.1", #payShieldStateFanState.1
            "2.3.1.1.3.2", #payShieldStateFanState.2
            "2.4.1.1.2.1", #payShieldStatePSUSerialNum.1
            "2.4.1.1.2.2", #payShieldStatePSUSerialNum.2
            "2.4.1.1.3.1", #payShieldStatePSUState.1
            "2.4.1.1.3.2", #payShieldStatePSUState.2
            "2.5.0",       #payShieldStateBattery.0
        ],
    ),
)

check_plugin_payshield_hardware_state = CheckPlugin(
    name = "payshield10k_hardware_state",
    sections = [ "payshield10k_hardware_state" ],
    service_name = "Payshield HW %s State",
    discovery_function = discover_payshield_hardware_state,
    check_function = check_payshield_hardware_state,
)
