BAB 10
-
10.1. Antarmuka Sistem Operasi 
-

The osmodul menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi
Pastikan untuk menggunakan gaya daripada . Ini akan mencegah membayangi fungsi bawaan yang beroperasi jauh berbeda.import osfrom os import *os.open()open()

Built-in dir()dan help()fungsi berguna sebagai bantuan interaktif untuk bekerja dengan modul besar seperti os

Untuk tugas-tugas harian dan manajemen direktori, shutilmodul ini menyediakan antarmuka tingkat yang lebih tinggi yang lebih mudah digunakan

10.2. File Wildcard 
-
The globmodul menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard

10.3. Argumen Baris Perintah 
-
Skrip utilitas umum sering perlu memproses argumen baris perintah. Argumen-argumen ini disimpan dalam atribut argvsys modul sebagai daftar. Sebagai contoh hasil keluaran berikut dari berjalan pada baris perintah:python demo.py one two three

The getoptproses modul sys.argv menggunakan konvensi dari Unix getopt()fungsi. Pemrosesan baris perintah yang lebih kuat dan fleksibel disediakan oleh argparsemodul.

10.4. Kesalahan Output Redirection dan Penghentian Program 
-
The sysModul juga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah dialihkan
Cara paling langsung untuk mengakhiri skrip adalah menggunakan sys.exit().

10,5. Pencocokan Pola String
-
The reModul menyediakan alat ekspresi reguler untuk pengolahan string yang canggih. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:
Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena mereka lebih mudah dibaca dan di-debug

10.6. Matematika
-
The mathmodul memberikan akses ke mendasari C fungsi perpustakaan untuk floating point matematika
Para randommodul menyediakan alat untuk membuat pilihan acak
The statisticsModul menghitung sifat dasar statistik (mean, median, varians, dll) dari data numerik
Proyek SciPy < https://scipy.org > memiliki banyak modul lain untuk perhitungan numerik

10.7. Akses Internet 
-
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.requestuntuk mengambil data dari URL dan smtplibuntuk mengirim email

10.8. Tanggal dan Waktu 
-
The datetimeModul memasok kelas untuk memanipulasi tanggal dan waktu di kedua cara sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus dari implementasi adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi output. Modul ini juga mendukung objek yang sadar zona waktu.

10.9. Kompresi Data 
-
Pengarsipan data umum dan kompresi format secara langsung didukung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfiledan tarfile.

10.10. Pengukuran Kinerja 
-
Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Python menyediakan alat pengukuran yang menjawab pertanyaan-pertanyaan itu dengan segera.

Misalnya, mungkin tergoda untuk menggunakan pengemasan tuple dan fitur unpacking daripada pendekatan tradisional untuk bertukar argumen. The timeit Modul cepat menunjukkan keunggulan kinerja yang sederhana:
Berbeda dengan timeittingkat perincian yang bagus, modul profiledan pstatsmenyediakan alat untuk mengidentifikasi bagian waktu kritis dalam blok kode yang lebih besar.

10.11. Kontrol Kualitas 
-
Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah menulis tes untuk setiap fungsi seperti yang dikembangkan dan untuk menjalankan tes tersebut sering selama proses pengembangan.

The doctestmodul menyediakan alat untuk memindai modul dan memvalidasi tes tertanam dalam docstrings program ini. Uji konstruksi sederhana seperti memotong dan menyisipkan panggilan khas bersama dengan hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest memastikan kode tetap benar untuk dokumentasi
The unittestModul ini tidak mudah seperti doctestmodul, tetapi memungkinkan satu set yang lebih komprehensif dari tes untuk dipertahankan dalam file terpisah

10.12. Termasuk Baterai 
-
Python memiliki filosofi "termasuk baterai". Ini paling baik dilihat melalui kapabilitas yang canggih dan kuat dari paket-paketnya yang lebih besar. Sebagai contoh:

-
The xmlrpc.clientdan xmlrpc.servermodul membuat menerapkan prosedur remote panggilan ke tugas yang hampir sepele. Meskipun nama modul, tidak ada pengetahuan langsung atau penanganan XML yang diperlukan.

-
The emailpaket perpustakaan untuk mengelola pesan email, termasuk MIME dan lainnyaDokumen pesan berbasis RFC 2822 . Tidak sepertismtplibdan poplibyang benar-benar mengirim dan menerima pesan, paket email memiliki toolset lengkap untuk membangun atau decoding struktur pesan yang kompleks (termasuk lampiran) dan untuk menerapkan pengkodean internet dan protokol header.

-
The jsonpaket menyediakan dukungan kuat untuk parsing format data interchange populer ini. The csvModul mendukung pembacaan langsung dan menulis file dalam format Nilai Comma-Separated, umumnya didukung oleh database dan spreadsheet. Pengolahan XML didukung oleh xml.etree.ElementTree, xml.domdan xml.saxpaket. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.

-
The sqlite3modul pembungkus untuk perpustakaan basis data SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL sedikit tidak standar.
Internasionalisasi didukung oleh sejumlah modul termasuk gettext, locale, dan codecspaket.
