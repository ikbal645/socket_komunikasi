import socket
import threading

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                print("[!] Server terputus.")
                sock.close()
                break
        except:
            print("[!] Gagal menerima pesan.")
            sock.close()
            break

def send_messages(sock):
    while True:
        try:
            message = input()
            sock.send(message.encode('utf-8'))
        except:
            print("[!] Gagal mengirim pesan.")
            sock.close()
            break

def start_client():
    host = '127.0.0.1'   # IP server (localhost)
    port = 5555          # Port harus sama dengan server

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((host, port))
        print(f"[+] Terhubung ke server {host}:{port}")
    except Exception as e:
        print(f"[X] Tidak bisa terhubung ke server! Error: {e}")
        return

    # Jalankan thread untuk kirim dan terima pesan
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    send_messages(client)

if __name__ == "__main__":
    start_client()
