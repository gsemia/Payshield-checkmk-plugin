#!/usr/bin/env python3

# OIDs used:
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldSystemDateAndTime.0                                  .1.3.6.1.4.1.4096.2.2.10000.5.1.0 = Hex-STRING: 07 E4 0B 0D 0D 13 2D 00
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldSystemSerialNum.0                                    .1.3.6.1.4.1.4096.2.2.10000.5.2.0 = STRING: "S0246378732H"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldSystemModel.0                                        .1.3.6.1.4.1.4096.2.2.10000.5.3.0 = STRING: "PS10-S"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldFraudPinVerifyLimitsExceeded.0                       .1.3.6.1.4.1.4096.2.2.10000.6.1.0 = INTEGER: 2
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldFraudPinAttackLimitsExceeded.0                       .1.3.6.1.4.1.4096.2.2.10000.6.2.0 = INTEGER: 2
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareBaseRelease.0                         .1.3.6.1.4.1.4096.2.2.10000.7.1.0 = STRING: "1.0f"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareRevision.0                            .1.3.6.1.4.1.4096.2.2.10000.7.2.0 = STRING: "1500-1022"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareBuildNumber.0                         .1.3.6.1.4.1.4096.2.2.10000.7.3.0 = STRING: "0000"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareHSMCoreAPIVersion.0          			.1.3.6.1.4.1.4096.2.2.10000.7.4.0 = ""
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareCPLDVersion.0                         .1.3.6.1.4.1.4096.2.2.10000.7.5.0 = STRING: "1.2.3"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareSPVersion.0                           .1.3.6.1.4.1.4096.2.2.10000.7.6.0 = STRING: "1.1.29"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareSPBootVersion.0                       .1.3.6.1.4.1.4096.2.2.10000.7.7.0 = STRING: "1.0.0"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareBootstrapVersion.0            		.1.3.6.1.4.1.4096.2.2.10000.7.8.0 = STRING: "1.1.40"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareFirmwareVersion.0                     .1.3.6.1.4.1.4096.2.2.10000.7.9.0 = STRING: "1.3.1"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldVersionSoftwareDeploymentVersion.0           		.1.3.6.1.4.1.4096.2.2.10000.7.10.0 = STRING: "1.3.2"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLicensingPerformanceModel.0                          .1.3.6.1.4.1.4096.2.2.10000.8.1.0 = INTEGER: 25
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLicensingPackage.0                                   .1.3.6.1.4.1.4096.2.2.10000.8.2.0 = STRING: "Premium Package:Premium Key Management;Magnetic Stripe Issuing;Magnetic Stripe Transaction Processing;EMV Chip, Contactless & Mobile Issuing;EMV Transaction Processing;User Authentication;Data Protection;"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLicensingOptionalLicenseCount.0                      .1.3.6.1.4.1.4096.2.2.10000.8.3.0 = INTEGER: 1
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLicensingOptionalLicensesList.0                      .1.3.6.1.4.1.4096.2.2.10000.8.4.0 = STRING: "001:LMKx5;"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLicensingCryptoAlgorithmCount.0                      .1.3.6.1.4.1.4096.2.2.10000.8.5.0 = INTEGER: 3
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldLicensingCryptoAlgorithmList.0                       .1.3.6.1.4.1.4096.2.2.10000.8.6.0 = STRING: "3DES;AES;RSA;"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldEnabledHostCommandsCount.0                           .1.3.6.1.4.1.4096.2.2.10000.9.1.0 = INTEGER: 38
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldEnabledHostCommandsList.0                            .1.3.6.1.4.1.4096.2.2.10000.9.2.0 = STRING: "A0;A6;A8;B2;BS;BU;BW;CC;CS;CW;CY;EI;EO;EW;EY;GI;GK;IO;IQ;IU;IW;IY;L0;L8;LG;LQ;LS;LU;LW;LY;M0;M2;M4;N0;NC;NO;RA;RY;"
# THALES-ESECURITY-PAYSHIELD-MIB::payShieldSettingsPCICompliant.0								.1.3.6.1.4.1.4096.2.2.10000.15.1.0 = INTEGER: 1
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_info.py

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

def parse_payshield_info(string_table):
    parsed = {}
    column_names = [
        "payShieldSystemDateAndTime",
        "payShieldSystemSerialNum",
        "payShieldSystemModel",
        "payShieldFraudPinVerifyLimitsExceeded",
        "payShieldFraudPinAttackLimitsExceeded",
        "payShieldVersionSoftwareBaseRelease",
        "payShieldVersionSoftwareRevision", 
        "payShieldVersionSoftwareBuildNumber",
        "payShieldVersionSoftwareHSMCoreAPIVersion",
        "payShieldVersionSoftwareCPLDVersion",
        "payShieldVersionSoftwareSPVersion",
        "payShieldVersionSoftwareSPBootVersion",
        "payShieldVersionSoftwareBootstrapVersion",
        "payShieldVersionSoftwareFirmwareVersion",
        "payShieldVersionSoftwareDeploymentVersion",
        "payShieldLicensingPerformanceModel",
        "payShieldLicensingPackage",
        "payShieldLicensingOptionalLicenseCount",
        "payShieldLicensingOptionalLicensesList",
        "payShieldLicensingCryptoAlgorithmCount",
        "payShieldLicensingCryptoAlgorithmList",
        "payShieldEnabledHostCommandsCount",
        "payShieldEnabledHostCommandsList",
        "payShieldSettingsPCICompliant"
    ]
    for line in string_table:
        for n in range(0, len(column_names)):
            parsed[column_names[n]] = line[n].replace('\n', '')
    return parsed

def discover_payshield_info(section):
    yield Service()

def check_payshield_info(section):
    pcicompliance = { "1" : "Yes", "2" : "No" }
    yield Result(
        state=State.OK,
        summary=f"Payshield Info: {section["payShieldSystemSerialNum"]}",
        details=f"System Serial Number: {section["payShieldSystemSerialNum"]}\n "+
            f"System Date and Time: {section["payShieldSystemDateAndTime"]}\n "+
            f"System Model: {section["payShieldSystemModel"]}\n "+
            f"Fraud Pin Verify Limit Exceeded: {section["payShieldFraudPinVerifyLimitsExceeded"]}\n"+
            f"Fraud Pin Attack Limits Exceeded: {section["payShieldFraudPinAttackLimitsExceeded"]}\n"+
            f"Version Software Base Release: {section["payShieldVersionSoftwareBaseRelease"]}\n"+
            f"Version Software Revision {section["payShieldVersionSoftwareRevision"]}\n"+
            f"Version Software Build Number: {section["payShieldVersionSoftwareBuildNumber"]}\n"+
            f"Version Software HSM Core API Version: {section["payShieldVersionSoftwareRevision"]}\n"+
            f"Version Software CPLD Version: {section["payShieldVersionSoftwareHSMCoreAPIVersion"]}\n"+
            f"Version Software SP Version: {section["payShieldVersionSoftwareSPVersion"]}\n"+
            f"Version Software SP Boot Version: {section["payShieldVersionSoftwareSPBootVersion"]}\n"+
            f"Version Software Bootstrap Version: {section["payShieldVersionSoftwareSPBootVersion"]}\n"+
            f"Version Software Firmware Version: {section["payShieldVersionSoftwareFirmwareVersion"]}\n"+
            f"Version Software Deployment Version: {section["payShieldVersionSoftwareDeploymentVersion"]}\n"+
            f"Licensing Performance Model: {section["payShieldLicensingPerformanceModel"]}\n"+
            f"Licensing Package: {section["payShieldLicensingPackage"]}\n"+
            f"Licensing Optional License Count: {section["payShieldLicensingOptionalLicenseCount"]}\n"+
            f"Licensing Optional Licenses List: {section["payShieldLicensingOptionalLicensesList"]}\n"+
            f"Licensing Crypto Algorithm Count: {section["payShieldLicensingCryptoAlgorithmCount"]}\n"+
            f"Licensing Crypto Algorithm List: {section["payShieldLicensingCryptoAlgorithmList"]}\n"+
            f"Enabled Host Commands Count: {section["payShieldEnabledHostCommandsCount"]}\n"+
            f"Enabled Host Commands List: {section["payShieldEnabledHostCommandsList"]}\n"+
            f"Settings PCI Compliant: {pcicompliance[section["payShieldSettingsPCICompliant"]]}"
    )

snmp_section_payshield_info_setup = SimpleSNMPSection(
    name = "payshield10k_info",
    parse_function = parse_payshield_info,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch = SNMPTree(
        base = '.1.3.6.1.4.1.4096.2.2.10000',
        oids = [
            "5.1.0",   #        payShieldSystemDateAndTime.0
            "5.2.0",   #        payShieldSystemSerialNum.0
            "5.3.0",   #        payShieldSystemModel.0
            "6.1.0",   #        payShieldFraudPinVerifyLimitsExceeded.0
            "6.2.0",   #        payShieldFraudPinAttackLimitsExceeded.0
            "7.1.0",   #        payShieldVersionSoftwareBaseRelease.0
            "7.2.0",   #        payShieldVersionSoftwareRevision.0
            "7.3.0",   #        payShieldVersionSoftwareBuildNumber.0
            "7.4.0",   #        payShieldVersionSoftwareHSMCoreAPIVersion.0
            "7.5.0",   #        payShieldVersionSoftwareCPLDVersion.0
            "7.6.0",   #        payShieldVersionSoftwareSPVersion.0
            "7.7.0",   #        payShieldVersionSoftwareSPBootVersion.0
            "7.8.0",   #        payShieldVersionSoftwareBootstrapVersion.0
            "7.9.0",   #        payShieldVersionSoftwareFirmwareVersion.0
            "7.10.0",  #        payShieldVersionSoftwareDeploymentVersion.0                                                   
            "8.1.0",   #        payShieldLicensingPerformanceModel.0
            "8.2.0",   #        payShieldLicensingPackage.0
            "8.3.0",   #        payShieldLicensingOptionalLicenseCount.0
            "8.4.0",   #        payShieldLicensingOptionalLicensesList.0
            "8.5.0",   #        payShieldLicensingCryptoAlgorithmCount.0
            "8.6.0",   #        payShieldLicensingCryptoAlgorithmList.0
            "9.1.0",   #        payShieldEnabledHostCommandsCount.0
            "9.2.0",   #        payShieldEnabledHostCommandsList.0
            "15.1.0",  #    payShieldSettingsPCICompliant.0
        ],
    ),
)

check_plugin_payshield_info = CheckPlugin(
    name = "payshield10k_info",
    sections = [ "payshield10k_info" ],
    service_name = "Payshield Info",
    discovery_function = discover_payshield_info,
    check_function = check_payshield_info,
)
