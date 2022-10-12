import socket


def client_process(address, port):
    msgFromClient = "Hello UDP Server"
    bytesToSend = str.encode(msgFromClient)
    serverAddressPort = (address, port)
    bufferSize = 1024

    # Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    while(True):
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
        print(msg)


if __name__ == "__main__":
    client_process("127.0.0.1", 20001)
