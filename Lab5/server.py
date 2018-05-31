import multiprocessing
import socket

import functions as f


def functions(logger,connection, data):
    if data == "":
        logger.debug("Socket closed remotely")
        return -1
    if data == " ":
        connection.send("Write a command! Do you need '/help'?".encode())

    elif data == "/help":
        connection.send(f.help_me())

    elif data.split(' ')[0] == "/hello":
        try:
            temp = data.split(' ')[1:]
            connection.send(f.hello(temp))
        except:
            connection.send("Please put proper parameters. (ex: /hello text)".encode())

    elif data.split(' ')[0] == "/prime":
        try:
            temp = data.split(' ')[1]
            connection.send(f.is_prime(temp))
        except:
            connection.send("Please put a proper parameter. (ex: /prime 256)".encode())

    elif data.split(' ')[0] == "/area":
        try:
            x = data.split(' ')[1]
            y = data.split(' ')[2]
            connection.send(f.rect_area(x, y))
        except:
            connection.send("Please put proper parameters. (ex: /area 32 79)".encode())
    elif data == "/answer":
        connection.send(f.answer())

    elif data == "/joke":
        connection.send(f.joke())

    elif data == "/exit":
        connection.send("Closing connection...\n".encode())
        return -1

    else:
        connection.send("Unknown command [\"%s\"]. Type [\"/help\"]!".encode() % (data.encode()))


def handle(connection, address):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" % (address,))
    try:
        logger.debug("Connected %r at %r", connection, address)
        while True:
            data = connection.recv(1024).decode()
            if functions(logger,connection, data) == -1:
                break
            logger.debug("Received data %r", data)
            # connection.send(data.encode())

    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing socket")
        connection.close()


class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            self.logger.debug("Got connection")
            process = multiprocessing.Process(target=handle, args=(conn, address))
            process.daemon = True
            process.start()
            self.logger.debug("Started process %r", process)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9000)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in multiprocessing.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")
