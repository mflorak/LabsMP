import socket

HOST = '127.0.0.1'
PORT = 65433


def start_file_server():
    print(f"File Server listening on {HOST}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection from {addr}. Receiving file...")

                with open('received_file.txt', 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print("File received and saved as 'received_file.txt'")


if __name__ == '__main__':
    start_file_server()