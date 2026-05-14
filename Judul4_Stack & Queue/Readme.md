Judul : Sistem Undo Redo pada Teks Editor Berbasis Stack Array

Program ini berfungsi sebagai simulator pengelolaan riwayat aksi pada sebuah teks editor secara terstruktur dan efisien. Lewat sistem ini, user/pengguna bisa menambahkan aksi atau perubahan teks, melakukan undo untuk membatalkan aksi terakhir, melakukan redo untuk mengembalikan aksi yang telah dibatalkan, serta melihat seluruh riwayat aksi yang tersimpan. Program ini membantu mempermudah pengelolaan perubahan data dan meminimalisir kesalahan yang fatal saat melakukan pengeditan teks.

Program ini menggunakan struktur data Stack Array untuk menyimpan riwayat aksi user/penggunanya. Konsep yang digunakan adalah LIFO (Last In First Out), yaitu data yang paling terakhir masuk akan menjadi data yang pertama kali keluar. Proses undo dilakukan dengan cara mengambil aksi terakhir dari stack history dan memindahkannya ke stack redo , sedangkan proses redo dilakukan dengan mengembalikan aksi dari stack redo ke stack history, jadi akan ada 2 stack pada sistem ini. Dengan penggunaan stack array, proses penyimpanan dan pengelolaan riwayat aksinya akan menjadi lebih teratur dan efisien.

_____


