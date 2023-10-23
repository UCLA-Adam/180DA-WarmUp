import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assigns a port for the server that listens to clients connecting to this port.
host='0.0.0.0'
port=8080
serv.bind((host, port))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = ''
	while True:
		data = conn.recv(4096)
		if not data: break
		from_client += data.decode('utf_8')
		print(from_client)
		conn.send("I am SERVER\n".encode())
conn.close()
print('client disconnected')
