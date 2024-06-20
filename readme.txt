Aplikasi Web dalam tahap pengembangan 
Masalah yang Anda alami disebabkan oleh kebijakan eksekusi PowerShell di sistem Anda yang tidak mengizinkan menjalankan skrip. Untuk mengatasi masalah ini, Anda perlu mengubah kebijakan eksekusi PowerShell.

Langkah-langkah Mengatasi Masalah Eksekusi Skrip PowerShell
Buka PowerShell dengan hak akses Administrator:

Klik kanan pada ikon PowerShell dan pilih "Run as administrator".
Cek kebijakan eksekusi saat ini:

powershell
Salin kode
Get-ExecutionPolicy
Kebijakan yang mungkin Anda lihat adalah Restricted atau RemoteSigned.

Ubah kebijakan eksekusi menjadi RemoteSigned:

powershell
Salin kode
Set-ExecutionPolicy RemoteSigned
Anda mungkin akan diminta untuk mengonfirmasi perubahan ini. Ketik Y dan tekan Enter.

Aktifkan Virtual Environment:
Sekarang Anda bisa mengaktifkan virtual environment tanpa masalah:

powershell
Salin kode
.\venv\Scripts\activate
Setelah selesai, Anda bisa mengembalikan kebijakan eksekusi ke pengaturan sebelumnya (opsional):

powershell
Salin kode
Set-ExecutionPolicy Restricted
Berikut adalah langkah-langkah yang lebih rinci:

Langkah-langkah Rinci
Buka PowerShell sebagai Administrator:

Cari PowerShell di menu Start.
Klik kanan pada Windows PowerShell dan pilih "Run as administrator".
Periksa Kebijakan Eksekusi Saat Ini:
Jalankan perintah berikut untuk melihat kebijakan eksekusi saat ini:

powershell
Salin kode
Get-ExecutionPolicy
Ubah Kebijakan Eksekusi:
Ubah kebijakan eksekusi menjadi RemoteSigned agar dapat menjalankan skrip dari virtual environment:

powershell
Salin kode
Set-ExecutionPolicy RemoteSigned
Jika diminta konfirmasi, ketik Y dan tekan Enter.

Aktifkan Virtual Environment:
Pindah ke direktori proyek Anda dan aktifkan virtual environment:

powershell
Salin kode
cd C:\Users\USER\OneDrive\Desktop\qr_code_generator - TEST KE SERVER
.\venv\Scripts\activate
Kembalikan Kebijakan Eksekusi (opsional):
Setelah Anda selesai bekerja dengan virtual environment dan ingin mengembalikan kebijakan eksekusi ke pengaturan semula, Anda dapat melakukannya dengan:

powershell
Salin kode
Set-ExecutionPolicy Restricted
Setelah melakukan langkah-langkah di atas, Anda seharusnya dapat mengaktifkan virtual environment dan melanjutkan dengan instalasi paket serta menjalankan aplikasi Flask.