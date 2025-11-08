#!/usr/bin/env python3

# OIDs used:
# THALES-PAYSHIELD-MIB::payShieldLmkNumLoaded.0 				    .1.3.6.1.4.1.4096.2.2.10000.3.1.0
# THALES-PAYSHIELD-MIB::payShieldLmkNumTestLmksLoaded.0 			.1.3.6.1.4.1.4096.2.2.10000.3.2.0
# THALES-PAYSHIELD-MIB::payShieldLmkNumOldLmksLoaded.0 			.1.3.6.1.4.1.4096.2.2.10000.3.3.0
# THALES-PAYSHIELD-MIB::payShieldLmkStatusLoaded.x 				.1.3.6.1.4.1.4096.2.2.10000.3.4.1.2.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusAuth.x				    .1.3.6.1.4.1.4096.2.2.10000.3.4.1.3.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusNumAuthActivities.x 	.1.3.6.1.4.1.4096.2.2.10000.3.4.1.4.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusScheme.x				.1.3.6.1.4.1.4096.2.2.10000.3.4.1.5.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusAlgorithm.x				.1.3.6.1.4.1.4096.2.2.10000.3.4.1.6.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusLiveTest.x				.1.3.6.1.4.1.4096.2.2.10000.3.4.1.7.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusComments.x				.1.3.6.1.4.1.4096.2.2.10000.3.4.1.8.1
# THALES-PAYSHIELD-MIB::payShieldLmkStatusCheckDigits.x			.1.3.6.1.4.1.4096.2.2.10000.3.4.1.9.1
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_lmk.py

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

def parse_payshield_lmk(string_table):
    parsed = {}
    lmkcount_column_names = [
        "payShieldLmkNumLoaded",
        "payShieldLmkNumTestLmksLoaded",
        "payShieldLmkNumOldLmksLoaded",
    ]

    #parse the overall lmk values from line 1
    lmkcounts = string_table[0]
    for n in range(0, len(lmkcount_column_names)):
        parsed[lmkcount_column_names[n]] = lmkcounts[n]

    #parse the detailed lmk values which follow on line 2 to the end
    parsed["lmks"] = []
    lmkinfo_table = string_table[1:]
    lmkinfo_column_names = [
        "payShieldLmkStatusLoaded",
        "payShieldLmkStatusAuth",
        "payShieldLmkStatusNumAuthActivities",
        "payShieldLmkStatusScheme", 
        "payShieldLmkStatusAlgorithm",
        "ps10000LmkStatusLiveTest",
        "payShieldLmkStatusComments",
        "payShieldLmkStatusCheckDigits"
    ]
    for index,lmkinfo in enumerate(lmkinfo_table):
        parsedlmk = {}
        if int(lmkinfo[3]) == 1:
            for n in range(0, len(lmkinfo_column_names)):
                parsedlmk[lmkinfo_column_names[n]] = lmkinfo[n+3]
            parsed["lmks"].append(parsedlmk)
    return parsed

def discover_payshield_lmk(section):
    yield Service(item="LMK Num Loaded")
    yield Service(item="LMK Num Test Loaded")
    yield Service(item="LMK Num Old Loaded")

    for index,lmk in enumerate(section["lmks"]):
        if lmk["payShieldLmkStatusLoaded"] == '1': 
            yield Service(item=f"LMK Info {index}")


def check_payshield_lmk(item, section):
    if 'LMK Num Loaded' in item:
        yield Result(state=State.OK, summary=f"Currently there are {section["payShieldLmkNumLoaded"]} LMK loaded")

    elif 'LMK Num Test Loaded' in item:
        yield Result(state=State.OK, summary=f"Currently there are {section["payShieldLmkNumTestLmksLoaded"]} TEST LMK loaded")

    elif 'LMK Num Old Loaded' in item:
        yield Result(state=State.OK, summary=f"Currently there are {section["payShieldLmkNumOldLmksLoaded"]} OLD LMK loaded")

    for index,lmk in enumerate(section["lmks"]):      
        if f"LMK Info {index}" in item:
            scheme = {"1" : "Unknown", "2" : "Variant", "3" : "Keyblock", "4": "Aes"}
            algorithm = {"1" : "Unknown", "2": "3Des2Key", "3": "3Des3Key", "4": "Aes256"}
            livetest = { "1" : "lmkStatusUnknown", "2" : "Live", "3": "Test" }
            yield Result(
                state=State.OK, 
                summary=f"LMK {index} {lmk["payShieldLmkStatusComments"]} {lmk["payShieldLmkStatusCheckDigits"]}", 
                details=f"loaded {lmk["payShieldLmkStatusLoaded"]}\n"+
                f"Auth {lmk["payShieldLmkStatusAuth"]}\n"+
                f"NumAuthActivities: {lmk["payShieldLmkStatusNumAuthActivities"]}\n"+
                f"Scheme: \"{scheme[lmk["payShieldLmkStatusScheme"]]}\"\n"+
                f"Algorithm: \"{algorithm[lmk["payShieldLmkStatusAlgorithm"]]}\"\n"+
                f"LiveTest: \"{livetest[lmk["ps10000LmkStatusLiveTest"]]}\"\n"+
                f"Comment: \"{lmk["payShieldLmkStatusComments"]}\"\n"+
                f"Checkvalue: \"{lmk["payShieldLmkStatusCheckDigits"]}\"" 
            )

snmp_section_payshield_lmk_setup = SimpleSNMPSection(
    name = "payshield10k_lmk",
    parse_function = parse_payshield_lmk,

    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "3.1.0",   # payShieldLmkNumLoaded.0
            "3.2.0",   # payShieldLmkNumTestLmksLoaded.0
            "3.3.0",   # payShieldLmkNumOldLmksLoaded.0
            "3.4.1.2", # payShieldLmkStatusLoaded.x
            "3.4.1.3", # payShieldLmkStatusAuth.x
            "3.4.1.4", # payShieldLmkStatusNumAuthActivities.x
            "3.4.1.5", # payShieldLmkStatusScheme.x
            "3.4.1.6", # payShieldLmkStatusAlgorithm.x
            "3.4.1.7", # ps10000LmkStatusLiveTest.x
            "3.4.1.8", # payShieldLmkStatusComments.x
            "3.4.1.9"  # payShieldLmkStatusCheckDigits.x
        ],
    ),
)

check_plugin_payshield_lmk = CheckPlugin(
    name = "payshield10k_lmk",
    sections = [ "payshield10k_lmk" ],
    service_name = "Payshield %s",
    discovery_function = discover_payshield_lmk,
    check_function = check_payshield_lmk,
)
