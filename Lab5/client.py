import socket


def start_client(address, port, buffer):
    # We're using TCP/IP as transport
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to the given address and port
    client_socket.connect((address, port))
    print("=== Initiating connection to %s:%s" % (address, port))
    while True:
        print("=== Connecting to %s" % (address,))
        # Recv up to 1kB of data
        data = input()
        client_socket.sendall(data.encode())
        result = client_socket.recv(buffer)
        print(">>> %s" % (result.decode(),))
        # Send `data` to the client
        # Close outgoing connection
        if data == '/close':
            print('You ended the connection manually.')
            break
    client_socket.close()


if __name__ == '__main__':
    start_client('localhost', 9000, 4048)
