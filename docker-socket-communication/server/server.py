# server/server.py
import socket

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345      # Port to listen on

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received from client: {data.decode()}")
                conn.sendall(b"Hello from Server!")

if __name__ == "__main__":
    start_server()
