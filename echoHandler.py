class EchoHandler(asyncore.dispatcher_with_send):
    def __init__(self, sock, server):
        self.server = server

    def handle_read(self):
        datos = self.recv(1024);
        if datos:
            print(datos);
            self.out_buffer += 'I echo you: ' + datos

    def handle_close(self):
        self.server.remove_channel(self)
        self.close()