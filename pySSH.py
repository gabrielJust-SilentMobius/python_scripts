#!/usr/bin/env python

########################################################################
#created by br0k3ngla55 for linuxsystems LTD
#implementation pxssh library
########################################################################

#import Libs>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
import pxssh
import getpass

###Vars++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')

###
#Main/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
###

try:                                                            
    s = pxssh.pxssh()  
    s.login (hostname, username, password)
    s.sendline ('uptime')   # run a command
    s.prompt()             # match the prompt
    print s.before          # print everything before the prompt.
    s.sendline ('ls -l')
    s.prompt()
    print s.before
    s.sendline ('df -h')
    s.prompt()
    print s.before
    s.logout()
except pxssh.ExceptionPxssh, e:
    print "pxssh failed on login."
    print str(e)
