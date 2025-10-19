import socket
import threading

# Menyimpan semua koneksi client
clients = []

# Broadcast pesan ke semua client
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                if client in clients:
                    clients.remove(client)

# Menangani pesan dari client
def handle_client(client_socket, address):
    print(f"[+] {address} terhubung.")
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"[{address}] {message.decode()}")
                broadcast(message, client_socket)
            else:
                raise Exception("Client disconnected")
        except:
            print(f"[-] {address} terputus.")
            client_socket.close()
            if client_socket in clients:
                clients.remove(client_socket)
            break

# Main function
def start_server(host='127.0.0.1', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()
    print(f"[*] Server berjalan di {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
