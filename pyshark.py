#!/usr/bin/env python
#######################################################################
# created by thepacketgeek tutorial
#
#
########################################################################

import pyshark

# Open saved trace file 
cap = pyshark.FileCapture('/tmp/mycapture.cap')

# Sniff from interface
capture = pyshark.LiveCapture(interface='wlan0')
capture.sniff(timeout=10)
