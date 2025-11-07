#!/usr/bin/env python3

# OIDs used:
# THALES-PAYSHIELD-MIB::payShieldNtpIsNtpEnabled.0 = INTEGER: false(2)
# THALES-PAYSHIELD-MIB::payShieldNtpServersListIpAddress.1 = IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersListIpAddress.2 = IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersListIpAddress.3 = IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersListIpAddress.4 = IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusNameIpAddress.1 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusNameIpAddress.2 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusNameIpAddress.3 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusNameIpAddress.4 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusMS.1 = STRING:
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusMS.2 = STRING:
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusMS.3 = STRING:
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusMS.4 = STRING:
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusStratum.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusStratum.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusStratum.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusStratum.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusPoll.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusPoll.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusPoll.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusPoll.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusReach.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusReach.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusReach.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusReach.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastRx.1 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastRx.2 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastRx.3 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastRx.4 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastSample.1 = STRING: +0ns[   +0ns] +/-    0ns
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastSample.2 = STRING: +0ns[   +0ns] +/-    0ns
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastSample.3 = STRING: +0ns[   +0ns] +/-    0ns
# THALES-PAYSHIELD-MIB::payShieldNtpServersStatusLastSample.4 = STRING: +0ns[   +0ns] +/-    0ns
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNameIpAddress.1 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNameIpAddress.2 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNameIpAddress.3 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNameIpAddress.4 = Wrong Type (should be INTEGER): IpAddress: 0.0.0.0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusMode.1 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusMode.2 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusMode.3 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusMode.4 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKeyID.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKeyID.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKeyID.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKeyID.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusType.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusType.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusType.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusType.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKLen.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKLen.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKLen.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusKLen.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusLast.1 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusLast.2 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusLast.3 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusLast.4 = STRING: -
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusAtmp.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusAtmp.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusAtmp.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusAtmp.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNAK.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNAK.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNAK.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusNAK.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCook.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCook.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCook.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCook.4 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCLen.1 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCLen.2 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCLen.3 = INTEGER: 0
# THALES-PAYSHIELD-MIB::payShieldNtpServersAuthStatusCLen.4 = INTEGER: 0
# detect function looks for sysDescr == 'payShield 10K'

# Author: Rolf Koch - rolf.koch@netcetera.com - http://netcetera.com

#
# Store in your Checkmk site at:
# ~/local/lib/python3/cmk_addons/plugins/payshield10k/agent_based/payshield10k_selfdiag.py

from cmk.agent_based.v2 import (
    CheckPlugin,
    CheckResult,
    DiscoveryResult,
    Result,
    Service,
    SimpleSNMPSection,
    SNMPTree,
    State,
    startswith,
)

def parse_payshield_ntp(string_table):
    result = {
        "ntp_enabled": string_table[0][0],
        "ntp_servers": string_table[1:5],  # IPs of servers
        "stratum": string_table[5:9],
        "reach": string_table[9:13],
        "last_sample": string_table[13:17],
    }
    return result

def discover_payshield_ntp(section):
    yield Service()

def check_payshield_ntp(section):
    ntp_enabled = section["ntp_enabled"]
    servers = section["ntp_servers"]
    stratum = section["stratum"]
    reach = section["reach"]
    last_sample = section["last_sample"]

    if ntp_enabled != "1":
        yield Result(state=State.OK, summary="NTP is disabled")
        return

    valid_servers = [ip for ip in servers if ip != "0.0.0.0"]
    if not valid_servers:
        yield Result(state=State.CRIT, summary="No valid NTP servers configured")
        return

    issues = []
    for i, ip in enumerate(servers):
        if ip == "0.0.0.0":
            issues.append(f"Server {i+1}: IP not set")
        elif reach[i] == "0":
            issues.append(f"Server {i+1} ({ip}): Not reachable")
        elif stratum[i] == "0":
            issues.append(f"Server {i+1} ({ip}): Invalid stratum")
        elif "+0ns" in last_sample[i]:
            issues.append(f"Server {i+1} ({ip}): No sync data")

    if issues:
        yield Result(state=State.WARN, summary="NTP issues detected", details="\n".join(issues))
    else:
        yield Result(state=State.OK, summary="NTP is enabled and servers are reachable")

snmp_section_payshield_ntp_setup = SimpleSNMPSection(
    name="payshield10k_ntp",
    parse_function=parse_payshield_ntp,
    detect = startswith(
        ".1.3.6.1.2.1.1.1.0",
        "payShield 10K",
    ),
    fetch=SNMPTree(
        base=".1.3.6.1.4.1.4096.2.2.10000.17",
        oids=[
            "1.0",  # payShieldNtpIsNtpEnabled
            "2.1.1.2.1", "2.1.1.2.2", "2.1.1.2.3", "2.1.1.2.4",  # Server IPs
            "3.1.1.4.1", "3.1.1.4.2", "3.1.1.4.3", "3.1.1.4.4",  # Stratum
            "3.1.1.6.1", "3.1.1.6.2", "3.1.1.6.3", "3.1.1.6.4",  # Reach
            "3.1.1.8.1", "3.1.1.8.2", "3.1.1.8.3", "3.1.1.8.4",  # Last Sample
        ],
    ),
)

check_plugin_payshield_ntp = CheckPlugin(
    name="payshield10k_ntp",
    service_name="Payshield NTP",
    sections=["payshield10k_ntp"],
    discovery_function=discover_payshield_ntp,
    check_function=check_payshield_ntp,
)
