import socket


def server_process(host, port):
    server_address = (host, port)
    print(server_address)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)

    while True:

        connection, client_address = sock.accept()

        try:
            data = connection.recv(16)
            print(data)

        except:
            print("Getting data error")
            break

        finally:
            connection.close()


server_process('localhost', 10000)