import socket


def start_client(address, port, buffer):
    # We're using TCP/IP as transport
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to the given address and port
    client_socket.connect((address, port))
    print("=== Initiating connection to %s:%s" % (address, port))
    data = bytes("something", 'utf-8')
    while data != bytes("close", 'utf-8'):
        print("=== Connecting to %s" % (address,))
        # Recv up to 1kB of data
        data = bytes(input(), 'utf-8')

        client_socket.send(data)
        result = client_socket.recv(buffer)
        print(">>> Sent data %s" % (result,))
        # Send `data` to the client
        # Close outgoing connection
        client_socket.close()


if __name__ == '__main__':
    start_client('localhost', 9000, 4048)
