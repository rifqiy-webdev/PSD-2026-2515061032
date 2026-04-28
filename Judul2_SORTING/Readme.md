
Judul : Sistem Rekomendasi Tempat Magang Berdasarkan Rating ( Selection Sort)

Program ini berfungsi sebagai sistem sederhana untuk mengelola dan merekomendasikan tempat magang berdasarkan nilai rating. Pengguna dapat memasukkan beberapa data tempat magang beserta ratingnya, kemudian sistem akan mengurutkan data tersebut dari rating tertinggi ke terendah.

Program ini menggunakan struktur data Array (List) untuk menyimpan nama tempat dan rating secara terpisah, serta menerapkan algoritma Selection Sort (O(n²)) untuk proses pengurutan. Pengolahan data dilakukan menggunakan teknik indexing agar relasi antara nama dan rating tetap sinkron saat ditukar.

<img width="912" height="410" alt="Screenshot 2026-04-28 203458" src="https://github.com/user-attachments/assets/f7a18b6e-7b12-4843-bf0b-8ac0c3c98b13" />
<img width="914" height="403" alt="Screenshot 2026-04-28 203526" src="https://github.com/user-attachments/assets/b8f9a146-14b4-4f1e-83a9-891dfae76d8a" />

FUNGSi AWAl

fungsi tukar untuk menukar posisi dua elemen dalam list arr. 

temp menyimpan sementara nilai di indeks i. 

Lalu nilai di indeks i diganti dengan nilai di indeks j. 

Nilai di indeks j diganti dengan temp.


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
            



