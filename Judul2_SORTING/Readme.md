
Judul : Sistem Rekomendasi Tempat Magang Berdasarkan Rating 

Program ini berfungsi sebagai sistem sederhana untuk mengelola dan merekomendasikan tempat magang berdasarkan nilai rating. Pengguna dapat memasukkan beberapa data tempat magang beserta ratingnya, kemudian sistem akan mengurutkan data tersebut dari rating tertinggi ke terendah.

Program ini menggunakan struktur data Array (List) untuk menyimpan nama tempat dan rating secara terpisah, serta menerapkan algoritma Selection Sort (O(n²)) untuk proses pengurutan. Pengolahan data dilakukan menggunakan teknik indexing agar relasi antara nama dan rating tetap sinkron saat ditukar.

<img width="909" height="405" alt="image" src="https://github.com/user-attachments/assets/cd736bb2-ec48-4598-b065-6bb15881c537" />

<img width="914" height="403" alt="Screenshot 2026-04-28 203526" src="https://github.com/user-attachments/assets/b8f9a146-14b4-4f1e-83a9-891dfae76d8a" />

____________________________________________________________________
FUNGSi AWAl

fungsi tukar untuk menukar posisi dua elemen dalam list arr. 

temp menyimpan sementara nilai di indeks i. 

Lalu nilai di indeks i diganti dengan nilai di indeks j. 

Nilai di indeks j diganti dengan temp.

_________________________________________________________________
FUNGSI SELECtION SORT

Fungsi selection_sort untuk mengurutkan data berdasarkan rating tertinggi.

for i in range(n - 1):  loop dari elemen pertama sampai sebelum terakhir.

pos = i   anggap posisi awal sebagai nilai terbesar.

for j in range(i + 1, n):   loop membandingkan elemen setelah i.

if rating[j] > rating[pos]:   jika ditemukan rating lebih besar, 

pos = j simpan indeksnya di pos

if pos != i:
Mengecek apakah indeks posisi nilai terbesar (pos) berbeda dengan indeks awal (i).

tukar(rating, i, pos)
Menukar nilai rating di indeks i dengan nilai rating di indeks pos.
            
tukar(nama, i, pos)
Menukar nilai nama di indeks i dengan nama di indeks pos.
__________________________________________________________________________________________________________
FUNGSI UTAMA

def main():
mendefinisikan fungsi main

try:
digunakan untuk validasi input supaya tidak error

n = int(input("Masukkan jumlah tempat: "))
meminta inputan kepada user 

except ValueError:

print("Input tidak valid!")
menampilkan input tidak valid

return
mengembalikan nilai 

nama = []
membuat list kosong untuk nama tempat magang 

rating = []
membuat list kosong untuk rating

____________________________________________________________________________________________________
LOOPING UNTUK MENAMBAHKAN DATA

for i in range(n):
melakukan perulangan sebanyak n kali

print("\nData ke-", i + 1)
menampilkan urutan data dari data k-1 sampai n

nama.append(input("Nama tempat: "))
meminta input nama tempat , lalu menambahkannya ke list nama
        
while True:
perulangan apabila masih true

try:
digunakan untuk validasi input supaya tidak error

nilai = float(input("Rating: "))
meminta input angka nilai rating dari tempat magang

rating.append(nilai)
menambahkan inputan nilai ke list rating

break
keluar dari loop

except ValueError:

print("Masukkan angka yang valid!")
jika input tidak valid (bukan angka) , meanmpilkan masuan angka yang valid

__________________________________________________________________________________
print("\n=== Sistem Rekomendasi Tempat Magang berdasarkan Rating Tertinggi ===")
menampilkan judul program

print("\nSebelum diurutkan:")
menampilkan teks "sebelum di urutkan"

for i in range(n):
perulangan sebanyak n kali 

print(nama[i], "-", rating[i])
menampilkan data sebelum di sorting , nama ke i - raitng ke i

selection_sort(rating, nama, n)
memanggil fungsi selection sort dengan parameter rating , nama , dan n (banyaknya data)

print("\nSetelah diurutkan:")
menampilkan teks "setelah di urutkan"

for i in range(n):
perulangan sebanyak n kali 

print(nama[i], "-", rating[i])
menampilkan data setelah di sorting , nama ke i - raitng ke i

if __name__ == "__main__":

main()
memanggil fungsi main

________________________________________________________________________________________

<img width="928" height="424" alt="Screenshot 2026-04-28 203400" src="https://github.com/user-attachments/assets/41691ad6-575d-4f92-9616-e48a7eb0143b" />
<img width="923" height="117" alt="Screenshot 2026-04-28 203416" src="https://github.com/user-attachments/assets/bc81725d-6275-4387-b6b6-e599edaba812" />

outputnya

meminta input banyaknya data tempat kepada user 

lalu user diminta menginputkan isi data ke 1-5 , dengan isian nama tempat dan rating

lalu menampilkan judul program 

menampilkan data sebelum di urutkan 

terakhir , menampilkan data setelah di urutkan berdasarkan nilai rating.




