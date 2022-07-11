import socket


def main():
    host = '127.0.0.1' 
    port = 50000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()
    print("Connection from {}".format(addr))
    
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break 
        print("From : {}".format(data))
        data = data.upper()
        print("Sending data {} to client...".format(data))
        c.send(data.encode('utf-8'))
    c.close()


if __name__ == '__main__':
    main()