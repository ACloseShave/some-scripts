#!/bin/bash

# Pull the last 6 of the serial number

serial=$(ioreg -rd1 -c IOPlatformExpertDevice | awk -F'"' '/IOPlatformSerialNumber/{print $4}' | tail -c 7)

#Change computer names to "OSX-" + last 6 

/usr/sbin/scutil --set ComputerName "OSX-$serial"
/usr/sbin/scutil --set LocalHostName "OSX-$serial"
/usr/sbin/scutil --set HostName "OSX-$serial"
