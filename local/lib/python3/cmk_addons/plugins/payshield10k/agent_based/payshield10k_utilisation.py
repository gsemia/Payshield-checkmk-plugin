#!/usr/bin/env python3

# OIDs used:
# THALES-PAYSHIELD-MIB::payShieldUtilLoad.0		    .1.3.6.1.4.1.4096.2.2.10000.1.1.0
# THALES-PAYSHIELD-MIB::payShieldUtilHostCmdVolume.0	.1.3.6.1.4.1.4096.2.2.10000.1.2.0 = STRING: "60,1\nM2,00002;"
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_utilisation.py

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
    check_levels,
)

commanddictionary = { 
"A0": "Generate Key", 
"A6": "Import a Key", 
"A8": "Export a Key", 
"B2": "Echo Command", 
"BS": "Erase the Key Change Storage",
"BU": "Generate Key Check Value",
"BW": "Translate Keys from Old LMK to New LMK and Migrate to New Key Type",
"CC": "Translate a PIN from One TPK to Another",
"CS": "Modify Key Block Header",
"CW": "Generate a Card Verification Code/Value (Visa/Mastercard)", 
"CY": "Verify a Card Verification Code/Value",
"EI": "Generate a Public/Private Key Pair", 
"EO": "Import a Public Key", 
"EW": "Generate an RSA Signature",
"EY": "Validate an RSA Signature", 
"GI": "Import Key or data under an RSA Public Key", 
"GK": "Export Key under an RSA Public Key",
"IO": "Generate Remote Management Session ID and Session Keys", 
"IQ": "Validate Authentication Code",
"IU": "Generate Remote Management Secure Message", 
"IW": "Validate and Recover Remote Management Secure Message", 
"IY": "Generate Digitised Card Single Use Keys", 
"LQ": "Generate an HMAC on a Block of Data",
"LS": "Verify an HMAC on a Bock of Data",
"LU": "Import an HMAC key under a ZMK",
"LW": "Export an HMAC key under a ZMK",
"LY": "Transalate a HMAC Key from Old LMK to New LMK",
"M0": "Encrypt Data Block", 
"M2": "Decrypt Data Block", 
"M4": "Translate Data Block",
"N0": "Generate a Random Value", 
"NC": "Perform Diagnostics",
"NO": "HSM Status",
"RA": "Cancel Authorized Activities",
"RY": "Calculate Card Security Codes (AMEX)"}


def parse_payshield_utilisation(string_table):  
    #[['8', '60,4\nA0,00001;B2,00060;M0,00043;M2,00213;']]
    #"load" , "frequenzy, utilisation\n<command>:<usage>;[<command>:<usage>;]*"
    parsed = {}


    #raw data
    parsed["payShieldUtilLoad"] = int(string_table[0][0])  
    parsed["payShieldUtilHostCmdVolume"] = string_table[0][1].replace('\n', ';;')

    #parsed data
    lines = string_table[0][1].split('\n')
    frequency, utilisation = lines[0].split(',')
    parsed["frequency"] = int(frequency)
    parsed["utilisation"] = int(utilisation)
    
    #Create command list and parse command usage
    parsed["commands"] = []

    for monitoredcmd,monitoredcmdtext in commanddictionary.items():
        command = {}
        command["monitoredcmd"] = monitoredcmd
        command["monitoredcmdtext"] = monitoredcmdtext
        command["monitoredcmdUsage"] = 0

        #parse command usage
        if len(lines) > 1 and len(lines[1].split(";")) > 1:
            for commands in lines[1].split(";"):
                if len(commands.split(',')) > 1:
                    cmd, volume = commands.split(',')
                    if monitoredcmd == cmd: 
                            command["monitoredcmdUsage"] = int(volume)

        parsed["commands"].append(command) 

    return parsed

def discover_payshield_utilisation(section):
    yield Service(item="Payshield Utilisation Load")
    yield Service(item="Payshield usage Total")
    yield Service(item="Payshield HostCmdVolume")
    for command, commandtext in commanddictionary.items():
        yield Service(item=f"Payshield usage {command}")


def check_payshield_utilisation(item, section):
    if 'Utilisation Load' in item:
        if int(section["payShieldUtilLoad"]) >= 90:
            yield Result(state=State.CRIT, summary=f"High usage above 90%!! Current Utilisation Load is {section["payShieldUtilLoad"]}%")
        if int(section["payShieldUtilLoad"]) >= 75:
            yield Result(state=State.WARN, summary=f"Usage above 75%!! Current Utilisation Load is {section["payShieldUtilLoad"]}%")
        else:
            yield Result(state=State.OK, summary=f"Current Utilisation Load is {section["payShieldUtilLoad"]}%")

        # Load Metric
        yield from check_levels(
            section["payShieldUtilLoad"],
            levels_upper = ("fixed", (90.0, 75.0)),
            metric_name = "load",
            label = "Load",
            boundaries = (0.0, 100.0),
            notice_only = True,
        )
    if 'usage Total' in item:
        yield Result(state=State.OK, summary=f"Total command usage is {section["utilisation"]}")
        yield from check_levels(
            section["utilisation"],
            metric_name = "usage",
            label = "usage",
            notice_only = True,
        )
    elif 'HostCmdVolume' in item:
        yield Result(state=State.OK, summary=f"Raw command usage string is {section["payShieldUtilHostCmdVolume"]}")


    for command in section["commands"]:
        if f"Payshield usage {command["monitoredcmd"]}" in item:
            
            yield Result(
                state=State.OK, 
                summary=f"command {command["monitoredcmd"]} was used {command["monitoredcmdUsage"]} times in last {section["frequency"]} Seconds ({command["monitoredcmdtext"]})"
            )
            # Command Metric
            yield from check_levels(
                command["monitoredcmdUsage"],
                metric_name = command["monitoredcmd"],
                label = f"{command["monitoredcmd"]} - {command["monitoredcmdtext"]}",
                notice_only = True,
            )

snmp_section_payshield_utilisation_setup = SimpleSNMPSection(
    name = "payshield10k_utilisation",
    parse_function = parse_payshield_utilisation,

    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "1.1.0",   # payShieldUtilLoad.0
            "1.2.0",   # payShieldUtilHostCmdVolume.0
        ],
    ),
)

check_plugin_payshield_utilisation = CheckPlugin(
    name = "payshield10k_utilisation",
    sections = [ "payshield10k_utilisation" ],
    service_name = "%s",
    discovery_function = discover_payshield_utilisation,
    check_function = check_payshield_utilisation,
)
