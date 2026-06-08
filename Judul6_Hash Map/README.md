Judul: Sistem Manajemen Data Mahasiswa

Program ini berfungsi sebagai sistem manajemen data mahasiswa yang digunakan untuk menyimpan, mencari, menghapus, dan menampilkan informasi mahasiswa secara terstruktur dan efisien. Melalui sistem ini, pengguna dapat menambahkan data mahasiswa baru, melakukan pencarian berdasarkan Nomor pokok Mahasiswa (NPM), menghapus data mahasiswa yang sudah tidak diperlukan, serta menampilkan seluruh data mahasiswa yang tersimpan dalam sistem. Program ini membantu mempermudah pengelolaan data mahasiswa dan mempercepat proses akses informasi tanpa harus melakukan pencarian secara berurutan pada seluruh data yang ada.

Program ini menggunakan struktur data Hash Map Open Addressing sebagai metode penyimpanan data. Setiap data mahasiswa disimpan ke dalam tabel hash berdasarkan nilai kunci (key), yaitu NPM mahasiswa, yang diproses menggunakan fungsi hash untuk menentukan lokasi penyimpanan. Untuk menangani terjadinya collision, program menerapkan metode Linear Probing, yaitu mencari slot berikutnya secara berurutan hingga ditemukan posisi yang kosong atau sesuai dengan data yang dicari. Dengan metode ini, proses penambahan, pencarian, penghapusan, dan penampilan data mahasiswa dapat dilakukan secara lebih cepat, efisien, dan terorganisir. Penggunaan Hash Map Open Addressing dengan Linear Probing juga membuat pemanfaatan memori menjadi lebih optimal karena seluruh data disimpan langsung di dalam tabel hash tanpa memerlukan struktur data tambahan.

___

<img width="899" height="360" alt="Screenshot 2026-06-08 181132" src="https://github.com/user-attachments/assets/2f634bf0-d850-4da3-afd7-df62945b49cd" />
<img width="917" height="387" alt="Screenshot 2026-06-08 181203" src="https://github.com/user-attachments/assets/8b32f14e-b535-4d9d-8fb6-40e7e3789811" />
<img width="917" height="316" alt="Screenshot 2026-06-08 181217" src="https://github.com/user-attachments/assets/9526e4c7-8f3b-458b-b740-59579c591784" />
<img width="914" height="343" alt="Screenshot 2026-06-08 181240" src="https://github.com/user-attachments/assets/ad4edc5d-6d81-4ba0-aac3-beb1c5f5c13f" />
<img width="915" height="413" alt="Screenshot 2026-06-08 181258" src="https://github.com/user-attachments/assets/6ff0c81e-b7cd-4eda-8491-b84328f1fd29" />
<img width="918" height="228" alt="Screenshot 2026-06-08 181312" src="https://github.com/user-attachments/assets/e4790010-b61e-4313-987d-12a7f8b9ab5c" />

___

PENJELASAN KODE


class SlotState:
Membuat kelas bernama SlotState yang digunakan untuk menyimpan status setiap slot pada hash table.

EMPTY = 0
Menandakan slot masih kosong dan belum pernah digunakan.

OCCUPIED = 1
Menandakan slot sedang berisi data.

DELETED = 2
Menandakan data pernah ada tetapi sudah dihapus.

class Entry:
Membuat kelas untuk menyimpan data pada setiap slot hash table.

def __init__(self):
Constructor yang akan dijalankan saat objek Entry dibuat.

self.key = None
Menyimpan key (NPM mahasiswa).

self.value = None
Menyimpan value (nama mahasiswa).

self.state = SlotState.EMPTY
Status awal slot adalah kosong.

_____

HASHMAP OPEN ADRESSING

class HashMapOpenAddressing:
Membuat kelas Hash Map menggunakan metode Open Addressing.

def __init__(self, size=10):
Membuat constructor dengan ukuran default hash table 10 slot.

self.SIZE = size
Menyimpan ukuran hash table.

self.table = [Entry() for _ in range(self.SIZE)]
Membuat list berisi objek Entry sebanyak SIZE.

____

def hash_function(self, key):
Membuat fungsi hash.

return (key % self.SIZE + self.SIZE) % self.SIZE
Funhsi hash menghasilkan indeks berdasarkan NPM.

____

def insert(self, key, value):
Membuat  fungsi bernama insert dengan parameter key dan value


idx = self.hash_function(key)
Menghitung indeks awal menggunakan fungsi hash.

first_deleted = -1
Menyimpan posisi slot yang berstatus DELETED jika ditemukan.

for step in range(self.SIZE):
Melakukan pencarian maksimal sebanyak ukuran tabel.

i = (idx + step) % self.SIZE
Rumus Linear probing.

if self.table[i].state == SlotState.OCCUPIED:
Memeriksa apakah slot sedang digunakan.

if self.table[i].key == key:
Jika key sudah ada.

self.table[i].value = value
update value

return True
kembalikan true

elif self.table[i].state == SlotState.DELETED:
Jika slot pernah digunakan tetapi sudah dihapus.

if first_deleted == -1:
Jika belum ada slot deleted yang ditemukan.

first_deleted = i
Simpan indeks deleted pertama.

else:
jika slot kosong

if first_deleted != -1:
Jika sebelumnya ditemukan slot DELETED.

i = first_deleted
Gunakan slot deleted tersebut.

self.table[i].key = key
menyimpan kunci

self.table[i].value = value
menyimpan value

self.table[i].state = SlotState.OCCUPIED
mengubah status menjadi terisi

return True
kembalkan true

return False
jika tabel penuh , return false

____

def search(self, key):
mmebuat fungsi bernama search untuk mencari data  dengan parameter keynya.

idx = self.hash_function(key)
Menghitung indeks awal menggunakan fungsi hash.

for step in range(self.SIZE):
Perulangan mencari maksimal sebanyak ukuran tabel.

i = (idx + step) % self.SIZE
rumus linear probling.

if self.table[i].state == SlotState.EMPTY:
Jika slot kondisi kosong 

return None
kembalikan none

if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
jika slot terisi dan nilai kuncinya sama

return self.table[i]
mengembalikan objek entrynya

return None
kembalikan none

_____

def remove_key(self, key):
membuat fungsi rmmove dengan parameter keynya/

entry = self.search(key)
mencari data dan memasukkan ke variable entry

if entry is None:
jika data tidak ditemukan

return False
kembalikan false

entry.state = SlotState.DELETED
Mengubah status menjadi DELETED.

return True
penhapusan berhasil , kembalikan true

____

def display(self):
membuat fungsi display unutk menamplkan data

print("\n===== DATA MAHASISWA =====")
menaampilkan ===== DATA MAHASISWA =====

for i in range(self.SIZE):
perulangan ke semua indeks

if self.table[i].state == SlotState.OCCUPIED:
jika slot berisi data

print(

f"NPM: {self.table[i].key} | Nama: {self.table[i].value}"
menampilkan npm dan nama.

)

____

def main():
membuat fungsi utama program

mahasiswa = HashMapOpenAddressing()
membuat obje hasmap

while True:
melakukan perulangan sampai false

print("\n===== MENU DATA MAHASISWA =====")

print("1. Tambah Mahasiswa")

print("2. Cari Mahasiswa")

print("3. Hapus Mahasiswa")

print("4. Tampilkan Semua Data")

print("5. Keluar")

pilihan = int(input("Pilih menu: "))
meminta input pilihan menu

if pilihan == 1:
jika pengguna memilih 1

npm = int(input("Masukkan NPM: "))
Meminta pengguna memasukkan NPM mahasiswa.

nama = input("Masukkan Nama: ")
Meminta pengguna memasukkan nama mahasiswa.

if mahasiswa.insert(npm, nama):
Memanggil fungsi insert untuk menyimpan data ke HashMap.

print("Data berhasil disimpan.")
menampilkan data berhasil disimpan.

else:
jika kondisi sebelumnya false

print("Hash Table penuh!")
menampilkan hash table penuh

elif pilihan == 2:
jika pengguna memilih dua 

npm = int(input("Masukkan NPM yang dicari: "))
Meminta pengguna memasukkan NPM mahasiswa dicari.

hasil = mahasiswa.search(npm)
menjalankan fungsi search dan menyimpannya di hasil

if hasil:
Memeriksa apakah data ditemukan.

print(f"Data ditemukan")
menampilkan data ditemukan

print(f"NPM  : {hasil.key}")
menampilkan npm

print(f"Nama : {hasil.value}")
menampilkan value atau nilainya

else:
jka kondiis sebelumnya false

print("Data tidak ditemukan.")
menampilka data tidak ditemukan


elif pilihan == 3:
jika pengguna memilih tiga

npm = int(input("Masukkan NPM yang akan dihapus: "))
meminta pengguna menginputkan npm yang ingin di hapus

if mahasiswa.remove_key(npm):
memanggil fungsi remove untuk dijalakan

print("Data berhasil dihapus.")
menampilkan data berhasil dsimpan

else:
jika kondisi sebelumnya false

print("Data tidak ditemukan.")
menampilkan data tidak di temukan


elif pilihan == 4:
jika pengguna memilih empat

mahasiswa.display()
memanggil fungsi display untuk menampilkan data

elif pilihan == 5:
jika pengguna memilih 5

print("Program selesai.")
keluar program , menampilkan program selesai

break

else:
jka pilihan tidak valid

print("Pilihan tidak valid.")
menampilkan pilihan tidak valid


if __name__ == "__main__":

main()
memanggil fungsi main untuk di jalankan

___

<img width="909" height="354" alt="Screenshot 2026-06-08 181037" src="https://github.com/user-attachments/assets/befaf7d8-a37b-4631-9bd6-df80b55d720e" />
<img width="906" height="378" alt="Screenshot 2026-06-08 181051" src="https://github.com/user-attachments/assets/53a1fa34-3b98-44e0-beea-a9707cbb8c6b" />
<img width="908" height="335" alt="Screenshot 2026-06-08 181103" src="https://github.com/user-attachments/assets/ec4624d8-9adf-4eab-8bc1-77c2cf1cdfc5" />
<img width="909" height="161" alt="Screenshot 2026-06-08 181113" src="https://github.com/user-attachments/assets/b79ff15c-5f64-4372-88f5-1dec8a70a074" />

_____

PENJELASAN OUTPUT

Memilih menu 1, lalu memasukkan NPM 2515061001 dan nama abe. Data berhasil disimpan ke dalam hash table.

Memilih menu 1 lagi, lalu memasukkan NPM 2515061002 dan nama ode. Data kedua berhasil disimpan.

Memilih menu 4 untuk menampilkan data. Program menampilkan:

2515061001 | abe

2515061002 | ode

Memilih menu 2 dan mencari NPM 2515061002. Data ditemukan dengan nama ode.

Memilih menu 3 dan menghapus NPM 2515061001. Data berhasil dihapus.

Memilih menu 4 kembali. Program hanya menampilkan:

2515061002 | ode

Memilih menu 5 untuk keluar. Program menampilkan pesan "Program selesai." dan berhenti.

_____

link video : https://youtu.be/y5mf-2MSQk8?si=6H4BvDMgU_yg-6rB


