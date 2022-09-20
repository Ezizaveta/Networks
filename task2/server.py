import socket


def reverse_string(str):
    reversed_string = str[::-1]
    return reversed_string


def server_process(host, port):
    server_address = (host, port)
    print(server_address)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)
    done = False
    while not done:

        connection, client_address = sock.accept()

        try:
            data = connection.recv(255)
            if data:
                print(data)
                msg = reverse_string(data.decode())
                connection.sendall(msg.encode())
                done = True
        except:
            print("Getting data error")
            break

        if done: connection.close()


server_process('localhost', 10001)
