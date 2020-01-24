import socket

# Every function or method is created by the keyword def 
# Following the keyword def is the name of the method
def main():



	# First we need to create a socket obect
	sock = socket.socket()
	sock2 = socket.socket()
	sock3 = socket.socket()
	sock4 = socket.socket()

	# We then get the local hosts name. This would be the remote servers IP if we were not on the local host already
	host = socket.gethostname()

	# We now set the port we will be using
	port = 22
	port2 = 80
	port3= 443
	port4= 21


	# Now we issue a connection to the server
	sock.connect((host, port))
	sock2.connect((host,port2))
	sock3.connect((host, port3))
	sock4.connect((host,port4))


	# Now we recieve the data sent to use
	print('Data Recieved: {0}'.format(sock.recv(1024)))
	print('Data Recieved: {0}'.format(sock2.recv(1024)))
	print('Data Recieved: {0}'.format(sock3.recv(1024)))
	print('Data Recieved: {0}'.format(sock4.recv(1024)))

	# Close the socked connection
	sock.close()
	sock2.close()
	sock3.close()
	sock3.close()



# When running a .py file that specific file willl create a special variable called __name__
# It will set  __name__ to the value __main__ to let the code know this is the file used to 
# Run the python script
if __name__ == '__main__':

	# This will call a function main() that we created above this
	main()