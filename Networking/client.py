#!/usr/bin/python
import socket

# Create a Socket Object 
clientsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Get the Local Machine Name
host = socket.gethostname()
port = 55555


# Connection to the hostname on the Port
clientsock.connect((host,port))

print "Client has established Connection with the Server"

# Recieve no more than 1024 bytes
tm =clientsock.recv(1024)
print ("The Message recieved from the Server is below \n %s" %tm.decode('ascii'))

clientsock.close

print ("The Message recieved from the Server is below \n %s" %tm.decode('ascii'))
print tm
