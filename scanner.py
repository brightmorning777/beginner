#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# Ask for input
remoteServer	= input("enter the ip: ")
remoteServerIP 	= socket.gethostbyname(remoteServer)

# Print a banner with information
print("-" * 60)
print("Please wait while I scan your target: " , remoteServerIP)
print("-" * 60)

# check what time the scan started
t1 = datetime.now()

#Using the range function to specify ports (here it will scan all ports between 1 and 1024)


# We also put in some error handling for catching errors

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:       Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("Your pressed CTRL+C")
    sys.exit()

except socket.gaierror:
    print ('Target could not be resolved 007. Exiting')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

# Checking time again
t2 = datetime.now()

# Calculates the different of time, to see how long it took to run the script
total = t2 - t1

# Printing the information to screen
print ('Scanning Completed in: ', total)
