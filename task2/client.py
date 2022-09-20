import socket


def client_send(host, port, msg):
    server_address = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    try:
        sock.sendall(msg.encode())
        data = sock.recv(255)
        print(data.decode())
    except:
        print("Can't send/receive data")
    sock.close()




client_send('localhost', 10001, "Hello, world!\n Hola!")