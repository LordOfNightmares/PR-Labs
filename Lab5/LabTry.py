import socket


def start_server(address, port, max_connections=5):
    # We're using TCP/IP as transport
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to the given address and port
    server_socket.bind((address, port))
    # Listen for incoming connection (with max connections)
    server_socket.listen(max_connections)
    print("=== Listening for connections at %s:%s" % (address, port))
    data = bytes("nothing", 'utf-8')
    while data != bytes("close", 'utf-8'):
        # Accept an incomming connection
        # Note: this is blocking and synchronous processing of incoming connection
        incoming_socket, address = server_socket.accept()
        print("=== New connection from %s" % (address,))
        # Recv up to 1kB of data
        data = incoming_socket.recv(4048)
        print(">>> Received data %s" % (data,))
        # Send `data` to the client
        incoming_socket.send(data)
        # Close incoming connection
        incoming_socket.close()


if __name__ == '__main__':
    start_server('127.0.0.1', 9000)
