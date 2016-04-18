# gremlin

Small script used to <strike>get revenge on a roommate</stirke> simulate wireless service distruptions.

The script requires aircrack-ng suite and a compatible wireless adapter.

Also requires a targets.txt in the same directory, which consists of:
name_of_target_device mac_address_of_device mac_address_of_connected_AP

all this information including mac of correspodning Access Point can be found via airodump
in the aircrack-ng suite.

After targets.txt is populated with the desired targets, simply run the script and enter
the wireless interface to be used (wireless interface may have to be set to monitor mode).
