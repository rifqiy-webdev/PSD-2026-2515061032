Judul : Sistem Pencarian Buku Berbasis Array

Program ini berfungsi sebagai simulator pencarian data buku dalam sebuah perpustakaan atau toko buku digital secara terstruktur dan efisien. Melalui sistem ini, user bisa menambahkan daftar buku, mencari buku berdasarkan judul tertentu, serta menampilkan seluruh data buku yang ada. Program ini membantu mempermudah proses pencarian  buku dan meminimalisir kesalahan pencarian secara manual.

Program ini menerapkan struktur data Array (List) untuk menyimpan kumpulan data buku. Algoritma yang digunakan adalah Binary Search (O(Log n)). yaitu metode pencarian dengan membagi data menjadi dua bagian secara berulang hingga data yang dicari ditemukan. Pencarian dilakukan dengan membandingkan judul buku target dengan elemen tengah array, kemudian menentukan apakah pencarian dilanjutkan ke bagian kiri atau kanan data. 

____

<img width="896" height="196" alt="Screenshot 2026-05-07 195624" src="https://github.com/user-attachments/assets/f70a51e1-d0f2-4654-bd60-b64846dbb22b" />
<img width="910" height="334" alt="Screenshot 2026-05-07 195639" src="https://github.com/user-attachments/assets/799b4097-9233-4326-a4aa-a842ae8457f9" />
<img width="907" height="368" alt="Screenshot 2026-05-07 195709" src="https://github.com/user-attachments/assets/14647cf3-ee8f-4851-ae32-c1937fa6bd04" />
<img width="903" height="307" alt="Screenshot 2026-05-07 195727" src="https://github.com/user-attachments/assets/a5d1356e-9eb1-4395-9c5d-d3ce9a301d3f" />

___

FUNGSI SELECTION SORT

def selection_sort(buku, n):
mendefinisikan fungsi selection sort dengan parameter buku (listnya), dan n (banayaknya elemen)

for i in range(n - 1):
melakukan perulangan sebanyak jumlah elemen 

min_idx = i
mengasumsikan elem index terkecil adalah i

for j in range(i + 1, n):
perulangan kedua untuk mencari elemen terkecil di sisa list. Dimulai dari indeks setelah i (i+1) sampai akhir list.

if buku[j].lower() < buku[min_idx].lower():
Membandingkan apakah elemen buku[j] lebih kecil dengan elemen terkecil saat ini (buku[min_idx]). .lower() digunakan supaya perbandingan tidak sensitif terhadap huruf besar atau kecil.

min_idx = j
kalau ditemukan elemen yang lebih kecil, min_idx diperbarui ke indeks j.

if min_idx != i:
Mengecek apakah elemen terkecil ditemukan di posisi lain (min_idx ≠ i).

buku[i], buku[min_idx] = buku[min_idx], buku[i]
kalau iya, maka dilakukan pertukaran antara elemen di posisi i dengan elemen di posisi min_idx.

___

FUNGSI BINARY SEARCH

def binary_search(buku, n, target): Mendefinisikan fungsi binary_search dengan parameter buku , n , dan target

l = 0
indeks batas kiri (awal list).

r = n - 1
indeks batas kanan (akhir list).


while l <= r:
Perulangan berjalan selama batas kiri (l) belum melewati batas kanan (r).

m = l + (r - l) // 2
index tengah elemen, memastikan pembagian bulat (integer division).

print(f"Sedang cek buku: {buku[m]}")
menampilkan elemen yang sedang dicek di posisi tengah.

if buku[m].lower() == target.lower():
Jika elemen tengah sama dengan target maka pencarian berhasil.

return m
fungsi mengembalikan nilai index m

elif buku[m].lower() < target.lower():
Jika elemen tengah lebih kecil daripada target

print("Mencari di kanan...")
Menampilkan mencari di kanan

l = m + 1
batas kiri (l) digeser ke m + 1.

else:
Jika tidak, berarti target ada di sisi kiri.

print("Mencari di kiri...")
Menampilkan mencari dikiri 

r = m - 1
batas kanan (r) digeser ke m - 1.

return -1
Jika loop selesai tanpa menemukan target, fungsi mengembalikan -1 sebagai tanda tidak ditemukan.

___

FUNGSI UTAMA

def main():
Mendefinisikan fungsi main sebagai titik masuk program.

try:

n = int(input("Masukkan jumlah buku: "))
Meminta pengguna memasukkan jumlah buku.

except ValueError:

print("Input tidak valid!")
Jika input bukan angka , akan terjadi error ValueError.

return
lalu menghentikan fungsi dengan return.

buku = []
Membuat list kosong bernama buku untuk menampung judul buku yang akan dimasukkan oleh user.

print("\nMasukkan judul buku:")
Menampilkan masukkan judul buku

for i in range(n):
Melakukan perulangan sebanyak n kali

judul = input(f"Buku ke-{i+1}: ")
Mmeminta input judul buku kepada user.

buku.append(judul)
Menambahkan judul buku kedalam list buku

print("\n Buku Sebelum diurutkan:")
Menamplkan buku sebelum di urutkan

print(buku)
menampilkan list buku

selection_sort(buku, n)
Memanggil fungsi selection sort denan parameter buku dan n.

print("\n Buku Setelah diurutkan (A-Z):")
menampikan Buku Setelah diurutkan (A-Z)

print(buku)
Menampilkan list buku setelah di sorting

target = input("\nMasukkan judul buku yang ingin dicari: ")
meminta pengguna memasukkan judul buku yang akan dicari.

pos = binary_search(buku, n, target)
memanggil fungsi binary_search dengan parameter buku, n, dan target. lalu disimpan ke dalam variabel pos.

if pos != -1:
Mengecek apakah hasil pencarian bukan -1.

if pos < n // 2:
Jika indeks pos lebih kecil dari setengah jumlah buku.

print(f"\n Buku '{target}' ditemukan pada indeks {pos} di area awal ")
menampilakn Buku '{target}' ditemukan pada indeks {pos} di area awal

else:
print(f"\n Buku '{target}' ditemukan pada indeks {pos} di area akhir ")
Jika indeks pos lebih besar atau sama dengan setengah jumlah buku, menampilkan Buku '{target}' ditemukan pada indeks {pos} di area akhir.

else:
jika tidak ditemukan

print("\n Buku tidak ditemukan")
menampilkan pesan buku tidak ditemukan

if __name__ == "__main__":
Bmemastikan bahwa fungsi main() hanya dijalankan jika file Python ini dieksekusi langsung.

main()
memanggil fungsi main() untuk di jalankan

___

<img width="914" height="382" alt="image" src="https://github.com/user-attachments/assets/9925991d-ea75-4331-898e-0dc83bf58aed" />
___

 OUTPUT


Masukkan jumlah buku: 5
user memasukkan angka 5 , berarti akan ada 5 judul buku yg di tambahkan

Masukkan judul buku:
Program meminta judul buku satu per satu.

Buku ke-1: vibe coding

Buku ke-2: ai

Buku ke-3: machine learning

Buku ke-4: aljabar matriks

Buku ke-5: kalkulus

user meanmbahkan judul buku satu persatu

Buku Sebelum diurutkan:

['vibe coding', 'ai', 'machine learning', 'aljabar matriks ', 'kalkulus']
menampilkan list buku sebelum di urutkan 

Buku Setelah diurutkan (A-Z):

['ai', 'aljabar matriks ', 'kalkulus', 'machine learning', 'vibe coding']
menampilkan list buku setelah di urutkan 

Masukkan judul buku yang ingin dicari: ai
,user memasukkan ai sebagai target pencarian.

Sedang cek buku: kalkulus
Algoritma Binary Search mulai dari tengah list = kalkulus.

Mencari di kiri...
Karena ai lebih kecil dari kalkulus, pencarian digeser ke kiri.

Sedang cek buku: ai\
Dicek lagi elemen di kiri = ai, cocok dengan target

Buku 'ai' ditemukan pada indeks 0 di area awal
program menemukan target

link video : https://youtu.be/Y886fDdQ1gU



