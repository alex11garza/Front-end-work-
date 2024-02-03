###############################################################################
# server-python.py
# Name: Juan Chavarria
# EID: jac23763
###############################################################################

import sys
import threading
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    main_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_soc.bind(('', server_port))
    main_soc.listen(QUEUE_LENGTH)

    while True:
        conn, addr = main_soc.accept()
        t = threading.Thread(target = thread_process, args = (conn,))
        t.start()
    
    main_soc.close()

def thread_process(conn):
    msg = conn.recv(RECV_BUFFER_SIZE).decode()
    sys.stdout.write(msg)
    conn.close()


def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
