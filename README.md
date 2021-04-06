This repository contains the Monitoring Plugins for Check_mk for the following HSM Types:

* Thales Payshield 9000 
* Thales Payshield 10000 (Thales Payshield 10k) 
* Entrust nShield Connect (limited)

To install the plugin merge the content of the check_mk folder into the /omd/sites/#sitename#/local/share/check_mk folder 

The payshield hsm must already be monitored with snmp in check_mk.
The Entrust nShield Connect is more complicated. You need to have the SNMP Component installed on a client with the security world software and this plugin monitors that clients SNMP Interface. The nShield HSM itself is not monitorable via snmp directly.
