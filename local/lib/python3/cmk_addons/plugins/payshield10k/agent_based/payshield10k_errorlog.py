#!/usr/bin/env python3

# OIDs used:
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLogsErrorlogTotalCount.0                     .1.3.6.1.4.1.4096.2.2.10000.10.1.1.0
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_errorlog.py

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

def parse_payshield_errorlog(string_table):
    result = {}
    result["payShieldLogsErrorlogTotalCount"] = string_table[0][0]
    return result

def discover_payshield_errorlog(section):
    yield Service()

def check_payshield_errorlog(section):
    if section["payShieldLogsErrorlogTotalCount"] >= "1":
        #TODO: change this state to WARN or CRIT if you want to be alerted for errors.
        yield Result(state=State.OK, summary=f"Errors found in errorlog: {section["payShieldLogsErrorlogTotalCount"]} errors")
    else:
        yield Result(state=State.OK, summary=f"No Errors found in errorlog: {section["payShieldLogsErrorlogTotalCount"]} errors")

snmp_section_payshield_errorlog_setup = SimpleSNMPSection(
    name = "payshield10k_errorlog",
    parse_function = parse_payshield_errorlog,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "10.1.1.0" # payShieldLogsErrorlogTotalCount.0
        ],
    ),
)

check_plugin_payshield_errorlog = CheckPlugin(
    name = "payshield10k_errorlog",
    sections = [ "payshield10k_errorlog" ],
    service_name = "Payshield Error Logs",
    discovery_function = discover_payshield_errorlog,
    check_function = check_payshield_errorlog,
)
