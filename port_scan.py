#! /usr/bin/env python
############################################################################################
#created by infosec institute,
#edited by br0k3ngl255
############################################################################################

#Lib import
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
 
#Vars
dst_ip = sysargv[0] 
src_port = RandShort()
dst_port=sysarg[1]
 
###
#Main
###

tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)
if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
print "Closed"
elif(tcp_connect_scan_resp.haslayer(TCP)):
if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
print "Open"
elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14):
print "Closed"
