import socket


def client_send(host, port, msg):
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    sock.sendall(msg.encode())
    sock.close()


client_send('localhost', 10000, "Hello, world!")