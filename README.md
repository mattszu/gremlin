# gremlin

Small script used to <strike>get revenge on a roommate</strike> simulate periodic wireless service distruptions.
The script progressively steps through target list and sends deauth packets (100) per device (effectively
denying service), then waits a set amount of time for <strike>(victim's hope to return)</strike> devices
to reconnect, before recommencing disruptions.

The script requires <b>aircrack-ng suite</b> and a <b>compatible wireless adapter</b>.

Also requires a <b>targets.txt</b> in the same directory, which consists of:
<br>
<br>
<b>name_of_target_device mac_address_of_device mac_address_of_connected_AP</b>
<br>
<br>
separated by single space

all this information including mac of correspodning Access Point can be found via airodump
in the aircrack-ng suite.

After targets.txt is populated with the desired targets, simply run the script and enter
the wireless interface to be used (wireless interface may have to be set to monitor mode).
