
First try a snmpwalk on your device:

snmpwalk -v3 -c public -u public <payshield-device> .1.3.6.1.4.1.4096.2.2.10000



install these files into



discover the service on a host via :

cmk -vI --detect-plugins=payshield10k_device_state <payshield-device>
cmk -vI --detect-plugins=payshield10k_tamper_state <payshield-device>
cmk -vI --detect-plugins=payshield10k_errorlog <payshield-device>
cmk -vI --detect-plugins=payshield10k_info <payshield-device>
cmk -vI --detect-plugins=payshield10k_hardware_state <payshield-device>


then test the plugin:

cmk -v --detect-plugins=payshield10k_device_state <payshield-device>
cmk -v --detect-plugins=payshield10k_tamper_state <payshield-device>
cmk -v --detect-plugins=payshield10k_errorlog <payshield-device>
cmk -v --detect-plugins=payshield10k_info <payshield-device>



#how to DEBUG:
if a crash happens search for the report id in the check_mk folder

find ~/ -name "*85520bd4-8972-11f0-a513-005056b2297d*"
/omd/sites/xxxx/var/check_mk/crashes/check/245deed8-8972-11f0-83eb-005056b2297d

then do:
cat /omd/sites/xxxx/var/check_mk/crashes/check/85520bd4-8972-11f0-a513-005056b2297d/crash.info
to get details of crash



if you need debug output do:

{{{from pprint import pprint}}}

and add these in the code:

{{{pprint(string_table)}}}