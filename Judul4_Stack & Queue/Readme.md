Judul : Sistem Undo Redo pada Teks Editor Berbasis Stack Array

Program ini berfungsi sebagai simulator pengelolaan riwayat aksi pada sebuah teks editor secara terstruktur dan efisien. Lewat sistem ini, user/pengguna bisa menambahkan aksi atau perubahan teks, melakukan undo untuk membatalkan aksi terakhir, melakukan redo untuk mengembalikan aksi yang telah dibatalkan, serta melihat seluruh riwayat aksi yang tersimpan. Program ini membantu mempermudah pengelolaan perubahan data dan meminimalisir kesalahan yang fatal saat melakukan pengeditan teks.

Program ini menggunakan struktur data Stack Array untuk menyimpan riwayat aksi user/penggunanya. Konsep yang digunakan adalah LIFO (Last In First Out), yaitu data yang paling terakhir masuk akan menjadi data yang pertama kali keluar. Proses undo dilakukan dengan cara mengambil aksi terakhir dari stack history dan memindahkannya ke stack redo , sedangkan proses redo dilakukan dengan mengembalikan aksi dari stack redo ke stack history, jadi akan ada 2 stack pada sistem ini. Dengan penggunaan stack array, proses penyimpanan dan pengelolaan riwayat aksinya akan menjadi lebih teratur dan efisien.

___
<img width="919" height="409" alt="Screenshot 2026-05-14 190423" src="https://github.com/user-attachments/assets/52c1b456-2672-4827-a6c0-aece58b5f650" />
<img width="912" height="403" alt="Screenshot 2026-05-14 190447" src="https://github.com/user-attachments/assets/b7e5d29c-e653-4dbf-bf83-8927280152d7" />
<img width="925" height="412" alt="Screenshot 2026-05-14 190515" src="https://github.com/user-attachments/assets/c2ae5fa5-6543-45ed-a8ac-c5cbf394fe07" />
<img width="927" height="417" alt="Screenshot 2026-05-14 190536" src="https://github.com/user-attachments/assets/145b1da2-409a-4c0a-9523-3498058f0220" />
<img width="926" height="69" alt="Screenshot 2026-05-14 190549" src="https://github.com/user-attachments/assets/becfb820-72d6-4037-ab22-829c415b16e5" />
___

CLASS DAN METHOD

class StackArray:
Membuat class bernama stackarray.

def __init__(self, max_size=100):
Method constructor yang otomatis dijalankan saat object dibuat , dengan kapasitas maksimal 100 data.

self.MAX = max_size
Menyimpan ukuran maksimal stack ke variabel MAX.

self.st = [None] * self.MAX
Membuat array dengan isi awal None sebanyak kapasitas stacknya.

self.top_idx = -1
Variabel penunjuk posisi elemen paling atas stack, -1 berarti stack masih kosong.

def is_empty(self):
Method untuk mengecek apakah stack kosong.

return self.top_idx == -1
Kalau top_idx = -1, maka stack kosong.


def is_full(self):
Method untuk mengecek apakah stack penuh.

return self.top_idx == self.MAX - 1
Jika posisi top sudah ada di indeks terakhir array, maka stack penuh.

def push(self, x):
Method untuk menambahkan data ke stack.

if self.is_full():
Mengecek apakah stack penuh.

print("Stack penuh")

return
Jika penuh , tampilkan pesan Stack penuh lalu keluar dari fungsi.

self.top_idx += 1
Menaikkan posisi top satu langkah.

self.st[self.top_idx] = x
Menyimpan data ke posisi top.


def pop(self):
Method untuk mengambil atau menghapus data paling atas stack.

if self.is_empty():
Mengecek apakah stack kosong.

return None
Jika kosong, mengembalikan None.

data = self.st[self.top_idx]
Mengambil data paling atas dan menyimpannya ke variabel data.

self.top_idx -= 1
Menurunkan posisi top satu langkah kebawah.

return data
Mengembalikan data yang tadi diambil.

def display(self):
Method untuk menampilkan isi stack.

if self.is_empty():
Mengecek apakah stack kosong.

print("Kosong")

return
Jika kosong tampilkan Kosong .

for i in range(self.top_idx, -1, -1):
Melakukan perulangan dari indeks paling atas ke bawah.

print(self.st[i], end=" | ")
Menampilkan isi stack per elemen.

print()
Pindah baris setelah selesai.

___

FUNGSI UTAMA PROGRAM

def main():
Mendefinisikan fungsi bernama main, sebagai ungsi utama program.

history = StackArray()
Membuat stack untuk menyimpan riwayat aksi.

redo_stack = StackArray()
Membuat stack khusus redo.

pilih = 0
Menginisialisasi variabel pilih dengan nilai awal 0.

while pilih != 6:
Program akan terus mengulang selama pilih tidak sama dengan 6.

print("\n=== MENU UNDO / REDO ===")

print("1. Tambah Aksi")

print("2. Undo")

print("3. Redo")

print("4. Lihat History")

print("5. Lihat Redo")

print("6. Keluar")
Menampilkan daftar menu.

___
try:
Untuk menangani error input.

pilih = int(input("Pilih menu: "))
Meminta user memasukkan angka untuk memilih menu.

except ValueError:
Jika user memasukkan selain angka.

print("Input harus angka")

continue
Menampilkan pesan Input harus angka lalu kembali ke menu.

___
CONDITIONAL STATEMENT

menu tambah aksi

if pilih == 1:
Jika user memilih menu 1.

aksi = input("Masukkan aksi: ")
Meminta Input aksi dari user.

history.push(aksi)
Menyimpan aksi ke stack history.

redo_stack = StackArray()
Mengosongkan redo stack.

print(f"Aksi '{aksi}' berhasil ditambahkan")
Menampilkan pesan berhasil.

___

menu undo

elif pilih == 2:
Jika user memilih 2.

aksi = history.pop()
Mengambil aksi terakhir dari history.

if aksi is None:
Jika history kosong.

print("Tidak ada aksi untuk di-undo")
Menampilkan pesan Tidak ada aksi untuk di-undo.

else:
Jika ada aksi

redo_stack.push(aksi)
simpan aksi ke redo stack.

print(f"Undo aksi: {aksi}")
Menampilkan aksi yang di-undo.

___

menu redo

elif pilih == 3:
Jika user memilih 3.

aksi = redo_stack.pop()
Mengambil aksi dari redo stack.

if aksi is None:
Jika redo stack kosong.

print("Tidak ada aksi untuk di-redo")
Menampilkan pesan Tidak ada aksi untuk di-redo.

else:
Jika ada aksi 

history.push(aksi)
kembalikan aksi ke history.

print(f"Redo aksi: {aksi}")
kembalikan ke history.

___

menu lihat history

elif pilih == 4:
Jika user memilih 4.

print("\nHistory Aksi:")

history.display()
Menampilkan seluruh history stack.

___

menu lihat redo

elif pilih == 5:
Jika user memilih 5.

print("\nRedo Stack:")

redo_stack.display()
Menampilkan isi redo stack.

___

menu keluar

elif pilih == 6:
jika user memilih 6.

print("Program selesai")
Menampilkan pesan program selesai.

else:
jika tidak

print("Pilihan tidak valid")
Menampilkan pilihan tidak valid


if __name__ == "__main__":
main()
Menjalankan fungsi utama program.

___

<img width="901" height="438" alt="Screenshot 2026-05-14 190045" src="https://github.com/user-attachments/assets/4729bcea-2a3e-4cdf-b916-f3452854f18e" />
<img width="926" height="283" alt="Screenshot 2026-05-14 190110" src="https://github.com/user-attachments/assets/b091479b-6602-424b-8925-e33437993abe" />
<img width="920" height="289" alt="Screenshot 2026-05-14 190131" src="https://github.com/user-attachments/assets/dbb67f41-0320-4371-8c67-c6b17a6d5781" />
<img width="921" height="306" alt="Screenshot 2026-05-14 190144" src="https://github.com/user-attachments/assets/96c9ee13-e7d5-4607-b567-c811589f548a" />

___

penjelasan output


=== MENU UNDO / REDO ===

1. Tambah Aksi

2. Undo

3. Redo

4. Lihat History

5. Lihat Redo

6. Keluar

Pilih menu: 1
user memilih 1


Masukkan aksi: print hello
User menginputkan print hallo

Pilih menu: 1
Memilih tambah aksi lagi.

Masukkan aksi: tambah titik dua
User menginputkan tambah titik dua

Pilih menu: 1
tambah aksi lagi.

Masukkan aksi: print ini benar
User menginputkan print ini benar

ketiga aksi ini ditambahkan ke stack history

lalu user memilih menu 4 , maka akan menampilkan . print ini benar | tambah titik dua | print hello |

lalu user memilih 2 , maka akan undo , elemen teratas dalam history akan di pindahka keredo stack

lalu user memillih 4 , maka akan menampilkan history sekarang. print ini benar | tambah titik dua | print hello |

lalu user memilih 3 , maka akan redo , elemen terakhir yang dipindahkan ke redo akan di pindahkan kembali ke stack history

lalu user memilih 4 , maka akan menampikan history sekarang yang sudah ditambahkan kembali dari redo, yaitu print ini benar | tambah titik dua | print hello |

lalu user memilih 6 , makan akan keluar dari program

___
video : https://youtu.be/nN-A8dv9Z8M


