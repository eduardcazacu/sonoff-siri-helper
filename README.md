# sonoff-siri-helper
Raspberry Pi application that helps Apple Shortcuts find the LAN IP of Sonoff devices in DIY mode.

Sonoff smart switches in DIY mode can only be controlled when knowing their IP if using the REST API. In cases where the network DHCP server cannot be configured to serve the devices a static IP, an alternative is needed.

This script is designed to run on a Raspberry Pi. An Apple Shortcut can make an HTTP get request to the Raspberry PI on port 8080 which will return the ip of a Sonoff device on the same network. By default, the Raspberry Pi can be found at http://raspberrypi.local.

## Limitations
Currently this script supports only one Sonoff device on the network.

## Usage
* Edit the sonoff-siri-helper.py hostname to the device's hostname (by default raspberrypi.local)
* Edit the sonoff-siri-helper.service file to point to the sonoff-siri-helper.py script (by default this script is expected to be in /home/pi/sonoff-siri-helper/)
* Add the sonoff-siri-helper.service file in /etc/systemd/system/
* Enable the service:    ```sudo systemctl enable sonoff-siri-helper```
* Start the service:     ```sudo systemctl start sonoff-siri-helper```

## Siri Shortcuts
* Make an HTTP GET call to http://<raspberrrypi-hostname>.local:8080
* Use the result of the call as the address field of a second HTTP call, this time POST.
* As a JSON body add a dictiponary entry with key "data". Inside the dictionary and a Text item with key "switch" and value "on" or "off" depending on the desired result. More information about the Sonoff REST API [here](https://github.com/itead/Sonoff_Devices_DIY_Tools/blob/master/SONOFF%20DIY%20MODE%20Protocol%20Doc%20v1.4.md)

## Disclosure
The files in this repository are provided with absolutely no waranty. This project is not actively maintained. 
