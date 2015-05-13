#!/usr/bin/env python
'''
Purpose: see wireless probes sent by devices at your phisical area.
created by : br0k3ngl255

'''
import os
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

interface = 'mon0'
clients = []
essid = []
def sniffmgmt(packet):
    types = (0, 2, 4, 8)
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype in types:
            if packet.addr2 not in clients:
                print ('%s | %s') %(packet.addr2,packet.info) 
                
                clients.append(packet.addr2)
                clients.append(packet.info)

capture.sniff(iface=interface, prn=sniffmgmt)
