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

class SlotState:
EMPTY = 0
OCCUPIED = 1
DELETED = 2


class Entry:
def __init__(self):
self.key = None
self.value = None
self.state = SlotState.EMPTY


class HashMapOpenAddressing:
def __init__(self, size=10):
self.SIZE = size
self.table = [Entry() for _ in range(self.SIZE)]

def hash_function(self, key):
return (key % self.SIZE + self.SIZE) % self.SIZE

def insert(self, key, value):
idx = self.hash_function(key)
first_deleted = -1

for step in range(self.SIZE):
i = (idx + step) % self.SIZE

if self.table[i].state == SlotState.OCCUPIED:
if self.table[i].key == key:
self.table[i].value = value
return True

elif self.table[i].state == SlotState.DELETED:
if first_deleted == -1:
first_deleted = i

else:
if first_deleted != -1:
i = first_deleted

self.table[i].key = key
self.table[i].value = value
self.table[i].state = SlotState.OCCUPIED
return True

return False

def search(self, key):
idx = self.hash_function(key)

for step in range(self.SIZE):
i = (idx + step) % self.SIZE

if self.table[i].state == SlotState.EMPTY:
return None

if self.table[i].state == SlotState.OCCUPIED and self.table[i].key == key:
return self.table[i]

return None

def remove_key(self, key):
entry = self.search(key)

if entry is None:
return False

entry.state = SlotState.DELETED
return True

def display(self):
print("\n===== DATA MAHASISWA =====")

for i in range(self.SIZE):
if self.table[i].state == SlotState.OCCUPIED:
print(
f"NPM: {self.table[i].key} | Nama: {self.table[i].value}"
)


def main():
mahasiswa = HashMapOpenAddressing()

while True:
print("\n===== MENU DATA MAHASISWA =====")
print("1. Tambah Mahasiswa")
print("2. Cari Mahasiswa")
print("3. Hapus Mahasiswa")
print("4. Tampilkan Semua Data")
print("5. Keluar")

pilihan = int(input("Pilih menu: "))

if pilihan == 1:
npm = int(input("Masukkan NPM: "))
nama = input("Masukkan Nama: ")

if mahasiswa.insert(npm, nama):
print("Data berhasil disimpan.")
else:
print("Hash Table penuh!")

elif pilihan == 2:
npm = int(input("Masukkan NPM yang dicari: "))

hasil = mahasiswa.search(npm)

if hasil:
print(f"Data ditemukan")
print(f"NPM  : {hasil.key}")
print(f"Nama : {hasil.value}")
else:
print("Data tidak ditemukan.")

elif pilihan == 3:
npm = int(input("Masukkan NPM yang akan dihapus: "))

if mahasiswa.remove_key(npm):
print("Data berhasil dihapus.")
else:
print("Data tidak ditemukan.")

elif pilihan == 4:
mahasiswa.display()

elif pilihan == 5:
print("Program selesai.")
break

else:
print("Pilihan tidak valid.")


if __name__ == "__main__":
main()

___


