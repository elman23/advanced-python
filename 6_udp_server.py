import socket


def main():
    host = '127.0.0.1'
    port = 50000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print("Server started!")

    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print("Received from {}: {}".format(str(addr), data))
        data = data.upper()
        print("Sending {} to {}".format(data, str(addr)))
        s.sendto(data.encode('utf-8'), addr)
    s.close()


if __name__ == '__main__':
    main()