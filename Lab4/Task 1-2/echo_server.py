import socket

HOST = '127.0.0.1'
PORT = 65432

def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Echo Server listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode('utf-8')}")
                    conn.sendall(data)

if __name__ == '__main__':
    start_server()