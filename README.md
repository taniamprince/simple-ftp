# Simple FTP

A simple TCP file transfer application.

## Dependencies

Python 3

## To run

1. Start the server on the machine to receive the file using the following command:

	```bash
python3 server.py <local-port>
```

	Use port number 3000+ to safely avoid conflicts with reserved ports.

2. Start the client on the machine you are sending the file from using the following command:

	```bash
python3 client.py <remote-IP> <remote-port> <local-file-to-transfer>
```

	Where

	```bash
<remote-IP> is the IP of the server
```

	```bash
<remote-port> is the local port of the server
```

	```bash
<local-file-to-transfer> is the local address of the file to send
```