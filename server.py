#!/usr/bin/python3

import sys
import socket

# Get command line argument
if len(sys.argv) == 2:
   port = sys.argv[1]
else:
   print("Error: Expected 2 arguments")
   print("Usage: server.py <local-port>")
   exit()

# Open socket
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
   print("Error: Cannot open socket")
   print(error)
   exit()

# Get hostname
try:
   host = socket.gethostbyname(socket.gethostname())
except socket.error as error:
   print("Error: Failed to get hostname of server")
   print(error)
   exit()

# Bind socket
try:
   s.bind((host, int(port)))
except socket.error as error:
   print("Error: Cannot bind socket")
   print(error)
   exit()

# Listen for connections
s.listen(1)

# Display server information
print ("Server running on", host, "port", port)

while True:

   # Accept connection
   conn, addr = s.accept()
   print ("Connected by", addr)

   # Get file name
   name = conn.recv(20)
   print("Incoming file", name)
   print("Receiving...")

   # Create new file
   in_file = open(name, 'wb')

   # Write data to file
   while True:
      data = conn.recv(1024)
      if not data: break
      in_file.write(data)

   print("File successfully received")

   # Close file
   in_file.close()

   # Close connection
   conn.close()
