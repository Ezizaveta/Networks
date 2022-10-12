import socket


def server_process(address, port):
    bufferSize = 1000000
    msgFromServer = "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((address, port))
    print("UDP server up and listening")

    # Listen for incoming datagrams
    done = False
    while not done:
        message, address = UDPServerSocket.recvfrom(bufferSize)
        clientIP = "Client IP Address:{}".format(address)
        print(clientIP)
        c = 0
        while(c < 1000):
            UDPServerSocket.sendto(bytesToSend, address)
            c += 1
            if (c == 100):
                done = True


if __name__ == "__main__":
    server_process("127.0.0.1", 20001)