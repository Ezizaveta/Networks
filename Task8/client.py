import socket
import sys
import threading

def readConsole(sock):
    while True:
        inp = sys.stdin.readline(80)
        #print(repr(inp))
        sock.send(inp.encode())


def readSocket(sock):
    while True:
        data = sock.recv(1024)
        print(data.decode())


def main():
    sock = socket.socket()
    sock.connect(('localhost', 4040))
    console_threading = threading.Thread(target=readConsole, args=[sock])
    console_threading.start()
    socket_threading = threading.Thread(target=readSocket, args=[sock])
    socket_threading.start()
    console_threading.join()
    socket_threading.join()


if __name__ == '__main__':
    print('client started')
    main()