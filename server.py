import asyncore, socket

class Handler(asyncore.dispatcher):
	def handle_read(self):
		data = self.recv(1024)
		if not data:
			return

		print('Received:', data.decode())

	def handle_close(self):
		print('Server: Connection Closed')
		self.close()

class Server(asyncore.dispatcher):
	def __init__(self, host, port):
		self.HANDLER = Handler
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind((host, port))
		self.listen(5)
		print('Waiting for connection...')
		self.connections = []

	def handle_accept(self):
		(sock, addr) = self.accept()
		self.connections.append(socket)
		print('Connection by ', addr)
		sock.send(b'Hello Server')
		self.HANDLER(sock)

	def serve(Self):
		asyncore.loop()

s = Server('0.0.0.0', 5037)
s.serve()