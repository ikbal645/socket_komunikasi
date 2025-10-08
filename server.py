import socket

HOST = '127.0.0.1' 
PORT = 65432        

print("--- PROGRAM SERVER DIMULAI ---")

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        print(f" Socket berhasil diikat ke {HOST}:{PORT}")
        s.listen() # Hapus batasan 1
        print("Server sedang mendengarkan koneksi dari client (Running Forever)...")
        
        # Tambahkan perulangan tak terbatas untuk menerima banyak koneksi
        while True:
            # Server akan terblokir di sini, menunggu koneksi
            conn, addr = s.accept()
            with conn:
                print(f"\n KONEKSI BARU: Terhubung oleh {addr}")
                
                data = conn.recv(1024) 
                
                if data:
                    pesan_diterima = data.decode('utf-8')
                    print(f"Pesan Diterima: >>> {pesan_diterima}")
                    
                    pesan_balasan = f"Server menerima pesan Anda: '{pesan_diterima[:20]}...' [CONFIRMED]"
                    conn.sendall(pesan_balasan.encode('utf-8'))
                    print(" Mengirim balasan konfirmasi.")
                    
except Exception as e:
    print(f" Terjadi kesalahan pada Server: {e}")
# Hapus finally: program tidak akan selesai kecuali dihentikan paksa (Ctrl+C)