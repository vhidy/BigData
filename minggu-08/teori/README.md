panda: toolkit analisis data Python yang kuat 
Versi PDF

Zipped HTML

Tanggal : 05 Agustus 2018 Versi : 0.23.4

Biner Installer: https://pypi.org/project/pandas

Sumber Repositori: http://github.com/pandas-dev/pandas

Masalah & Ide: https://github.com/pandas-dev/pandas/issues

Dukungan Q & A: http://stackoverflow.com/questions/tagged/pandas

Mailing List Pengembang: http://groups.google.com/group/pydata

panda adalah paket Python yang menyediakan struktur data yang cepat, fleksibel, dan ekspresif yang dirancang untuk membuat bekerja dengan data "relasional" atau "berlabel" mudah dan intuitif. Ini bertujuan untuk menjadi blok bangunan tingkat tinggi yang fundamental untuk melakukan analisis data dunia nyata secara praktis dengan Python. Selain itu, ia memiliki tujuan yang lebih luas untuk menjadi alat analisis / manipulasi data open source yang paling kuat dan fleksibel yang tersedia dalam bahasa apa pun . Sudah dalam perjalanan menuju tujuan ini.

panda sangat cocok untuk berbagai jenis data:

Data tabular dengan kolom-kolom yang diketik secara heterogen, seperti dalam tabel SQL atau spreadsheet Excel
Data deret waktu teratur dan tidak teratur (tidak harus tetap-frekuensi).
Data matriks arbitrer (diketik secara homogen atau heterogen) dengan label baris dan kolom
Bentuk lain dari kumpulan data observasi / statistik. Data sebenarnya tidak perlu diberi label sama sekali untuk ditempatkan ke dalam struktur data panda
Dua struktur data utama panda, Series(1-dimensi) dan DataFrame(2-dimensi), menangani sebagian besar kasus penggunaan umum di bidang keuangan, statistik, ilmu sosial, dan banyak bidang rekayasa. Untuk pengguna R, DataFrameberikan semua yang disediakan oleh R data.framedan banyak lagi. panda dibangun di atas NumPy dan dimaksudkan untuk berintegrasi dengan baik dalam lingkungan komputasi ilmiah dengan banyak pustaka pihak ke-3 lainnya.

Berikut beberapa hal yang dilakukan panda dengan baik:

Mudah penanganan data yang hilang (diwakili sebagai NaN) di floating point serta data titik non-floating
Ukuran berubah: kolom dapat disisipkan dan dihapus dari DataFrame dan objek dimensi yang lebih tinggi
Penyelarasan data otomatis dan eksplisit : objek dapat secara eksplisit disejajarkan dengan serangkaian label, atau pengguna dapat mengabaikan label dan membiarkan Seri , DataFrame , dll. Secara otomatis menyesuaikan data untuk Anda dalam perhitungan
Kelompok yang kuat dan fleksibel dengan fungsi untuk melakukan operasi split-apply-combine pada set data, baik untuk menggabungkan dan mengubah data
Buatlah mudah untuk mengkonversi data yang compang-camping dan berbeda-indeks dalam struktur data Python dan NumPy lainnya menjadi objek DataFrame
Pengiris berbasis label cerdas , pengindeksan mewah , dan subset kumpulan data besar
Intuitif penggabungan dan bergabung set data
Pembentukan ulang dan pengalihan set data yang fleksibel
Pelabelan yang bersifat hierarkis (mungkin memiliki banyak label per tick)
Alat IO yang kuat untuk memuat data dari file datar (CSV dan delimited), file Excel, database, dan menyimpan / memuat data dari format HDF5 ultra cepat
Fungsionalitas seri waktu tertentu: rentang tanggal pembuatan dan konversi frekuensi, statistik jendela bergerak, regresi linier jendela bergerak, pemindahan dan kelambatan tanggal, dll.
Banyak dari prinsip-prinsip ini di sini untuk mengatasi kekurangan yang sering dialami menggunakan bahasa lain / lingkungan penelitian ilmiah. Untuk ilmuwan data, bekerja dengan data biasanya dibagi menjadi beberapa tahap: memabukkan dan membersihkan data, menganalisis / memodelkannya, kemudian mengatur hasil analisis ke dalam bentuk yang cocok untuk merencanakan atau menampilkan tabular. panda adalah alat yang ideal untuk semua tugas ini.

Beberapa catatan lain

panda cepat . Banyak bit algoritmik tingkat rendah telah banyak dimodifikasi dalam kode Cython . Namun, seperti halnya generalisasi lain biasanya mengorbankan kinerja. Jadi jika Anda fokus pada satu fitur untuk aplikasi Anda, Anda mungkin dapat membuat alat khusus yang lebih cepat.
panda adalah ketergantungan statsmodels , menjadikannya bagian penting dari ekosistem komputasi statistik dengan Python.
panda telah digunakan secara luas dalam produksi dalam aplikasi keuangan.
