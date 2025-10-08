import socket

# Konfigurasi Server yang akan dihubungi
HOST = '127.0.0.1'  # Harus sama dengan HOST di Server
PORT = 65432        # Harus sama dengan PORT di Server

# Pesan yang akan dikirim ke Server
pesan_untuk_server = "Selamat siang, Server! Saya ingin menguji koneksi socket client-server TCP ini. Apakah Anda sudah siap?"

print("--- PROGRAM CLIENT DIMULAI ---")

try:
    # 1. Membuat objek socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 2. Terhubung ke server
        s.connect((HOST, PORT))
        print(f" Berhasil terhubung ke Server di {HOST}:{PORT}")
        
        # 3. Mengirimkan pesan teks ke server
        s.sendall(pesan_untuk_server.encode('utf-8'))
        print(f"Mengirim pesan: >>> {pesan_untuk_server}")
        
        # 4. Menerima balasan dari server
        data = s.recv(1024)
        
        if data:
            balasan_server = data.decode('utf-8')
            # 5. Menampilkan balasan dari server
            print(f"\nBalasan Diterima dari Server: >>> {balasan_server}")
        
except ConnectionRefusedError:
    print(f" GAGAL KONEKSI: Pastikan program Server berjalan di {HOST}:{PORT}.")
except Exception as e:
    print(f" Terjadi kesalahan pada Client: {e}")

finally:
    print("\n--- PROGRAM CLIENT SELESAI ---")