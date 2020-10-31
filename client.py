# load additional Python modules
import socket
import time

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = '127.0.0.1';

# get fully qualified hostname
local_fqdn = socket.getfqdn()

# get the according IP address
ip_address = socket.gethostbyname(local_hostname)

# bind the socket to the port 23456, and connect
server_address = (ip_address, 23456)
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))
while True:
	print('Message :')
	x = input()
	# define example data to be sent to the server
	new_data = str(x).encode("utf-8")
	sock.sendall(new_data)
    
    # wait for two seconds
time.sleep(2)

# close connection
sock.close()
