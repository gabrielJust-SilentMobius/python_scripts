#!/usr/bin/env python
#######################################################################
#created by : violent python book author--> TJ O'Conner
#	edited by : br0k3ngl255
#######################################################################
#simple nmap implimitation with python
###import libs+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
import nmap

###Funcs /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
def nmapScan(tgtHost, tgtPort):
	nmScan = nmap.PortScanner()
	nmScan.scan(tgtHost, tgtPort)
	state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	print("[*] " + tgtHost + " tcp/" + tgtPort + " " + state)


###
#Main
###
nmapScan('127.0.0.1', '22')
