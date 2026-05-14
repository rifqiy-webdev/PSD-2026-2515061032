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


___

<img width="901" height="438" alt="Screenshot 2026-05-14 190045" src="https://github.com/user-attachments/assets/4729bcea-2a3e-4cdf-b916-f3452854f18e" />
<img width="926" height="283" alt="Screenshot 2026-05-14 190110" src="https://github.com/user-attachments/assets/b091479b-6602-424b-8925-e33437993abe" />
<img width="920" height="289" alt="Screenshot 2026-05-14 190131" src="https://github.com/user-attachments/assets/dbb67f41-0320-4371-8c67-c6b17a6d5781" />
<img width="921" height="306" alt="Screenshot 2026-05-14 190144" src="https://github.com/user-attachments/assets/96c9ee13-e7d5-4607-b567-c811589f548a" />

___



