Miniconda 

Instruksi instalasi

Sumber daya lain:

Miniconda dengan Python 3.7 untuk Power8 & Power9
Miniconda dengan Python 2.7 untuk Power8 & Power9
Gambar Miniconda Docker
Gambar Miniconda AWS
Jumlah arsip dan MD5 untuk installer
log perubahan konda
Installer Miniconda ini berisi manajer paket conda dan Python. Setelah Miniconda diinstal, Anda dapat menggunakan perintah conda untuk menginstal paket lain dan membuat lingkungan, dll. Misalnya:

$ conda install numpy
...
$ conda create -n py3k anaconda python=3
...
Ada dua varian installer: Miniconda berbasis Python 2 dan Miniconda3 berbasis Python 3. Perhatikan bahwa pilihan Miniconda yang dipasang hanya mempengaruhi lingkungan root. Terlepas dari versi Miniconda yang Anda instal, Anda masih dapat menginstal kedua lingkungan Python 2.x dan Python 3.x.

Perbedaan lainnya adalah bahwa Python 3 versi Miniconda akan menjadi default untuk Python 3 saat membuat lingkungan baru dan paket-paket bangunan. Jadi misalnya, perilaku

$ conda create -n myenv python
akan menginstal Python 2.7 dengan Python 2 Miniconda dan menginstal Python 3.7 dengan Python 3 Miniconda. Anda dapat mengganti default dengan pengaturan python=2atau secara eksplisit python=3. Ini juga menentukan nilai default CONDA_PYsaat menggunakan .conda build

Catatan : Jika Anda sudah memasang Miniconda atau Anaconda, dan Anda hanya ingin memutakhirkan, Anda sebaiknya tidak menggunakan penginstal. Cukup gunakan . Contohnyaconda update

$ conda update conda
akan memperbarui conda.
