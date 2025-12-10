import socket

HOST = '127.0.0.1'
PORT = 65432


def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        message = "Hello, Lab 4! Testing TCP connection."
        print(f"Sending: {message}")
        s.sendall(message.encode('utf-8'))

        data = s.recv(1024)
        print(f"Received back: {data.decode('utf-8')}")


if __name__ == '__main__':
    start_client()