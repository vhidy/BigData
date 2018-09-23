2. Menggunakan Interpreter Python 
2.1. Meminjam Interpreter 
Interpreter Python biasanya diinstal seperti /usr/local/bin/python3.7 pada mesin-mesin di mana tersedia; menempatkan /usr/local/bindi jalur pencarian shell Unix Anda memungkinkan untuk memulainya dengan mengetikkan perintah:

python3.7
ke shell. [1] Karena pilihan direktori tempat tinggal penerjemah adalah opsi instalasi, tempat lain dimungkinkan; periksa dengan guru Python lokal atau administrator sistem Anda. (Misalnya, /usr/local/pythonadalah lokasi alternatif yang populer.)

Pada mesin Windows, instalasi Python biasanya ditempatkan di C:\Python36, meskipun Anda dapat mengubah ini ketika Anda menjalankan penginstal. Untuk menambahkan direktori ini ke jalan Anda, Anda dapat mengetikkan perintah berikut ke dalam prompt perintah dalam kotak DOS:

set path=%path%;C:\python36
Mengetik karakter akhir-file ( Control-Dpada Unix, Control-Zpada Windows) pada prompt utama menyebabkan interpreter untuk keluar dengan status keluar nol. Jika itu tidak berhasil, Anda dapat keluar penafsir dengan mengetikkan perintah berikut: quit().

Fitur pengeditan garis interpreter termasuk penyuntingan interaktif, substitusi sejarah dan penyelesaian kode pada sistem yang mendukung readline. Mungkin pemeriksaan tercepat untuk melihat apakah pengeditan baris perintah didukung adalah mengetik Control-Pke prompt Python pertama yang Anda dapatkan. Jika berbunyi, Anda memiliki pengeditan baris perintah; lihat Lampiran Pengeditan Input Interaktif dan Substitusi Riwayat untuk pengenalan kunci. Jika tidak ada yang terjadi, atau jika di ^P-echo, pengeditan baris perintah tidak tersedia; Anda hanya dapat menggunakan backspace untuk menghapus karakter dari baris saat ini.

Interpreter beroperasi agak seperti shell Unix: ketika dipanggil dengan input standar yang terhubung ke perangkat tty, ia membaca dan menjalankan perintah secara interaktif; ketika dipanggil dengan argumen nama file atau dengan file sebagai input standar, ia membaca dan mengeksekusi skrip dari file itu.

Cara kedua untuk memulai interpreter adalah , yang mengeksekusi pernyataan dalam perintah , analog dengan opsi shell . Karena pernyataan Python sering mengandung spasi atau karakter lain yang khusus untuk shell, biasanya disarankan untuk mengutip perintah secara keseluruhan dengan tanda kutip tunggal.python -c command [arg] ...-c

Beberapa modul Python juga berguna sebagai skrip. Ini dapat dipanggil menggunakan , yang mengeksekusi file sumber untuk modul seolah-olah Anda telah mengeja nama lengkapnya pada baris perintah.python -m module [arg] ...

Ketika file skrip digunakan, kadang-kadang berguna untuk dapat menjalankan skrip dan masuk ke mode interaktif setelahnya. Ini bisa dilakukan dengan melewatkan -i sebelum naskah.

Semua opsi baris perintah dijelaskan dalam baris Perintah dan lingkungan .

2.1.1. Argumen Lewat 
Ketika diketahui oleh interpreter, nama skrip dan argumen tambahan sesudahnya diubah menjadi daftar string dan ditetapkan ke argv variabel dalam sysmodul. Anda dapat mengakses daftar ini dengan mengeksekusi . Panjang daftar setidaknya satu; ketika tidak ada skrip dan tidak ada argumen yang diberikan, adalah string kosong. Ketika nama skrip diberikan sebagai (berarti input standar), diatur ke . Ketika perintah digunakan, diatur ke . Ketika modul digunakan, diatur ke nama lengkap dari modul yang ada. Pilihan yang ditemukan setelah perintah atau modul tidak dikonsumsi oleh pemrosesan opsi juru bahasa Python, tetapi tersisa diimport syssys.argv[0]'-'sys.argv[0]'-'-c sys.argv[0]'-c'-m sys.argv[0]-c -m sys.argv untuk perintah atau modul untuk ditangani.

2.1.2. Mode Interaktif 
Ketika perintah dibaca dari tty, interpreter dikatakan dalam mode interaktif . Dalam mode ini meminta perintah berikutnya dengan prompt utama , biasanya tiga lebih besar dari tanda ( >>>); untuk garis lanjutan, akan muncul prompt sekunder , secara default tiga titik ( ...). Interpreter mencetak pesan selamat datang yang menyatakan nomor versi dan pemberitahuan hak cipta sebelum mencetak prompt pertama:

$ python3.7
Python 3.7 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
Garis lanjutan diperlukan saat memasukkan konstruksi multi-garis. Sebagai contoh, lihatlah ifpernyataan ini :

>>>
>>> the_world_is_flat = True
>>> if the_world_is_flat:
...     print("Be careful not to fall off!")
...
Be careful not to fall off!
Untuk lebih lanjut tentang mode interaktif, lihat Mode Interaktif .

2.2. Interpreter dan Lingkungannya 
2.2.1. Pengodean Kode Sumber 
Secara default, file sumber Python diperlakukan sebagai dikodekan dalam UTF-8. Dalam pengkodean itu, karakter sebagian besar bahasa di dunia dapat digunakan secara bersamaan dalam string literal, pengidentifikasi dan komentar - meskipun pustaka standar hanya menggunakan karakter ASCII untuk pengenal, sebuah konvensi yang harus diikuti oleh kode portabel apa pun. Untuk menampilkan semua karakter ini dengan benar, editor Anda harus mengenali bahwa file tersebut UTF-8, dan itu harus menggunakan font yang mendukung semua karakter dalam file.

Untuk menyatakan pengkodean selain yang default, baris komentar khusus harus ditambahkan sebagai baris pertama file. Sintaksnya adalah sebagai berikut:

# -*- coding: encoding -*-
dimana pengkodean adalah salah satu yang sah codecsdidukung oleh Python.

Misalnya, untuk menyatakan bahwa pengkodean Windows-1252 akan digunakan, baris pertama file kode sumber Anda harus:

# -*- coding: cp1252 -*-
Satu pengecualian untuk aturan baris pertama adalah ketika kode sumber dimulai dengan garis "shebang" UNIX . Dalam hal ini, deklarasi pengkodean harus ditambahkan sebagai baris kedua file. Sebagai contoh:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-

3. Pengenalan Informal terhadap Python 
Dalam contoh-contoh berikut, input dan output dibedakan oleh ada atau tidaknya prompt ( >>> dan ... ): untuk mengulang contoh, Anda harus mengetik semuanya setelah prompt, ketika muncul prompt; baris yang tidak dimulai dengan prompt adalah output dari interpreter. Perhatikan bahwa prompt sekunder pada baris dengan sendirinya dalam contoh berarti Anda harus mengetikkan baris kosong; ini digunakan untuk mengakhiri perintah multi-baris.

Banyak contoh dalam manual ini, bahkan yang dimasukkan pada prompt interaktif, termasuk komentar. Komentar di Python mulai dengan karakter hash #,, dan meluas ke ujung garis fisik. Sebuah komentar dapat muncul di awal baris atau mengikuti spasi atau kode, tetapi tidak dalam string literal. Karakter hash dalam string literal hanyalah karakter hash. Karena komentar adalah untuk mengklarifikasi kode dan tidak ditafsirkan oleh Python, mereka dapat dihilangkan ketika mengetikkan contoh.

Beberapa contoh:

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
3.1. Menggunakan Python sebagai Kalkulator 
Mari kita coba beberapa perintah Python sederhana. Jalankan interpreter dan tunggu prompt utama >>>,. (Tidak boleh lama.)

3.1.1. Angka 
Interpreter bertindak sebagai kalkulator sederhana: Anda dapat mengetikkan ekspresi pada itu dan itu akan menulis nilai. Sintaks ekspresi sangat mudah: operator +, -, *dan /bekerja sama seperti dalam kebanyakan bahasa lain (misalnya, Pascal atau C); tanda kurung ( ()) dapat digunakan untuk pengelompokan. Sebagai contoh:

>>>
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5  # division always returns a floating point number
1.6
Angka-angka bilangan bulat (misalnya 2, 4, 20) memiliki jenis int, yang dengan bagian pecahan (misalnya 5.0, 1.6) memiliki tipe float. Kita akan melihat lebih banyak tentang tipe numerik nanti di tutorial.

Division ( /) selalu mengembalikan float. Untuk melakukan pembagian lantai dan mendapatkan hasil integer (membuang hasil pecahan) Anda dapat menggunakan // operator; untuk menghitung sisa yang dapat Anda gunakan %:

>>>
>>> 17 / 3  # classic division returns a float
5.666666666666667
>>>
>>> 17 // 3  # floor division discards the fractional part
5
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17
Dengan Python, adalah mungkin untuk menggunakan **operator untuk menghitung kekuatan [1] :

>>>
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128
Tanda sama ( =) digunakan untuk menetapkan nilai ke variabel. Setelah itu, tidak ada hasil yang ditampilkan sebelum prompt interaktif berikutnya:

>>>
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
Jika sebuah variabel tidak "didefinisikan" (diberi nilai), mencoba menggunakannya akan memberi Anda kesalahan:

>>>
>>> n  # try to access an undefined variable
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'n' is not defined
Ada dukungan penuh untuk floating point; operator dengan operan jenis campuran mengonversi operan bilangan bulat ke titik mengambang:

>>>
>>> 4 * 3.75 - 1
14.0
Dalam mode interaktif, ekspresi tercetak terakhir ditetapkan ke variabel _. Ini berarti bahwa ketika Anda menggunakan Python sebagai kalkulator meja, itu agak lebih mudah untuk melanjutkan perhitungan, misalnya:

>>>
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
Variabel ini harus diperlakukan sebagai hanya-baca oleh pengguna. Jangan secara eksplisit menetapkan nilai untuk itu - Anda akan membuat variabel lokal independen dengan nama yang sama dengan masking variabel bawaan dengan perilaku sihirnya.

Selain intdan float, Python mendukung jenis angka lain, seperti Decimaldan Fraction. Python juga memiliki dukungan built-in untuk bilangan kompleks , dan menggunakan jatau Jsufiks untuk menunjukkan bagian imajiner (misalnya 3+5j).

3.1.2. String 
Selain angka, Python juga dapat memanipulasi string, yang dapat diekspresikan dalam beberapa cara. Mereka dapat dilampirkan dalam tanda kutip tunggal ( '...') atau tanda kutip ganda ( "...") dengan hasil yang sama [2] . \dapat digunakan untuk menghindari tanda kutip:

>>>
>>> 'spam eggs'  # single quotes
'spam eggs'
>>> 'doesn\'t'  # use \' to escape the single quote...
"doesn't"
>>> "doesn't"  # ...or use double quotes instead
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
Dalam interpreter interaktif, string output diapit dalam tanda kutip dan karakter khusus diloloskan dengan backslashes. Meskipun ini kadang-kadang terlihat berbeda dari input (tanda kutip yang terlampir dapat berubah), kedua string ini setara. String ini dilingkupi dalam tanda kutip ganda jika string tersebut berisi satu kutipan dan tidak ada tanda kutip ganda, jika tidak maka akan dikurung dalam tanda kutip tunggal. The print()Fungsi menghasilkan output lebih mudah dibaca, dengan menghilangkan tanda kutip melampirkan dan dengan mencetak melarikan diri dan karakter khusus:

>>>
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'  # \n means newline
>>> s  # without print(), \n is included in the output
'First line.\nSecond line.'
>>> print(s)  # with print(), \n produces a new line
First line.
Second line.
Jika Anda tidak ingin karakter diawali oleh \untuk ditafsirkan sebagai karakter khusus, Anda dapat menggunakan string mentah dengan menambahkan rsebelum kutipan pertama:

>>>
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
Literal string dapat menjangkau banyak baris. Salah satu cara adalah menggunakan triple-quotes: """..."""atau '''...'''. Ujung garis secara otomatis termasuk dalam string, tetapi mungkin untuk mencegah hal ini dengan menambahkan \di akhir baris. Contoh berikut:

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
menghasilkan output berikut (perhatikan bahwa baris baru awal tidak termasuk):

Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
String dapat digabung (direkatkan) dengan +operator, dan diulangi dengan *:

>>>
>>> # 3 times 'un', followed by 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
Dua atau lebih literal string (yaitu yang terlampir di antara tanda kutip) di samping satu sama lain secara otomatis digabung.

>>>
>>> 'Py' 'thon'
'Python'
Fitur ini sangat berguna ketika Anda ingin mematahkan string panjang:

>>>
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
Ini hanya bekerja dengan dua literal, bukan dengan variabel atau ekspresi:

>>>
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  File "<stdin>", line 1
    prefix 'thon'
                ^
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  File "<stdin>", line 1
    ('un' * 3) 'ium'
                   ^
SyntaxError: invalid syntax
Jika Anda ingin menggabungkan variabel atau variabel dan literal, gunakan +:

>>>
>>> prefix + 'thon'
'Python'
String dapat diindeks (subscript), dengan karakter pertama memiliki indeks 0. Tidak ada jenis karakter yang terpisah; karakter hanyalah string ukuran satu:

>>>
>>> word = 'Python'
>>> word[0]  # character in position 0
'P'
>>> word[5]  # character in position 5
'n'
Indeks mungkin juga angka negatif, untuk mulai menghitung dari kanan:

>>>
>>> word[-1]  # last character
'n'
>>> word[-2]  # second-last character
'o'
>>> word[-6]
'P'
Perhatikan bahwa sejak -0 sama dengan 0, indeks negatif mulai dari -1.

Selain pengindeksan, mengiris juga didukung. Saat pengindeksan digunakan untuk mendapatkan karakter individu, mengiris memungkinkan Anda untuk mendapatkan substring:

>>>
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
>>> word[2:5]  # characters from position 2 (included) to 5 (excluded)
'tho'
Perhatikan bagaimana awal selalu disertakan, dan akhirnya selalu dikecualikan. Ini memastikan bahwa selalu sama dengan :s[:i] + s[i:]s

>>>
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
Indeks slice memiliki default yang berguna; default indeks pertama yang dihilangkan ke nol, default indeks kedua yang dihilangkan dengan ukuran string yang diiris.

>>>
>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
Salah satu cara untuk mengingat cara kerja irisan adalah dengan memikirkan indeks sebagai penunjuk antara karakter, dengan tepi kiri karakter pertama bernomor 0. Kemudian tepi kanan karakter terakhir string n karakter memiliki indeks n , misalnya:

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
Baris angka pertama memberikan posisi indeks 0… 6 dalam string; baris kedua memberikan indeks negatif yang sesuai. Potongan dari i ke j terdiri dari semua karakter antara tepi berlabel i dan j , masing-masing.

Untuk indeks non-negatif, panjang irisan adalah perbedaan indeks, jika keduanya dalam batas. Misalnya, panjangnya word[1:3]adalah 2.

Mencoba menggunakan indeks yang terlalu besar akan menghasilkan kesalahan:

>>>
>>> word[42]  # the word only has 6 characters
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
Namun, di luar rentang indeks slice ditangani dengan anggun saat digunakan untuk mengiris:

>>>
>>> word[4:42]
'on'
>>> word[42:]
''
String Python tidak dapat diubah - mereka tidak dapat diubah . Oleh karena itu, menetapkan ke posisi indeks dalam string menghasilkan kesalahan:

>>>
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
Jika Anda membutuhkan string yang berbeda, Anda harus membuat yang baru:

>>>
>>> 'J' + word[1:]
'Jython'
>>> word[:2] + 'py'
'Pypy'
Fungsi len()bawaan mengembalikan panjang string:

>>>
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
Lihat juga
Jenis Urutan Teks - str
String adalah contoh jenis urutan , dan mendukung operasi umum yang didukung oleh jenis tersebut.
Metode String
Strings mendukung sejumlah besar metode untuk transformasi dan pencarian dasar.
Literal string terformat
Literal string yang memiliki ekspresi yang tertanam.
Sintaks String Format
Informasi tentang pemformatan string dengan str.format().
Pemformatan String bergaya printf
Operasi pemformatan lama yang dipanggil saat string adalah operan kiri %operator dijelaskan secara lebih terperinci di sini.
3.1.3. Daftar 
Python mengetahui sejumlah tipe data majemuk , yang digunakan untuk mengelompokkan nilai-nilai lainnya. Yang paling serbaguna adalah daftar , yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Daftar mungkin berisi item dari berbagai jenis, tetapi biasanya semua item memiliki tipe yang sama.

>>>
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
Seperti string (dan semua tipe urutan bawaan lainnya), daftar dapat diindeks dan diiris:

>>>
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
Semua operasi slice mengembalikan daftar baru yang berisi elemen yang diminta. Ini berarti bahwa potongan berikut mengembalikan salinan daftar baru (dangkal):

>>>
>>> squares[:]
[1, 4, 9, 16, 25]
Daftar juga mendukung operasi seperti penggabungan:

>>>
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Tidak seperti string, yang tidak dapat diubah , daftar adalah jenis yang bisa berubah , yaitu dimungkinkan untuk mengubah kontennya:

>>>
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
Anda juga dapat menambahkan item baru di akhir daftar, dengan menggunakan append() metode (kita akan melihat lebih banyak tentang metode nanti):

>>>
>>> cubes.append(216)  # add the cube of 6
>>> cubes.append(7 ** 3)  # and the cube of 7
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
Tugas ke irisan juga dimungkinkan, dan ini bahkan dapat mengubah ukuran daftar atau menghapusnya sepenuhnya:

>>>
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> # replace some values
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> # now remove them
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> # clear the list by replacing all the elements with an empty list
>>> letters[:] = []
>>> letters
[]
Fungsi len()bawaan juga berlaku untuk daftar:

>>>
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
Anda dapat menyusun daftar (membuat daftar yang berisi daftar lain), misalnya:

>>>
>>> a = ['a', 'b', 'c']
>>> n = [1, 2, 3]
>>> x = [a, n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
3.2. Langkah Pertama Menuju Pemrograman 
Tentu saja, kita dapat menggunakan Python untuk tugas yang lebih rumit daripada menambahkan dua dan dua secara bersamaan. Misalnya, kita dapat menulis sub-urutan awal deret Fibonacci sebagai berikut:

>>>
>>> # Fibonacci series:
... # the sum of two elements defines the next
... a, b = 0, 1
>>> while a < 10:
...     print(a)
...     a, b = b, a+b
...
0
1
1
2
3
5
8
Contoh ini memperkenalkan beberapa fitur baru.

Baris pertama berisi beberapa tugas : variabel adan b secara bersamaan mendapatkan nilai baru 0 dan 1. Pada baris terakhir ini digunakan lagi, menunjukkan bahwa ekspresi di sisi kanan semua dievaluasi terlebih dahulu sebelum salah satu tugas berlangsung . Ekspresi sisi kanan dievaluasi dari kiri ke kanan.

The whileLoop mengeksekusi selama kondisi (di sini: ) tetap benar. Dalam Python, seperti dalam C, nilai integer non-nol adalah benar; nol salah. Kondisi ini juga bisa berupa nilai string atau daftar, sebenarnya setiap urutan; apa pun dengan panjang non-nol adalah benar, urutan kosong adalah salah. Tes yang digunakan dalam contoh adalah perbandingan sederhana. Operator pembanding standar ditulis sama seperti di C: (kurang dari), (lebih besar dari), (sama dengan), (kurang dari atau sama dengan), (lebih besar dari atau sama dengan) dan (tidak sama dengan).a < 10<>==<=>=!=

The tubuh dari loop adalah menjorok : lekukan cara Python pengelompokan pernyataan. Pada prompt interaktif, Anda harus mengetikkan tab atau spasi untuk setiap baris indentasi. Dalam prakteknya Anda akan menyiapkan masukan yang lebih rumit untuk Python dengan editor teks; semua editor teks yang layak memiliki fasilitas auto-indent. Ketika pernyataan gabungan dimasukkan secara interaktif, itu harus diikuti oleh garis kosong untuk menunjukkan selesai (karena parser tidak bisa menebak ketika Anda mengetik baris terakhir). Perhatikan bahwa setiap baris dalam blok dasar harus diberi indentasi dengan jumlah yang sama.

The print()Fungsi menulis nilai argumen (s) itu diberikan. Ini berbeda dari hanya menulis ekspresi yang ingin Anda tulis (seperti yang kami lakukan sebelumnya dalam contoh-contoh kalkulator) dalam cara menangani banyak argumen, kuantitas floating point, dan string. String dicetak tanpa tanda kutip, dan spasi disisipkan di antara item, sehingga Anda dapat memformat semuanya dengan baik, seperti ini:

>>>
>>> i = 256*256
>>> print('The value of i is', i)
The value of i is 65536
Argumen kata kunci akhir dapat digunakan untuk menghindari baris setelah output, atau mengakhiri output dengan string yang berbeda:

>>>
>>> a, b = 0, 1
>>> while a < 1000:
...     print(a, end=',')
...     a, b = b, a+b
...
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

4. Alat Kontrol Aliran Lainnya 
Selain whilepernyataan yang baru saja diperkenalkan, Python mengetahui pernyataan aliran kontrol yang biasa dikenal dari bahasa lain, dengan beberapa tikungan.

4.1. ifPernyataan 
Mungkin jenis pernyataan yang paling terkenal adalah ifpernyataannya. Sebagai contoh:

>>>
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More
Bisa ada nol atau lebih elifbagian, dan elsebagian itu opsional. Kata kunci ' elif' singkatan dari 'else if', dan berguna untuk menghindari indentasi yang berlebihan. Sebuah if... elif... elif... urutan adalah pengganti untuk switchatau casepernyataan yang ditemukan dalam bahasa lain.

4.2. forPernyataan 
The forpernyataan dalam Python berbeda sedikit dari apa yang Anda dapat digunakan untuk di C atau Pascal. Daripada selalu iterasi atas deret aritmetika angka (seperti dalam Pascal), atau memberikan pengguna kemampuan untuk menentukan baik langkah iterasi dan kondisi terputus (seperti C), forpernyataan Python iterates atas item dari setiap urutan (daftar atau string), dalam urutan yang muncul dalam urutan. Misalnya (tidak ada kata yang dimaksudkan):

>>>
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
Jika Anda perlu memodifikasi urutan Anda melakukan iterasi saat berada di dalam loop (misalnya untuk menggandakan item yang dipilih), Anda disarankan untuk membuat salinan terlebih dahulu. Iterasi atas urutan tidak secara implisit membuat salinan. Notasi slice membuat ini sangat nyaman:

>>>
>>> for w in words[:]:  # Loop over a slice copy of the entire list.
...     if len(w) > 6:
...         words.insert(0, w)
...
>>> words
['defenestrate', 'cat', 'window', 'defenestrate']
Dengan , contoh akan berusaha membuat daftar tak terbatas, memasukkan berulang-ulang.for w in words:defenestrate

4.3. The range()Fungsi 
Jika Anda perlu mengulangi urutan angka, fungsi range()bawaan akan berguna. Ini menghasilkan progresi aritmetika:

>>>
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan; range(10)menghasilkan 10 nilai, indeks hukum untuk item dari urutan panjang 10. Hal ini dimungkinkan untuk membiarkan rentang mulai pada nomor lain, atau untuk menentukan kenaikan yang berbeda (bahkan negatif; kadang-kadang ini disebut 'langkah'):

range(5, 10)
   5, 6, 7, 8, 9

range(0, 10, 3)
   0, 3, 6, 9

range(-10, -100, -30)
  -10, -40, -70
Untuk beralih ke indeks urutan, Anda dapat menggabungkan range()dan len()sebagai berikut:

>>>
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
Dalam kebanyakan kasus seperti itu, bagaimanapun, akan lebih mudah untuk menggunakan enumerate() fungsi, lihat Teknik Looping .

Suatu hal yang aneh terjadi jika Anda hanya mencetak rentang:

>>>
>>> print(range(10))
range(0, 10)
Dalam banyak hal, objek itu dikembalikan oleh range()berperilaku seolah-olah itu adalah daftar, tetapi sebenarnya tidak. Ini adalah objek yang mengembalikan item berurutan dari urutan yang diinginkan ketika Anda mengulanginya, tetapi itu tidak benar-benar membuat daftar, sehingga menghemat ruang.

Kami mengatakan objek seperti itu dapat diulang , yaitu, cocok sebagai target untuk fungsi dan konstruksi yang mengharapkan sesuatu dari mana mereka dapat memperoleh item berurutan sampai persediaan habis. Kami telah melihat bahwa forpernyataan itu adalah iterator seperti itu . Fungsi list() itu lain; itu membuat daftar dari iterables:

>>>
>>> list(range(5))
[0, 1, 2, 3, 4]
Nanti kita akan melihat lebih banyak fungsi yang mengembalikan iterables dan mengambil iterables sebagai argumen.

4.4. breakdan continuePernyataan, dan elseKlausul tentang Loops 
The breakpernyataan, seperti di C, pecah dari melampirkan terdalam foratau whilelingkaran.

Pernyataan loop mungkin memiliki elseklausa; itu dijalankan ketika loop berakhir karena kelelahan list (dengan for) atau ketika kondisi menjadi false (dengan while), tetapi tidak ketika loop diakhiri oleh sebuah breakpernyataan. Ini dicontohkan oleh loop berikut, yang mencari bilangan prima:

>>>
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
(Ya, ini adalah kode yang benar Lihatlah erat. Yang elseklausul milik forlingkaran, bukan yang if. Pernyataan)

Ketika digunakan dengan loop, elseklausa memiliki lebih banyak kesamaan dengan elseklausa trypernyataan daripada yang dilakukannya dari ifpernyataan: klausa trypernyataan elseberjalan ketika tidak ada pengecualian terjadi, dan elseklausa loop berjalan ketika tidak ada break terjadi. Untuk keterangan lebih lanjut tentang trypernyataan dan pengecualian, lihat Penanganan Pengecualian .

The continuepernyataan, juga dipinjam dari C, berlanjut dengan iterasi berikutnya dari loop:

>>>
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
4.5. passPernyataan 
The passpernyataan tidak apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. Sebagai contoh:

>>>
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
Ini biasanya digunakan untuk membuat kelas minimal:

>>>
>>> class MyEmptyClass:
...     pass
...
Tempat lain yang passdapat digunakan adalah sebagai tempat-pemegang untuk fungsi atau tubuh bersyarat ketika Anda bekerja pada kode baru, memungkinkan Anda untuk terus berpikir pada tingkat yang lebih abstrak. The passdiam-diam diabaikan:

>>>
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
4.6. Mendefinisikan Fungsi 
Kita dapat membuat fungsi yang menulis deret Fibonacci ke batas yang sewenang-wenang:

>>>
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
Kata kunci defmemperkenalkan definisi fungsi . Ini harus diikuti oleh nama fungsi dan daftar parameter formal yang disisipkan. Pernyataan yang membentuk badan fungsi dimulai pada baris berikutnya, dan harus dijorok.

Pernyataan pertama dari badan fungsi dapat secara opsional berupa string literal; string literal ini adalah string dokumentasi fungsi, atau docstring . (Lebih lanjut tentang docstrings dapat ditemukan di bagian String Dokumentasi .) Ada alat-alat yang menggunakan docstrings untuk secara otomatis menghasilkan dokumentasi online atau dicetak, atau membiarkan pengguna secara interaktif menelusuri kode; Ini adalah praktik yang baik untuk memasukkan aturan dalam kode yang Anda tulis, jadi biasakanlah.

The eksekusi dari suatu fungsi memperkenalkan tabel simbol baru yang digunakan untuk variabel lokal dari fungsi. Lebih tepatnya, semua tugas variabel dalam fungsi menyimpan nilai dalam tabel simbol lokal; sedangkan referensi variabel pertama kali terlihat di tabel simbol lokal, kemudian di tabel simbol lokal melampirkan fungsi, kemudian di tabel simbol global, dan akhirnya di tabel nama built-in. Dengan demikian, variabel global tidak dapat secara langsung diberikan nilai dalam fungsi (kecuali disebutkan dalam globalpernyataan), meskipun mereka dapat direferensikan.

Parameter aktual (argumen) ke pemanggilan fungsi diperkenalkan dalam tabel simbol lokal dari fungsi yang dipanggil ketika dipanggil; dengan demikian, argumen dilewatkan menggunakan panggilan oleh nilai (di mana nilai selalu merupakan referensi objek , bukan nilai objek). [1] Ketika suatu fungsi memanggil fungsi lain, tabel simbol lokal baru dibuat untuk panggilan itu.

Definisi fungsi memperkenalkan nama fungsi dalam tabel simbol saat ini. Nilai dari nama fungsi memiliki tipe yang dikenali oleh interpreter sebagai fungsi yang ditentukan pengguna. Nilai ini dapat ditetapkan ke nama lain yang kemudian dapat juga digunakan sebagai fungsi. Ini berfungsi sebagai mekanisme penggantian nama umum:

>>>
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
Datang dari bahasa lain, Anda mungkin keberatan bahwa fibitu bukan fungsi tetapi prosedur karena tidak mengembalikan nilai. Bahkan, bahkan fungsi tanpa returnpernyataan mengembalikan nilai, meskipun agak membosankan. Nilai ini disebut None(ini adalah nama bawaan). Menulis nilai Nonebiasanya ditekan oleh penerjemah jika itu adalah satu-satunya nilai yang ditulis. Anda dapat melihatnya jika Anda benar-benar ingin menggunakan print():

>>>
>>> fib(0)
>>> print(fib(0))
None
Sangat mudah untuk menulis fungsi yang mengembalikan daftar nomor seri Fibonacci, daripada mencetaknya:

>>>
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Contoh ini, seperti biasa, menunjukkan beberapa fitur Python baru:

The returnpernyataan kembali dengan nilai dari fungsi. returntanpa argumen ekspresi kembali None. Jatuh dari ujung fungsi juga kembali None.
Pernyataan itu result.append(a)memanggil metode objek daftar result. Metode adalah fungsi yang 'milik' untuk suatu objek dan diberi nama obj.methodname, di mana objada beberapa objek (ini mungkin berupa ekspresi), dan methodnamemerupakan nama metode yang ditentukan oleh jenis objek. Berbagai jenis menentukan metode yang berbeda. Metode dari berbagai tipe dapat memiliki nama yang sama tanpa menyebabkan ambiguitas. (Dimungkinkan untuk menentukan jenis dan metode objek Anda sendiri, menggunakan kelas , lihat Kelas ) Metode yang append()ditunjukkan pada contoh didefinisikan untuk objek daftar; itu menambahkan elemen baru di akhir daftar. Dalam contoh ini setara dengan , tetapi lebih efisien.result = result + [a]
4,7. Lebih lanjut tentang Mendefinisikan Fungsi 
Juga dimungkinkan untuk mendefinisikan fungsi dengan sejumlah argumen variabel. Ada tiga bentuk, yang bisa digabungkan.

4.7.1. Nilai Argumen Default 
Formulir yang paling berguna adalah menentukan nilai default untuk satu atau lebih argumen. Ini menciptakan fungsi yang dapat dipanggil dengan argumen yang lebih sedikit daripada yang ditentukan untuk diizinkan. Sebagai contoh:

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
Fungsi ini dapat dipanggil dengan beberapa cara:

hanya memberikan argumen wajib: ask_ok('Do you really want to quit?')
memberikan salah satu argumen opsional: ask_ok('OK to overwrite the file?', 2)
atau bahkan memberikan semua argumen: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
Contoh ini juga memperkenalkan inkata kunci. Ini menguji apakah suatu urutan mengandung nilai tertentu atau tidak.

Nilai-nilai default dievaluasi pada titik definisi fungsi dalam ruang lingkup yang menentukan , sehingga

i = 5

def f(arg=i):
    print(arg)

i = 6
f()
akan dicetak 5.

Peringatan penting: Nilai default hanya dievaluasi sekali. Ini membuat perbedaan ketika default adalah objek yang dapat berubah seperti daftar, kamus, atau instance dari sebagian besar kelas. Misalnya, fungsi berikut mengakumulasi argumen yang diteruskan ke panggilan berikutnya:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
Ini akan dicetak

[1]
[1, 2]
[1, 2, 3]
Jika Anda tidak ingin default dibagi antara panggilan berikutnya, Anda dapat menulis fungsi seperti ini sebagai gantinya:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
4.7.2. Argumen Kata Kunci 
Fungsi juga bisa disebut menggunakan argumen kata kunci dari bentuk kwarg=value. Misalnya, fungsi berikut:

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
menerima satu argumen yang diperlukan ( voltage) dan tiga argumen opsional ( state, action, dan type). Fungsi ini dapat dipanggil dengan salah satu cara berikut:

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
tetapi semua panggilan berikut akan menjadi tidak valid:

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument
Dalam panggilan fungsi, argumen kata kunci harus mengikuti argumen posisional. Semua argumen kata kunci yang dilewatkan harus sesuai dengan salah satu argumen yang diterima oleh fungsi (misalnya actorbukan argumen yang valid untuk parrotfungsi tersebut), dan urutannya tidak penting. Ini juga termasuk argumen non-opsional (misalnya parrot(voltage=1000)juga valid). Tidak ada argumen yang dapat menerima nilai lebih dari satu kali. Berikut ini contoh yang gagal karena pembatasan ini:

>>>
>>> def function(a):
...     pass
...
>>> function(0, a=0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: function() got multiple values for keyword argument 'a'
Ketika parameter formal terakhir dari formulir **nameada, ia akan menerima kamus (lihat Tipe Pemetaan - dict ) yang berisi semua argumen kata kunci kecuali yang terkait dengan parameter formal. Ini dapat dikombinasikan dengan parameter formal formulir *name(dijelaskan dalam subbagian berikutnya) yang menerima tuple yang berisi argumen posisi di luar daftar parameter formal. ( *nameharus terjadi sebelumnya **name.) Misalnya, jika kita mendefinisikan fungsi seperti ini:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
Itu bisa disebut seperti ini:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
dan tentu saja itu akan dicetak:

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
Perhatikan bahwa urutan argumen kata kunci yang dicetak dijamin untuk mencocokkan urutan di mana mereka disediakan dalam panggilan fungsi.

4.7.3. Daftar Argumen Sewenang-wenang 
Akhirnya, opsi yang paling jarang digunakan adalah untuk menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen acak. Argumen-argumen ini akan dibungkus dalam tuple (lihat Tuples dan Urutan ). Sebelum jumlah variabel argumen, nol atau lebih banyak argumen normal dapat terjadi.

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
Biasanya, variadicargumen ini akan menjadi yang terakhir dalam daftar parameter formal, karena mereka mengumpulkan semua argumen input yang tersisa yang diteruskan ke fungsi. Setiap parameter formal yang terjadi setelah *args parameter adalah argumen 'kata kunci saja', yang berarti bahwa mereka hanya dapat digunakan sebagai kata kunci daripada argumen posisional.

>>>
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
4.7.4. Membongkar Daftar Argumen 
Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau tupel tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah. Sebagai contoh, fungsi built-in range()mengharapkan mulai terpisah dan menghentikan argumen. Jika tidak tersedia secara terpisah, tulis panggilan fungsi dengan *-operator untuk membongkar argumen dari daftar atau tupel:

>>>
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
Dengan cara yang sama, kamus dapat menyampaikan argumen kata kunci dengan **-operator:

>>>
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
4.7.5. Lambda Expressions 
Fungsi anonim kecil dapat dibuat dengan lambdakata kunci. Fungsi ini mengembalikan jumlah dari dua argumen: . Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantis, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bertingkat, fungsi lambda dapat merujuk variabel dari ruang lingkup yang mengandung:lambda a, b: a+b

>>>
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
Contoh di atas menggunakan ekspresi lambda untuk mengembalikan fungsi. Penggunaan lain adalah untuk melewatkan fungsi kecil sebagai argumen:

>>>
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
4.7.6. String Dokumentasi 
Berikut adalah beberapa konvensi tentang konten dan format string dokumentasi.

Baris pertama harus selalu berupa ringkasan singkat dan ringkas dari tujuan objek. Untuk keringkasan, seharusnya tidak secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama terjadi menjadi kata kerja yang menggambarkan operasi fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.

Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, secara visual memisahkan ringkasan dari sisa deskripsi. Baris berikut harus berupa satu paragraf atau lebih yang menggambarkan konvensi pemanggilan objek, efek sampingnya, dll.

Pengurai Python tidak melonggarkan indentasi dari literal string multi-baris dengan Python, sehingga alat yang memproses dokumentasi harus melonggarkan indentasi jika diinginkan. Ini dilakukan dengan menggunakan konvensi berikut. Baris non-kosong pertama setelah baris pertama string menentukan jumlah indentasi untuk seluruh string dokumentasi. (Kita tidak dapat menggunakan baris pertama karena umumnya berdekatan dengan kutipan pembukaan string sehingga indentasinya tidak terlihat dalam string literal.) Whitespace "setara" dengan indentasi ini kemudian dilucuti dari awal semua baris string . Garis-garis yang menjorok kurang seharusnya tidak terjadi, tetapi jika mereka terjadi semua ruang putih terkemuka mereka harus dilucuti. Kesetaraan spasi harus diuji setelah perluasan tab (hingga 8 spasi, biasanya).

Berikut ini contoh multi-baris docstring:

>>>
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
4.7.7. Anotasi Fungsi 
Anotasi fungsi sepenuhnya informasi metadata opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna (lihatPEP 3107 dan PEP 484 untuk informasi lebih lanjut).

Anotasi disimpan dalam __annotations__atribut fungsi sebagai kamus dan tidak berpengaruh pada bagian lain dari fungsi. Anotasi parameter ditentukan oleh titik dua setelah nama parameter, diikuti oleh ekspresi yang mengevaluasi ke nilai anotasi. Anotasi pengembalian ditentukan oleh literal ->, diikuti oleh ekspresi, antara daftar parameter dan titik dua yang menunjukkan akhir dari defpernyataan. Contoh berikut memiliki argumen posisi, argumen kata kunci, dan nilai kembalian yang dianotasikan:

>>>
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
4.8. Intermezzo: Gaya Pengkodean 
Sekarang Anda akan menulis lebih lama, potongan Python yang lebih rumit, ini adalah saat yang tepat untuk berbicara tentang gaya pengkodean . Sebagian besar bahasa dapat ditulis (atau lebih ringkas, diformat ) dalam gaya yang berbeda; beberapa lebih mudah dibaca daripada yang lain. Mempermudah orang lain untuk membaca kode Anda selalu merupakan ide yang baik, dan mengadopsi gaya pengodean yang bagus sangat membantu untuk itu.

Untuk Python, PEP 8 telah muncul sebagai panduan gaya yang paling dipatuhi oleh kebanyakan proyek; itu mempromosikan gaya pengkodean yang sangat mudah dibaca dan menyenangkan mata. Setiap pengembang Python harus membacanya di beberapa titik; berikut adalah poin paling penting yang diekstrak untuk Anda:

Gunakan 4-spasi indentasi, dan tidak ada tab.

4 ruang adalah kompromi yang baik antara lekukan kecil (memungkinkan kedalaman bersarang lebih besar) dan indentasi besar (lebih mudah dibaca). Tab memasukkan kebingungan, dan paling baik ditinggalkan.

Bungkus garis agar tidak melebihi 79 karakter.

Ini membantu pengguna dengan layar kecil dan memungkinkan untuk memiliki beberapa file kode secara berdampingan pada layar yang lebih besar.

Gunakan baris kosong untuk memisahkan fungsi dan kelas, dan blok kode yang lebih besar di dalam fungsi.

Jika memungkinkan, berikan komentar pada garis mereka sendiri.

Gunakan docstring.

Menggunakan spasi sekitar operator dan setelah koma, tapi tidak secara langsung di dalam bracketing konstruksi: .a = f(1, 2) + g(3, 4)

Sebutkan kelas dan fungsi Anda secara konsisten; konvensi ini digunakan CamelCaseuntuk kelas dan lower_case_with_underscoresuntuk fungsi dan metode. Selalu gunakan selfsebagai nama untuk argumen metode pertama (lihat A First Look at Classes untuk lebih lanjut tentang kelas dan metode).

Jangan menggunakan pengkodean mewah jika kode Anda dimaksudkan untuk digunakan di lingkungan internasional. Default Python, UTF-8, atau bahkan ASCII biasa bekerja paling baik dalam hal apapun.

Demikian juga, jangan gunakan karakter non-ASCII dalam pengidentifikasi jika hanya ada sedikit kesempatan orang yang berbicara bahasa yang berbeda akan membaca atau mempertahankan kode.
