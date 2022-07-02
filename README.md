# Overview 
This repository contains the Monitoring Plugins for Check_mk for the following HSM Types:

* Thales Payshield 9000 
* Thales Payshield 10000 (Thales Payshield 10k) 

The check plugins are in the legacy format and are compatible with Check_mk 1.x and 2.x versions.

# Install
To install the plugin merge the content of the check_mk folder into the /omd/sites/#sitename#/local/share/check_mk folder 

# Notes
The payshield hsm must already be monitored with snmp in check_mk.

There are currently no check_mk check parameters, parameters must be changed in the python code of the check plugins.

# How can i get the utilisation Stats to work?

For the Utilisation stats to work properly via snmp a couple of settings are rquired:

via console use the following commands:
* use UTILENABLE to enable the collection of stats (Offline mode, No authorization) 
* use UTILCFG to set the "Measurement period for instantaneous statistics" to 60 seconds (Online mode, No authorization) 

via payshield manager:
* I don't know.. find out yourself :)

# Which Payshield commands utilisation stats are supported by the payshield10k_utilisation check?
Currently the following Command utilisation stats are supported. But this list can easily be updated.

* "A0": "Generate Key",
* "A6": "Import a Key",
* "A8": "Export a Key",
* "B2": "Echo Command",
* "BS": "Erase the Key Change Storage",
* "BU": "Generate Key Check Value",
* "BW": "Translate Keys from Old LMK to New LMK and Migrate to New Key Type",
* "CC": "Translate a PIN from One TPK to Another",
* "CS": "Modify Key Block Header",
* "CW": "Generate a Card Verification Code/Value (Visa/Mastercard)",
* "CY": "Verify a Card Verification Code/Value",
* "EI": "Generate a Public/Private Key Pair",
* "EO": "Import a Public Key",
* "EW": "Generate an RSA Signature",
* "EY": "Validate an RSA Signature",
* "GI": "Import Key or data under an RSA Public Key",
* "GK": "Export Key under an RSA Public Key",
* "IO": "Generate Remote Management Session ID and Session Keys",
* "IQ": "Validate Authentication Code",
* "IU": "Generate Remote Management Secure Message",
* "IW": "Validate and Recover Remote Management Secure Message",
* "IY": "Generate Digitised Card Single Use Keys",
* "LQ": "Generate an HMAC on a Block of Data",
* "LS": "Verify an HMAC on a Bock of Data",
* "LU": "Import an HMAC key under a ZMK",
* "LW": "Export an HMAC key under a ZMK",
* "LY": "Transalate a HMAC Key from Old LMK to New LMK",
* "M0": "Encrypt Data Block",
* "M2": "Decrypt Data Block",
* "M4": "Translate Data Block",
* "N0": "Generate a Random Value",
* "NC": "Perform Diagnostics",
* "NO": "HSM Status",
* "RA": "Cancel Authorized Activities",
* "RY": "Calculate Card Security Codes (AMEX)"

To add support for more commands simply update the commanddictionary in payshield10k_utilisation
