Judul : Sistem Manajemen Parkir Kendaraan Berbasis Array

Program ini berfungsi sebagai simulator pengelolaan slot parkir kendaraan secara terotomatisasi untuk kapasitas yang terbatas. Melalui sistem ini, pengguna/user dapat mendaftarkan kendaraan masuk ke slot yang kosong, menghapus data kendaraan yang keluar berdasarkan nomor plat, serta memantau status seluruh slot parkir secara real-time. Program ini membantu memastikan pengisian lahan parkir dilakukan secara urut dan meminimalisir kesalahan input data manual.

Program ini menerapkan struktur data Array (List) statis dengan ukuran tetap untuk merepresentasikan lahan parkir. Algoritma yang digunakan adalah Linear Search (O(n)), yang diimplementasikan saat mencari slot pertama yang bernilai None untuk pengisian kendaraan, serta saat memvalidasi keberadaan nomor plat di dalam daftar untuk proses pengeluaran kendaraan. Pengolahan data dilakukan melalui teknik Indexing untuk mengakses dan mengubah status slot secara efisien.


<img width="841" height="305" alt="Screenshot 2026-04-22 153206" src="https://github.com/user-attachments/assets/3ef13ad7-0df1-4a59-b2da-4a206db455bc" />
<img width="889" height="249" alt="Screenshot 2026-04-22 153222" src="https://github.com/user-attachments/assets/a40fa097-b6e4-43d6-b993-cc44aebfc123" />
<img width="830" height="304" alt="Screenshot 2026-04-22 153241" src="https://github.com/user-attachments/assets/02491bf4-1447-4c27-b842-9d042ba1618a" />
<img width="845" height="171" alt="Screenshot 2026-04-22 153258" src="https://github.com/user-attachments/assets/0a5a8fc8-d057-4042-824e-13822695b8d1" />

FUNGSI MENU

def menu():  
Mendefinisikan fungsi bernama menu yang tidak menerima argumen.

print("=== Sistem Parkir Pintar ===")  
Menampilkan judul sistem ke layar.

print("1. Masukkan kendaraan ke slot parkir")  
Opsi 1 ditampilkan untuk memasukkan kendaraan.

print("2. Keluarkan kendaraan dari slot parkir")  
Opsi 2 ditampilkan untuk mengeluarkan kendaraan.

print("3. Tampilkan kondisi parkir")  
Opsi 3 ditampilkan untuk melihat kondisi semua slot.

print("4. Keluar")  
Opsi 4 ditampilkan untuk menghentikan program.


FUNGSI UTAMA

def main():  
Mendefinisikan fungsi utama program.

slots = [None] * 5 # untuk contoh buat 5 slot parkir  
Membuat list slots berisi 5 elemen None, mewakili 5 slot kosong.

running = True  
Flag kontrol untuk loop utama; selama True program terus berjalan.

while running:  
Loop utama yang terus mengulang sampai running diubah menjadi False.


LOOP UTAMA , DAN MEMINTA INPUT DARI USER

menu()  
Memanggil fungsi menu untuk menampilkan pilihan setiap iterasi.

try:  
Memulai blok penanganan error untuk input pengguna.

choice = int(input("Pilihan: "))  
Membaca input pengguna, mengonversi ke int; jika bukan angka akan memicu ValueError.

except ValueError:  
Menangkap kesalahan bila input bukan angka.

print("Masukkan angka yang valid!")  
Memberi tahu pengguna bahwa input tidak valid.

continue  
Melompat ke iterasi berikutnya dari loop tanpa mengeksekusi sisa blok saat input salah.


PERCABANGAN PERTAMA (menambahkan kendaraan)

if choice == 1:  
Cabang untuk opsi 1 yaitu memasukkan kendaraan.

kosong = []  
Membuat list kosong untuk menyimpan indeks slot yang kosong.

for i, val in enumerate(slots):  
Iterasi melalui setiap slot dengan indeks i dan nilai val.

if val is None:  
Cek apakah slot kosong (nilai None berarti kosong).

kosong.append(i)  
Tambahkan indeks kosong ke list kosong.

if len(kosong) == 0:  
Jika tidak ada indeks kosong berarti parkir penuh.

print("Parkir penuh!")  
menampilkan pesan bahwa tidak ada slot tersedia.

else:  
Jika ada slot kosong, lanjutkan proses parkir.

plat = input("Masukkan nomor plat kendaraan: ")  
Minta input nomor plat dari pengguna.

slot = kosong[0] # isi slot kosong pertama  
Pilih slot kosong pertama dari daftar kosong.

slots[slot] = plat  
Isi slot dengan nomor plat yang dimasukkan.

print(f"Kendaraan {plat} diparkir di slot {slot+1}") # tampilkan mulai dari 1  
Konfirmasi ke pengguna bahwa kendaraan diparkir; slot+1 agar nomor slot tampil mulai dari 1 bukan indeks 0. jadi slot parkir mulai dari 1 bukan dari slot 0


PERVABANGAN KEDUA (mengeluarkan kendaraan)

elif choice == 2:  
Cabang untuk opsi 2 — mengeluarkan kendaraan.

plat = input("Masukkan nomor plat kendaraan yang keluar: ")  
Minta nomor plat kendaraan yang akan keluar.

if plat in slots:  
Cek apakah plat ada di list slots.

slot = slots.index(plat)  
Dapatkan indeks slot tempat kendaraan berada (metode index mengembalikan indeks pertama yang cocok).

slots[slot] = None  
Kosongkan slot dengan mengatur kembali ke None.

print(f"Kendaraan {plat} keluar dari slot {slot+1}")  
menampilkan konfirmasi bahwa kendaraan keluar dari slot tersebut.

else:  
Jika plat tidak ditemukan di parkiran.

print("Kendaraan tidak ditemukan di parkiran.")  
memberitahu pengguna bahwa plat tidak ada di daftar.


PERCABANGAN KETIGA (menampilkan kondisi parkir)

elif choice == 3:  
Cabang untuk opsi 3 — menampilkan kondisi semua slot.

print("=== Kondisi Parkir ===")  
Header untuk kondisi.

for i in range(5):  
Iterasi indeks 0 sampai 4 untuk menampilkan setiap slot.

if slots[i] is None:  
Cek apakah slot kosong.

print(f"Slot {i+1}: kosong")  
menampilkan status kosong untuk slot tersebut.

else:  
Jika slot terisi.

print(f"Slot {i+1}: {slots[i]}")  
menampilkan nomor plat yang menempati slot.


PERCABANGAN KE EMPAT (kelaur sistem)

elif choice == 4:  
Cabang untuk opsi 4  keluar dari program.

running = False  
Set flag sehingga loop utama berhenti.

print("Program selesai.")  
menampilkan pesan bahwa program berakhir.

else:  
Jika input angka tetapi bukan 1 sampai 4.

print("Pilihan tidak valid!")  
memberitahu pengguna bahwa pilihan tidak dikenali.

Eksekusi langsung saat dijalankan sebagai skrip
if __name__ == "__main__":  
Cek apakah file dijalankan langsung (bukan diimpor sebagai modul).

main()  
Panggil fungsi main untuk memulai program.

<img width="899" height="337" alt="Screenshot 2026-04-22 174249" src="https://github.com/user-attachments/assets/16ce1010-2f34-4f62-b1c4-ed10097ea869" />
<img width="895" height="339" alt="Screenshot 2026-04-22 174318" src="https://github.com/user-attachments/assets/4f37969f-62bf-4faf-a10e-8ab990186400" />
<img width="899" height="126" alt="Screenshot 2026-04-22 174347" src="https://github.com/user-attachments/assets/84d9fe62-4d72-4118-8c9a-645a31ebc4d3" />

OUTPUT
akan menampilkan pilihan menu, dan user diminta untuk memilih pilihan mennu

 pilih pilihan 1 pada menu
 
lalu akan menampilkan "Masukkan nomor plat kendaraan:" dan user harus memasukka nomor platnya
contoh kita pakai RI 1 
lalu akan menambahkan RI 1 ke slot parkir yang masih koosng

 pilih pilihan 3 pada menu
 
maka akan menampilkan kondid slot parkiran
seperti ini:

=== Kondisi Parkir ===

Slot 1: RI 1

Slot 2: kosong

Slot 3: kosong

Slot 4: kosong

Slot 5: kosong

 pilih pilihan 2 pada menu
 
maka akan menampilkan inputan nomor plat yang akan di hapus

contoh : RI !
maka akan menghapus RI 1 dari slot parkir

 pilih pilihan 3 pada menu
 
 maka akan meanmpilkan slot yang ada apa parkiran setelah RI 1 di hapus
 seperti ini:
 
 === Kondisi Parkir ===
 
Slot 1: kosong

Slot 2: kosong

Slot 3: kosong

Slot 4: kosong

Slot 5: kosong

pilih pilihan 4 pada menu 

maka akan keluar dari sistem/progran
dan menampilkan "Program selesai"

LINK YOUTUBE : https://youtu.be/J9XSPGTCQMM









