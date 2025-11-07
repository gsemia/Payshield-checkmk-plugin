#!/usr/bin/env python3

# OIDs used:
# THALES-PAYSHIELD-MIB::payShieldSettingsPCICompliant.0         .1.3.6.1.4.1.4096.2.2.10000.15.1.0
# THALES-PAYSHIELD-MIB::payShieldSettingsHashSecuritySetting.0  .1.3.6.1.4.1.4096.2.2.10000.15.2.0
# THALES-PAYSHIELD-MIB::payShieldSettingsHashGeneralSetting.0   .1.3.6.1.4.1.4096.2.2.10000.15.3.0
# THALES-PAYSHIELD-MIB::payShieldSettingsHashConfigureCommand.0 .1.3.6.1.4.1.4096.2.2.10000.15.4.0
# THALES-PAYSHIELD-MIB::payShieldSettingsHashAuditSetting.0     .1.3.6.1.4.1.4096.2.2.10000.15.5.0
# THALES-PAYSHIELD-MIB::payShieldSettingsHashLMK.0 			    .1.3.6.1.4.1.4096.2.2.10000.15.6.0
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.1 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.1 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.2 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.2
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.3 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.3 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.4 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.4 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.5 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.5 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.6 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.6
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.7 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.7 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.8 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.8 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.9 		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.9 
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.10		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.10
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.11		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.11
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.12		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.12
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.13		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.13
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.14		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.14
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.15		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.15
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.16		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.16
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.17		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.17
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.18		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.18
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.19		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.19
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.20		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.20
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.21		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.21
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.22		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.22
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.23		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.23
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.24		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.24
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.25		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.25
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.26		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.26
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.27		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.27
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.28		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.28
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.29		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.29
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.30		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.30
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.31		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.31
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.32		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.32
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.33		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.33
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.34		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.34
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.35		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.35
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.36		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.36
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.37		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.37
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.38		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.38
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.39		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.39
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.40		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.40
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.41		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.41
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.42		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.42
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.43		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.43
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.44		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.44
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.45		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.45
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.46		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.46
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.47		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.47
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.48		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.48
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.49		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.49
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.50		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.50
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.51		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.51
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.52		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.52
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.53		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.53
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.54		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.54
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.55		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.55
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.56		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.56
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.57		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.57
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.58		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.58
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.59		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.59
# THALES-PAYSHIELD-MIB::payShieldSecuritySettingsData.60		.1.3.6.1.4.1.4096.2.2.10000.15.7.1.2.60
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_security_settings.py

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

def parse_payshield_security_settings(string_table):
    parsed = {}
    column_names = [
        "payShieldSettingsPCICompliant",  
        "payShieldSettingsHashSecuritySetting",  
        "payShieldSettingsHashGeneralSetting",  
        "payShieldSettingsHashConfigureCommand",  
        "payShieldSettingsHashAuditSetting",  
        "payShieldSettingsHashLMK",  
        "xxx1",
        "User_storage_key_length",
        "xxx3",
        "xxx4",
        "xxx5",
        "Solicitation_batch_size",
        "xxx7",
        "PIN_length",
        "Encrypted_PIN_length",
        "xxx10",
        "xxx11",
        "xxx12",
        "xxx13",
        "xxx14",
        "xxx15",
        "xxx16",
        "ZMK_length",
        "Decimalization_tables",
        "xxx19",
        "xxx20",
        "xxx21",
        "xxx22",
        "Minimum_HMAC_length_in_bytes",
        "xxx24",
        "xxx25",
        "xxx26",
        "xxx27",
        "xxx28",
        "xxx29",
        "xxx30",
        "xxx31",
        "xxx32",
        "xxx33",
        "xxx34",
        "xxx35",
        "xxx36",
        "xxx37",
        "xxx38",
        "xxx39",
        "xxx40",
        "xxx41",
        "xxx42",
        "xxx43",
        "xxx44",
        "xxx45",
        "xxx46",
        "xxx47",
        "xxx48",
        "xxx49",
        "xxx50",
        "xxx51",
        "xxx52",
        "xxx53",
        "xxx54",
        "xxx55",
        "xxx56",
        "xxx57",
        "xxx58",
        "xxx59",
        "xxx60"

    ]
    for line in string_table:
        for n in range(0, len(column_names)):
            parsed[column_names[n]] = line[n].replace('\n', '')
    return parsed

def discover_payshield_security_settings(section):
    yield Service()

def check_payshield_security_settings(section):
    pcicompliance = { "1" : "Yes", "2" : "No" }
    yield Result(
        state=State.OK,
        summary=f"Payshield Security Settings PCI Compliant: {pcicompliance[section["payShieldSettingsPCICompliant"]]}",
        details=f"Payshield Security Settings PCI Compliant: {pcicompliance[section["payShieldSettingsPCICompliant"]]}\n" +
            f"Payshield Settings Hash Security Setting: {section["payShieldSettingsHashSecuritySetting"]}\n" +
            f"Payshield Settings Hash General Setting: {section["payShieldSettingsHashGeneralSetting"]}\n" +
            f"Payshield Settings Hash Configure Command: {section["payShieldSettingsHashConfigureCommand"]}\n" +
            f"Payshield Settings Hash Audit Setting: {section["payShieldSettingsHashAuditSetting"]}\n" +
            f"Payshield Settings Hash LMK: {section["payShieldSettingsHashLMK"]}\n" +
            f"xxxt1: {section['xxx1']}\n " +
            f"User storage key length: {section['User_storage_key_length']}\n " +
            f"xxxt2: {section['xxx3']}\n " +
            f"xxxt3: {section['xxx4']}\n " +
            f"xxxt4: {section['xxx5']}\n " +
            f"Solicitation batch size: {section['Solicitation_batch_size']}\n " +
            f"xxxt5: {section['xxx7']}\n " +
            f"PIN length: {section['PIN_length']}\n " +
            f"Encrypted PIN length: {section['Encrypted_PIN_length']}\n " +
            f"xxxt6: {section['xxx10']}\n " +
            f"xxxt7: {section['xxx11']}\n " +
            f"xxxt8: {section['xxx12']}\n " +
            f"xxxt9: {section['xxx13']}\n " +
            f"xxxt10: {section['xxx14']}\n " +
            f"xxxt11: {section['xxx15']}\n " +
            f"xxxt12: {section['xxx16']}\n " +
            f"ZMK length: {section['ZMK_length']}\n " +
            f"Decimalization tables: {section['Decimalization_tables']}\n " +
            f"xxxt13: {section['xxx19']}\n " +
            f"xxxt14: {section['xxx20']}\n " +
            f"xxxt15: {section['xxx21']}\n " +
            f"xxxt16: {section['xxx22']}\n " +
            f"Minimum HMAC length in bytes: {section['Minimum_HMAC_length_in_bytes']}\n " +
            f"xxxt17: {section['xxx24']}\n " +
            f"xxxt18: {section['xxx25']}\n " +
            f"xxxt19: {section['xxx26']}\n " +
            f"xxxt20: {section['xxx27']}\n " +
            f"xxxt21: {section['xxx28']}\n " +
            f"xxxt22: {section['xxx29']}\n " +
            f"xxxt23: {section['xxx30']}\n " +
            f"xxxt24: {section['xxx31']}\n " +
            f"xxxt25: {section['xxx32']}\n " +
            f"xxxt26: {section['xxx33']}\n " +
            f"xxxt27: {section['xxx34']}\n " +
            f"xxxt28: {section['xxx35']}\n " +
            f"xxxt29: {section['xxx36']}\n " +
            f"xxxt30: {section['xxx37']}\n " +
            f"xxxt31: {section['xxx38']}\n " +
            f"xxxt32: {section['xxx39']}\n " +
            f"xxxt33: {section['xxx40']}\n " +
            f"xxxt34: {section['xxx41']}\n " +
            f"xxxt35: {section['xxx42']}\n " +
            f"xxxt36: {section['xxx43']}\n " +
            f"xxxt37: {section['xxx44']}\n " +
            f"xxxt38: {section['xxx45']}\n " +
            f"xxxt39: {section['xxx46']}\n " +
            f"xxxt40: {section['xxx47']}\n " +
            f"xxxt41: {section['xxx48']}\n " +
            f"xxxt42: {section['xxx49']}\n " +
            f"xxxt43: {section['xxx50']}\n " +
            f"xxxt44: {section['xxx51']}\n " +
            f"xxxt45: {section['xxx52']}\n " +
            f"xxxt46: {section['xxx53']}\n " +
            f"xxxt47: {section['xxx54']}\n " +
            f"xxxt48: {section['xxx55']}\n " +
            f"xxxt49: {section['xxx56']}\n " +
            f"xxxt50: {section['xxx57']}\n " +
            f"xxxt51: {section['xxx58']}\n " +
            f"xxxt52: {section['xxx59']}\n " +
            f"xxxt53: {section['xxx60']}\n "

    )

snmp_section_payshield_security_settings_setup = SimpleSNMPSection(
    name = "payshield10k_security_settings",
    parse_function = parse_payshield_security_settings,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "15.1.0",    # THALES-PAYSHIELD-MIB::payShieldSettingsPCICompliant.0 = INTEGER: true(1)
            "15.2.0",    # THALES-PAYSHIELD-MIB::payShieldSettingsHashSecuritySetting.0 = STRING: cf55cf
            "15.3.0",    # THALES-PAYSHIELD-MIB::payShieldSettingsHashGeneralSetting.0 = STRING: 9b4ee9
            "15.4.0",    # THALES-PAYSHIELD-MIB::payShieldSettingsHashConfigureCommand.0 = STRING: 874fab
            "15.5.0",    # THALES-PAYSHIELD-MIB::payShieldSettingsHashAuditSetting.0 = STRING: 7ac7e2
            "15.6.0",    # THALES-PAYSHIELD-MIB::payShieldSettingsHashLMK.0 = STRING: b654bb
            "15.7.1.2.1",    # 
            "15.7.1.2.2",    # User storage key length
            "15.7.1.2.3",    # 
            "15.7.1.2.4",    # 
            "15.7.1.2.5",    # 
            "15.7.1.2.6",    # Solicitation batch size
            "15.7.1.2.7",    # 
            "15.7.1.2.8",    # PIN length
            "15.7.1.2.9",    # Encrypted PIN length
            "15.7.1.2.10",   # 
            "15.7.1.2.11",   # 
            "15.7.1.2.12",   # 
            "15.7.1.2.13",   # 
            "15.7.1.2.14",   # 
            "15.7.1.2.15",   # 
            "15.7.1.2.16",   # 
            "15.7.1.2.17",   # ZMK length
            "15.7.1.2.18",   # Decimalization tables
            "15.7.1.2.19",   # 
            "15.7.1.2.20",   # 
            "15.7.1.2.21",   # 
            "15.7.1.2.22",   # 
            "15.7.1.2.23",   # Minimum HMAC length in bytes
            "15.7.1.2.24",   # 
            "15.7.1.2.25",   # 
            "15.7.1.2.26",   # 
            "15.7.1.2.27",   # 
            "15.7.1.2.28",   # 
            "15.7.1.2.29",   # 
            "15.7.1.2.30",   # 
            "15.7.1.2.31",   # 
            "15.7.1.2.32",   # 
            "15.7.1.2.33",   # 
            "15.7.1.2.34",   # 
            "15.7.1.2.35",   # 
            "15.7.1.2.36",   # 
            "15.7.1.2.37",   # 
            "15.7.1.2.38",   # 
            "15.7.1.2.39",   # 
            "15.7.1.2.40",   # 
            "15.7.1.2.41",   # 
            "15.7.1.2.42",   # 
            "15.7.1.2.43",   # 
            "15.7.1.2.44",   # 
            "15.7.1.2.45",   # 
            "15.7.1.2.46",   # 
            "15.7.1.2.47",   # 
            "15.7.1.2.48",   # 
            "15.7.1.2.49",   # 
            "15.7.1.2.50",   # 
            "15.7.1.2.51",   # 
            "15.7.1.2.52",   # 
            "15.7.1.2.53",   # 
            "15.7.1.2.54",   # 
            "15.7.1.2.55",   # 
            "15.7.1.2.56",   # 
            "15.7.1.2.57",   # 
            "15.7.1.2.58",   # 
            "15.7.1.2.59",   # 
            "15.7.1.2.60"    #                                          
        ],
    ),
)

check_plugin_payshield_security_settings = CheckPlugin(
    name = "payshield10k_security_settings",
    sections = [ "payshield10k_security_settings" ],
    service_name = "Payshield Security Settings",
    discovery_function = discover_payshield_security_settings,
    check_function = check_payshield_security_settings,
)

