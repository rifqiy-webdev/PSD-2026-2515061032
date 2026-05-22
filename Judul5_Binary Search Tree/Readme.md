Judul: Sistem Leaderboard Pemain Berbasis Binary Search Tree

Program ini berfungsi sebagai simulator pengelolaan leaderboard skor pemain di sebuah game atau kompetisi secara terstruktur dan efisien. Dari sistem ini, user bisa menambahkan data skor, menampilkan urutan skor pemain, serta melihat posisi skor tertinggi maupun terendah. Program ini membantu mempermudah pengelolaan data peringkat pemain dan mempercepat proses pencarian maupun pembaruan skor pada sistem leaderboard.

Program ini menggunakan struktur data Binary Search Tree (BST) untuk menyimpan data skor pemain. Konsep yang digunakan adalah penyimpanan data berdasarkan nilai, di mana data lebih kecil berada di subtree kiri dan data lebih besar berada di subtree kanan. Dengan BST, proses pencarian, penambahan, dan pengurutan data leaderboard menjadi lebih cepat, rapi, dan efisien.
___

<img width="915" height="354" alt="Screenshot 2026-05-21 222808" src="https://github.com/user-attachments/assets/47a6ef22-3fee-4569-81eb-befa39dee9a0" />
<img width="886" height="400" alt="Screenshot 2026-05-21 222824" src="https://github.com/user-attachments/assets/cd0c1514-9872-4038-b823-df94cfeb417b" />
<img width="890" height="393" alt="Screenshot 2026-05-21 222842" src="https://github.com/user-attachments/assets/90b63b4f-b4e8-41a9-8d7e-db9287bc972f" />
<img width="881" height="399" alt="Screenshot 2026-05-21 222859" src="https://github.com/user-attachments/assets/5714483e-c563-4dea-b847-f204da564bef" />
<img width="880" height="60" alt="Screenshot 2026-05-21 222914" src="https://github.com/user-attachments/assets/6215a969-7245-46ad-8c68-7e1affe1e241" />

___

MEMBUAT NODE

class Node:
Membuat class bernama Node.

def __init__(self, key):
Membuat konstruktor dengan parameter key sebagai nilai skor

self.key = key
Menyimpan nilai skor ke variabel key.

self.left = None
Menyimpan child kiri, awalnya kosong

self.right = None
Menyimpan child kanan, awalnya kosong

____

MEMBUAT CLASS UNTUK LEADERBOARD

class LeaderboardBST:
membuat class bernama LeaderboardBST.

def __init__(self):
membuat konstruktor untuk BST

self.root = None
membuat root awal, di inisialisasi awalnya kosong

____

def insert_node(self, root, key):
Membuat fungsi rekursif untuk menambah node.

if root is None:
Jika node belum ada 

return Node(key)
buat node baru dan kembalikan nilainya

if key < root.key:
Kalau skor lebih kecil dari node saat ini , maka masuk kiri.

root.left = self.insert_node(root.left, key)
masuk ke subtree kiri.

elif key > root.key:
Kalau skor lebih besar , kekanan

root.right = self.insert_node(root.right, key)
masuk subtree kanan

return root
mengembalikan node


def insert(self, key):
fungsi untuk insert skor.

self.root = self.insert_node(self.root, key)
Memulai insert dari root.

_____

MEMBUAT FUNGSI UNTUK TRAVERSAL INORDER

def inorder(self, root):
membuat fungsi bernama inorder dengan parameternya root.

if root is None:
kalau kosong , berhenti

return

self.inorder(root.left)
Kunjungi subtree kiri

print(root.key, end=" ")
cetak nilai node root

self.inorder(root.right)
kunjungi subtree kanan

____

FUNGSI MENCARI NILAI MAXIMUM

def find_max(self, root):
membuat fungsi bernama find_max

if root is None:
kalau treenya kosong

return None
Kembalikan none

current = root
Mulai dari root.

while current.right is not None:
Selama masih ada node kanan atau node dikanan tidak kosong.

current = current.right
Geser kekanan  

return current.key
kembalikan nilai nodenya

____

FUNGSI MENCARI NILAI MINIMUM

def find_min(self, root):
Membuat fungsi bernana find_min

if root is None:
kalau root atau treenya kosong 

return None
kembalikan none

current = root
mulai dari root

while current.left is not None:
Selama masih ada node kiti atau node dikiti tidak kosong.

current = current.left
geser kekiri

return current.key
Kembalikan niliai nodenya

____

FUNGSI UTAMA PROGRAM

def main():
membaut fungsi bernama main.

leaderboard = LeaderboardBST()
Membuat objek BST.

pilih = 0
inisialisasi pilih = 0

while pilih != 5:
perulangan berjalan selama user belum pilih 5.

print("\n=== LEADERBOARD GAME ===")
menampilkan === LEADERBOARD GAME ===

print("1. Tambah skor pemain")
menampilkan 1. Tambah skor pemain

print("2. Tampilkan leaderboard")
menampilkan 2. Tampilkan leaderboard

print("3. Lihat skor tertinggi")
menampilkan 3. Lihat skor tertinggi

print("4. Lihat skor terendah")
menampilkan 4. Lihat skor terendah

print("5. Keluar")
menampilkan 5. Keluar

try:
menangani error

pilih = int(input("Pilih menu: "))
meminta inputan angka kepada user

except ValueError:
kalau input bukan angka

print("Input harus angka!")
tampilkan input bukan angka

continue

____

MENU 1 TAMBAH SKOR

if pilih == 1:
jika pilih 1

try:
skor = int(input("Masukkan skor pemain: "))
meminta inputan nilai skor

leaderboard.insert(skor)
memasukkan skor ke leaderboard

print("Skor berhasil ditambahkan!")
menampilkan skor berhasil ditambahkan

except ValueError:
jika input bukan angka

print("Input tidak valid!")
tampilkan input tidak valid

____

MENU 2 MENAMPILKAN LEADERBOARD

elif pilih == 2:
jika pilih 2

print("Leaderboard (terendah -> tertinggi):")
nenampikan Leaderboard (terendah -> tertinggi):

leaderboard.inorder(leaderboard.root)
melakukan traversal inorder di bst leaderboard

print()
tampikan di baris baru

____

MENU 3 CARI NILAI TERTINGGI

elif pilih == 3:
jika pilih 3

max_score = leaderboard.find_max(leaderboard.root)
mencari nilai max dan menyimpan di variabel max score

if max_score is not None:
jika nilai max tidak kosong

print(f"Skor tertinggi (Juara 1): {max_score}")
menampikan skor tertinggi 

else:
jka kosong 

print("Leaderboard masih kosong")
meanmpilkan leaderboard masih kosong

_____

MENU 4 MENCARI NILAI TERKECIL

elif pilih == 4:
JIKA PILIH 4

min_score = leaderboard.find_min(leaderboard.root)
mencari nilai minimum dan menyimpan di variabel min score


if min_score is not None:
jika nilai max tidak kosong

print(f"Skor terendah: {min_score}")
menampilkan skor terendah

else:
jika kosong

print("Leaderboard masih kosong")
menampilkan leaderboard masik kosong

_____

MENU 5 KELUAR

elif pilih == 5:
jika pilih 5

print("Program selesai.")
keluar program dan meanmpilkan program selesai

____

else:
jika bukan pilihan

print("Pilihan tidak valid!")
menammpilkan pilihan tidak valid


if __name__ == "__main__":
agar fungsi main langsung djalankan

main()
memanggil fungsi main



___
<img width="919" height="392" alt="Screenshot 2026-05-21 222643" src="https://github.com/user-attachments/assets/c66f25a2-ccca-47a2-aa90-380e77aa38b2" />
<img width="897" height="391" alt="Screenshot 2026-05-21 222704" src="https://github.com/user-attachments/assets/f6c723e7-9ed2-4060-a180-946b4063115a" />
<img width="914" height="377" alt="Screenshot 2026-05-21 222723" src="https://github.com/user-attachments/assets/1ee1c98c-7612-49ee-ac1f-0fcc0d7a37d9" />
<img width="917" height="269" alt="Screenshot 2026-05-21 222736" src="https://github.com/user-attachments/assets/58aaac8b-9912-4d5e-bdec-dad4af57c362" />

_____

PENJELASAN OUTPUT

user memilih menu 1 , menambahkan skor , sebanyak 7 kali 

yaitu menginputkan 4,3,8,2,5,6,9

lalu user memilih menu 2 , nenampilkan bst leaderboeardnya sacara inorder ( 2 3 4 5 6 8 9 )

lalu user memilih menu 3 , skor tertinggi = 9

lalu user memilih menu 4 , skor tertinggi = 2

terakhir user memilihmenu 5 , keluar program.

_____

link video : https://youtu.be/A9n__fO9lng?si=iKkmFRaW-wLgbEJZ

