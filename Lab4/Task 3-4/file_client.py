import socket
import os

HOST = '127.0.0.1'
PORT = 65433


def send_file():
    filename = 'my_data.txt'
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found!")
        return

    print(f"Sending {filename} to server...")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        with open(filename, 'rb') as f:
            data = f.read()
            s.sendall(data)

    print("File sent successfully.")


if __name__ == '__main__':
    send_file()