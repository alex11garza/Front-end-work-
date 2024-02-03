###############################################################################
# client-python.py
# Name: Juan Chavarria
# EID: jac23763
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((server_ip,server_port))

    while True:
        #read_line = sys.stdin.read(SEND_BUFFER_SIZE)
        read_line = sys.stdin.read(SEND_BUFFER_SIZE)
        #print(sys.getsizeof(read_line.encode()), "LENGTH OF CHARS:", len(read_line))
        #print(read_line[-30:-1])
        #print(read_line)
        if read_line == "":    
            break
        clientSocket.send(read_line.encode())
        #clientSocket.send(read_line)
    clientSocket.close()


def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
