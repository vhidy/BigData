pandas

Perpustakaan Analisis Data Python 
panda adalah open source, perpustakaan berlisensi BSD yang menyediakan struktur data dan alat analisis data kinerja tinggi, mudah digunakan untuk bahasa pemrograman Python .

panda adalah proyek yang disponsori NumFOCUS . Ini akan membantu memastikan keberhasilan pengembangan panda sebagai proyek sumber terbuka kelas dunia, dan memungkinkan untuk disumbangkan ke proyek.

Ini adalah rilis bug-fix minor dalam seri 0.23.x dan mencakup beberapa perbaikan regresi, perbaikan bug, dan peningkatan kinerja. Kami menyarankan agar semua pengguna meningkatkan ke versi ini.

Rilis dapat dipasang dengan conda dari conda-forge atau saluran default:

conda install pandas
Atau melalui PyPI:

python3 -m pip install --upgrade pandas
Lihat apa yang lengkap untuk daftar semua perubahan.

v0.23.0 Final (15 Mei 2018) 
Ini adalah rilis besar dari 0.22.0 dan mencakup sejumlah perubahan API, fitur baru, peningkatan, dan peningkatan kinerja bersama dengan sejumlah besar perbaikan bug.

Sorotan meliputi:

Format JSON round-trippable dengan orientasi 'tabel' .
Instansiasi dari perintah menghormati perintah untuk Python 3.6+ .
Argumen kolom dependen untuk menetapkan .
Penggabungan / penyortiran pada kombinasi kolom dan tingkat indeks .
Memperluas Pandas dengan tipe khusus .
Tidak termasuk kategori yang tidak teramati dari groupby .
Kandidat rilis dapat diinstal dengan conda dari saluran pengembangan kami (dibuat untuk osx-64, linux-64 dan win-64 untuk Python 2.7, Python 3.5, dan Python 3.6 semuanya tersedia):

conda install pandas
atau conda menempa:

conda install -c conda-forge pandas
Atau melalui PyPI:

python3 -m pip install --upgrade pandas==0.23.0
Lihat apa yang lengkap untuk daftar semua perubahan.

Cara terbaik untuk Menginstal 
Cara terbaik untuk mendapatkan panda adalah melalui conda

conda install pandas

Paket tersedia untuk semua versi python yang didukung di Windows, Linux, dan MacOS.

Roda juga diunggah ke PyPI dan dapat diinstal

pip install pandas
Sketsa cepat 

Masalah apa yang diselesaikan panda ? 
Python telah lama bagus untuk data munging dan persiapan, tetapi kurang begitu untuk analisis data dan pemodelan. panda membantu mengisi celah ini, memungkinkan Anda untuk melaksanakan seluruh alur kerja analisis data Anda dengan Python tanpa harus beralih ke bahasa yang lebih spesifik domain seperti R.

Dikombinasikan dengan toolkit IPython yang sangat baik dan pustaka lainnya, lingkungan untuk melakukan analisis data dengan Python unggul dalam kinerja, produktivitas, dan kemampuan untuk berkolaborasi.

panda tidak mengimplementasikan fungsi pemodelan yang signifikan di luar regresi linier dan panel; untuk ini, lihat statsmodels dan scikit-learn . Lebih banyak pekerjaan masih diperlukan untuk membuat Python lingkungan pemodelan statistik kelas pertama, tetapi kami sedang dalam perjalanan menuju tujuan itu.

Apa yang dikatakan pengguna kami? 
Logo Manajemen Modal AQR
Roni Israelov, PhD
Manajer portofolio
AQR Capital Management
“ Panda memungkinkan kami untuk lebih fokus pada penelitian dan lebih sedikit pada pemrograman. Kami menemukan panda mudah dipelajari, mudah digunakan, dan mudah dirawat. Intinya adalah itu telah meningkatkan produktivitas kami. "

Logo AppNexus
David Himrod
Direktur Pengoptimalan & Analisis
AppNexus
“ Panda adalah alat yang sempurna untuk menjembatani kesenjangan antara iterasi cepat analisis ad-hoc dan kode kualitas produksi. Jika Anda ingin satu alat untuk digunakan di seluruh organisasi multi-disiplin insinyur, matematikawan dan analis, tidak perlu mencari lebih jauh. ”

Datadog Logo
Olivier Pomel
CEO
Datadog
“Kami menggunakan panda untuk memproses data deret waktu pada server produksi kami. Kesederhanaan dan keanggunan API-nya, dan tingkat kinerjanya yang tinggi untuk dataset bervolume tinggi, menjadikannya pilihan yang sempurna bagi kami. ”
