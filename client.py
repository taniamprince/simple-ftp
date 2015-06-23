#!/usr/bin/python3

import sys
import socket

# Get command line arguments
if len(sys.argv) == 4:
   host = sys.argv[1]
   port = sys.argv[2]
   name = sys.argv[3]
else:
   print("Error: Expected 4 arguments")
   print("Usage: clienty.py <remote-IP> <remote-port> <local-file-to-transfer>")
   exit()

# Open file for reading
try:
   in_file = open(name, "rb")
except IOError:
   print("Error: File not found")
   exit()

# Open socket
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
   print("Error: Could not open socket")
   exit()

# Connect to remote host
try:
   s.connect((host, int(port)))
   print("Connected to", host, "port", port)
except socket.error:
   print("Error: Connection failed")
   exit()

# Send the name of the file
print("Sending...")
s.send(name.encode('utf-8'))

# Send the file data
data = in_file.read(1024)
s.send(data)
while True:
   if not data: break
   data = in_file.read(1024)
   s.send(data)

# Shutdown and close socket
print("File successfully sent")
s.shutdown(socket.SHUT_WR)
s.close()

# Close file
in_file.close()

# Exit program
exit()
