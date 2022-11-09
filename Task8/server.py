import socket
import select

class MSG:
    passwd = "abcd"
    wrong_pswd = 'wrong password'
    correct_pswd = 'correct password'
    enter_pswd = 'please enter password'

class Client:
    def __init__(self, _connection, _id, _authenticated=False, _name="Noname"):
        self.connection = _connection
        self.id = _id
        self.authenticated = _authenticated
        self.name = 'User' + str(_id) if _authenticated else 'Noname' + str(_id)

    def authent(self, data):
        decoded_data = data.decode()
        if str(decoded_data) == MSG.passwd:
            self.authenticated = True
            self.name = 'User' + str(self.id)
            self.connection.send(MSG.correct_pswd.encode())
            print("Client", self.id, " was added")
        else:
            self.connection.send(MSG.wrong_pswd.encode())
            self.connection.send(MSG.enter_pswd.encode())


def main():
    Connections = []
    Clients = []
    sock = socket.socket()
    sock.bind(('', 4040))
    sock.listen(1)
    count = 0
    data_buffer = b""
    while True:
        readable = select.select(Connections+[sock], [], [])[0]
        for s in readable:
            if s is sock:
                conn, addr = sock.accept()
                count += 1
                Clients.append(Client(conn, count, False))
                Connections.append(conn)
                conn.send(MSG.enter_pswd.encode())
            else:
                for client in Clients:
                    if client.connection == s:
                        try:
                            input_data = s.recv(1024)
                        except ConnectionResetError:
                            print('Client has disconected')
                            Connections.remove(client.connection)
                            Clients.remove(client)
                            continue
                        data_buffer += input_data
                        parts = data_buffer.split(b"\n")
                        for data in parts[:-1]:
                            if client.authenticated:
                                print(client.name, ': ', data.decode())
                                s = client.name + ': ' + str(data.decode())
                                for other_client in Clients:
                                    if other_client.authenticated and other_client.id != client.id:
                                        other_client.connection.send(s.encode())
                            else:
                                print(client.name, ': ', data.decode())
                                client.authent(data)
                        data_buffer = parts[-1]
                        break


if __name__ == '__main__':
    print('server started')
    main()
