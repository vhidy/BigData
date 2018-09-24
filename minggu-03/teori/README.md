5. Struktur Data 
Bab ini menjelaskan beberapa hal yang telah Anda pelajari tentang hal ini secara lebih rinci, dan menambahkan beberapa hal baru juga.

5.1. Lebih lanjut tentang Daftar 
Tipe data daftar memiliki beberapa metode lagi. Berikut adalah semua metode objek daftar:

list.append( x )
Tambahkan item ke bagian akhir daftar. Setara dengan .a[len(a):] = [x]

list.extend( iterable )
Perpanjang daftar dengan menambahkan semua item dari iterable. Setara dengan .a[len(a):] = iterable

list.insert( saya , x )
Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang sebelumnya disisipkan, sehingga menyisipkan di depan daftar, dan setara dengan .a.insert(0, x)a.insert(len(a), x)a.append(x)

list.remove( x )
Hapus item pertama dari daftar yang nilainya sama dengan x . Ini menimbulkan ValueErrorjika tidak ada barang seperti itu.

list.pop( [ i ] )
Hapus item pada posisi yang ditentukan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop()hapus dan kembalikan item terakhir dalam daftar. (Tanda kurung persegi di sekitar i dalam tanda tangan metode menunjukkan bahwa parameter adalah opsional, bukan bahwa Anda harus mengetik tanda kurung siku pada posisi itu. Anda akan melihat notasi ini sering dalam Referensi Perpustakaan Python.)

list.clear( )
Hapus semua item dari daftar. Setara dengan .del a[:]

list.index( x [ , mulai [ , akhir ] ] )
Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x . Mengangkat ValueErrorjika tidak ada barang seperti itu.

Argumen opsional awal dan akhir ditafsirkan sebagai dalam notasi slice dan digunakan untuk membatasi pencarian ke daftar urutan tertentu. Indeks yang dikembalikan dihitung relatif terhadap awal dari urutan penuh daripada argumen awal .

list.count( x )
Kembalikan jumlah kali x muncul dalam daftar.

list.sort( kunci = Tidak ada , balik = Salah )
Urutkan item dari daftar di tempat (argumen dapat digunakan untuk mengurutkan kustomisasi, lihat sorted()untuk penjelasannya).

list.reverse( )
Membalikkan unsur-unsur daftar di tempat.

list.copy( )
Kembalikan salinan dangkal daftar. Setara dengan a[:].

Contoh yang menggunakan sebagian besar metode daftar:

>>>
>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
Anda mungkin telah memperhatikan bahwa metode seperti insert, removeatau sortyang hanya mengubah daftar tidak memiliki nilai hasil cetak - mereka mengembalikan default None. [1] Ini adalah prinsip desain untuk semua struktur data yang bisa berubah dengan Python.

5.1.1. Menggunakan Daftar sebagai Tumpukan 
Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("terakhir-masuk, pertama-keluar"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari bagian atas tumpukan, gunakan pop()tanpa indeks eksplisit. Sebagai contoh:

>>>
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
5.1.2. Menggunakan Daftar sebagai Antrian 
Juga dimungkinkan untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, pertama keluar"); Namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser oleh satu).

Untuk mengimplementasikan antrian, gunakan collections.dequeyang dirancang agar memiliki penambahan cepat dan muncul dari kedua ujungnya. Sebagai contoh:

>>>
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
5.1.3. Daftar Pemahaman 
Daftar pemahaman menyediakan cara yang ringkas untuk membuat daftar. Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan lain atau dapat dilakukan, atau untuk menciptakan kelanjutan dari elemen-elemen yang memenuhi suatu kondisi tertentu.

Sebagai contoh, asumsikan kita ingin membuat daftar kotak, seperti:

>>>
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Perhatikan bahwa ini membuat (atau menimpa) variabel bernama xyang masih ada setelah loop selesai. Kita dapat menghitung daftar kotak tanpa efek samping menggunakan:

squares = list(map(lambda x: x**2, range(10)))
atau, dengan kata lain:

squares = [x**2 for x in range(10)]
yang lebih ringkas dan mudah dibaca.

Daftar pemahaman terdiri dari tanda kurung yang berisi ekspresi diikuti oleh forklausa, kemudian nol atau lebih foratau if klausa. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks fordan ifklausa yang mengikutinya. Misalnya, daftar ini menggabungkan beberapa elemen dari dua daftar jika tidak sama:

>>>
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
dan itu setara dengan:

>>>
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
Perhatikan bagaimana urutan fordan ifpernyataannya sama di kedua cuplikan ini.

Jika ungkapan adalah tupel (misalnya dalam contoh sebelumnya), itu harus disisipkan.(x, y)

>>>
>>> vec = [-4, -2, 0, 2, 4]
>>> # create a new list with the values doubled
>>> [x*2 for x in vec]
[-8, -4, 0, 4, 8]
>>> # filter the list to exclude negative numbers
>>> [x for x in vec if x >= 0]
[0, 2, 4]
>>> # apply a function to all the elements
>>> [abs(x) for x in vec]
[4, 2, 0, 2, 4]
>>> # call a method on each element
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
>>> # create a list of 2-tuples like (number, square)
>>> [(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
>>> # the tuple must be parenthesized, otherwise an error is raised
>>> [x, x**2 for x in range(6)]
  File "<stdin>", line 1, in <module>
    [x, x**2 for x in range(6)]
               ^
SyntaxError: invalid syntax
>>> # flatten a list using a listcomp with two 'for'
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
List comprehensions dapat berisi ekspresi kompleks dan fungsi yang disarangkan:

>>>
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
5.1.4. Pengertian Daftar Bersarang 
Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi sembarang, termasuk pemahaman daftar lainnya.

Pertimbangkan contoh berikut dari matriks 3x4 yang diimplementasikan sebagai daftar 3 daftar panjang 4:

>>>
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
Daftar pemahaman berikut ini akan mentransposisi baris dan kolom:

>>>
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Seperti yang kita lihat di bagian sebelumnya, listcomp bersarang dievaluasi dalam konteks foryang mengikutinya, jadi contoh ini setara dengan:

>>>
>>> transposed = []
>>> for i in range(4):
...     transposed.append([row[i] for row in matrix])
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
yang, pada gilirannya, adalah sama dengan:

>>>
>>> transposed = []
>>> for i in range(4):
...     # the following 3 lines implement the nested listcomp
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
Di dunia nyata, Anda harus lebih memilih fungsi-fungsi bawaan untuk pernyataan aliran yang rumit. The zip()fungsi akan melakukan pekerjaan yang besar untuk kasus penggunaan ini:

>>>
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
Lihat Membongkar Daftar Argumen untuk perincian tentang tanda bintang di baris ini.

5.2. The delPernyataan 
Ada cara untuk menghapus item dari daftar yang diberikan indeksnya, bukan nilainya: delpernyataan. Ini berbeda dari pop()metode yang mengembalikan nilai. The delPernyataan juga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kami lakukan sebelumnya oleh tugas dari daftar kosong untuk slice). Sebagai contoh:

>>>
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
del juga dapat digunakan untuk menghapus seluruh variabel:

>>>
>>> del a
Mereferensikan nama aselanjutnya adalah kesalahan (setidaknya sampai nilai lain ditetapkan untuk itu). Kami akan menemukan kegunaan lain untuk delnanti.

5.3. Tuples dan Urutan 
Kami melihat bahwa daftar dan string memiliki banyak properti umum, seperti pengindeksan dan operasi pengirisan. Mereka adalah dua contoh tipe data urutan (lihat Jenis Urutan - daftar, tupel, rentang ). Karena Python adalah bahasa yang sedang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple .

Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:

>>>
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])
Seperti yang Anda lihat, pada tupel keluaran selalu diapit dalam tanda kurung, sehingga tuple yang disarangkan ditafsirkan dengan benar; mereka mungkin menjadi masukan dengan atau tanpa tanda kurung di sekitarnya, meskipun seringkali tanda kurung diperlukan (jika tupel adalah bagian dari ekspresi yang lebih besar). Tidak mungkin untuk menetapkan ke masing-masing item tuple, namun dimungkinkan untuk membuat tuple yang berisi objek yang bisa berubah, seperti daftar.

Meskipun tuples mungkin tampak mirip dengan daftar, tuples sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuples tidak dapat diubah , dan biasanya mengandung urutan elemen heterogen yang diakses melalui pembongkaran (lihat nanti di bagian ini) atau pengindeksan (atau bahkan oleh atribut dalam kasus namedtuples). Daftar bisa berubah , dan elemen mereka biasanya homogen dan diakses dengan iterasi di atas daftar.

Masalah khusus adalah konstruksi tuple berisi 0 atau 1 item: sintaks memiliki beberapa quirks tambahan untuk mengakomodasi ini. Tuple kosong dibangun oleh sepasang tanda kurung kosong; tuple dengan satu item dikonstruksi dengan mengikuti nilai dengan koma (tidak cukup untuk menyertakan satu nilai dalam tanda kurung). Jelek, tapi efektif. Sebagai contoh:

>>>
>>> empty = ()
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
Pernyataan itu adalah contoh pengepakan tuple : nilai-nilai , dan dikemas bersama dalam sebuah tuple. Operasi sebaliknya juga dimungkinkan:t = 12345, 54321, 'hello!'1234554321'hello!'

>>>
>>> x, y, z = t
Ini disebut, cukup tepat, urutan membongkar dan berfungsi untuk setiap urutan di sisi kanan. Urutan pembongkaran mensyaratkan bahwa ada banyak variabel di sisi kiri tanda sama dengan karena ada elemen dalam urutan. Perhatikan bahwa banyak tugas benar-benar hanya kombinasi dari pengepakan tuple dan urutan unpacking.

5.4. Set 
Python juga termasuk tipe data untuk set . Satu set adalah koleksi tak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Mengatur objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

Keriting kurung atau set()fungsi dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong yang harus Anda gunakan set(), tidak {}; yang terakhir menciptakan kamus kosong, struktur data yang kita diskusikan di bagian selanjutnya.

Berikut ini adalah demonstrasi singkat:

>>>
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
Demikian pula untuk daftar comprehensions , set comprehensions juga didukung:

>>>
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
5,5. Kamus 
Tipe data lain yang berguna dibangun ke dalam Python adalah kamus (lihat Jenis Pemetaan - dict ). Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "kenangan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh berbagai angka, kamus diindeks oleh kunci , yang bisa menjadi jenis yang tidak berubah; string dan angka selalu bisa menjadi kunci. Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika tuple berisi objek yang dapat berubah baik secara langsung atau tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan tugas indeks, tugas slice, atau metode seperti append()dan extend().

Yang terbaik adalah memikirkan kamus sebagai satu set kunci: pasangan nilai , dengan persyaratan bahwa kunci itu unik (dalam satu kamus). Sepasang kawat gigi menciptakan kamus kosong: {}. Menempatkan daftar kunci yang dipisahkan koma: pasangan nilai dalam tanda kurung menambahkan kunci awal: pasang nilai ke kamus; ini juga cara kamus ditulis pada output.

Operasi utama pada kamus menyimpan nilai dengan beberapa kunci dan mengekstraksi nilai yang diberikan kunci. Anda juga dapat menghapus kunci: pasangan nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu terlupakan. Ini adalah kesalahan untuk mengekstrak nilai menggunakan kunci yang tidak ada.

Melakukan list(d)pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, gunakan saja sorted(d)sebagai gantinya). Untuk memeriksa apakah kunci tunggal ada di kamus, gunakan inkata kunci.

Berikut ini contoh kecil menggunakan kamus:

>>>
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
The dict()konstruktor membangun kamus langsung dari urutan pasangan kunci-nilai:

>>>
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
Selain itu, pemahaman dimengerti dapat digunakan untuk membuat kamus dari kunci acak dan ekspresi nilai:

>>>
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
Ketika kunci adalah string sederhana, terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:

>>>
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
5.6. Teknik Looping 
Ketika mengulang melalui kamus, kunci dan nilai yang terkait dapat diambil pada saat yang sama menggunakan items()metode.

>>>
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
Ketika mengulang melalui urutan, indeks posisi dan nilai yang terkait dapat diambil pada saat yang sama menggunakan enumerate()fungsi.

>>>
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
...
0 tic
1 tac
2 toe
Untuk mengulang lebih dari dua atau lebih urutan pada saat yang sama, entri dapat dipasangkan dengan zip()fungsi.

>>>
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...     print('What is your {0}?  It is {1}.'.format(q, a))
...
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
Untuk mengulang suatu urutan secara terbalik, pertama-tama tentukan urutan dalam arah maju dan kemudian panggil reversed()fungsi tersebut.

>>>
>>> for i in reversed(range(1, 10, 2)):
...     print(i)
...
9
7
5
3
1
Untuk mengulang urutan dalam urutan yang diurutkan, gunakan sorted()fungsi yang mengembalikan daftar yang diurutkan baru saat meninggalkan sumber tidak berubah.

>>>
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...     print(f)
...
apple
banana
orange
pear
Terkadang menggoda untuk mengubah daftar saat Anda mengulanginya; namun, seringkali lebih sederhana dan lebih aman untuk membuat daftar baru.

>>>
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
5.7. Lebih lanjut tentang Ketentuan 
Kondisi yang digunakan dalam whiledan ifpernyataan dapat mengandung operator, bukan hanya perbandingan.

Operator perbandingan indan memeriksa apakah nilai terjadi (tidak terjadi) secara berurutan. Operator dan membandingkan apakah dua objek benar-benar objek yang sama; ini hanya penting untuk objek yang bisa berubah seperti daftar. Semua operator pembanding memiliki prioritas yang sama, yang lebih rendah daripada semua operator numerik.not inisis not

Perbandingan bisa dirantai. Sebagai contoh, tes apakah kurang dari dan lebih dari sama .a < b == cabbc

Perbandingan dapat digabungkan menggunakan operator Boolean anddan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat diabaikan not. Ini memiliki prioritas yang lebih rendah daripada operator pembanding; di antara mereka, notmemiliki prioritas tertinggi dan orterendah, sehingga setara dengan . Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.A and not B or C(A and (not B)) or C

Operator Boolean anddan ordisebut operator hubungan singkat : argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan. Misalnya, jika Adan Cbenar tetapi Bsalah, tidak mengevaluasi ekspresi . Ketika digunakan sebagai nilai umum dan bukan sebagai Boolean, nilai kembalian dari operator hubung singkat adalah argumen yang terakhir dievaluasi.A and B and CC

Adalah mungkin untuk menetapkan hasil perbandingan atau ekspresi Boolean lain ke suatu variabel. Sebagai contoh,

>>>
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
Perhatikan bahwa dengan Python, tidak seperti C, tugas tidak dapat terjadi di dalam ekspresi. Pemrogram C mungkin mengeluh tentang hal ini, tetapi menghindari kelas umum masalah yang dihadapi dalam program C: mengetikkan =ekspresi ketika ==dimaksudkan.

5.8. Membandingkan Urutan dan Jenis Lain 
Objek urutan dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan ini menggunakan urutan leksikografis : pertama dua item pertama dibandingkan, dan jika mereka berbeda, ini menentukan hasil perbandingan; jika keduanya sama, dua item berikutnya akan dibandingkan, dan seterusnya, hingga urutannya habis. Jika dua item untuk dibandingkan adalah urutan dari jenis yang sama, perbandingan leksikografis dilakukan secara rekursif. Jika semua item dari dua urutan membandingkan sama, urutan dianggap sama. Jika satu urutan adalah sub-urutan awal yang lain, urutan yang lebih pendek adalah yang lebih kecil (lebih kecil). Pemesanan Lexicographical untuk string menggunakan nomor poin kode Unicode untuk memesan karakter individu. Beberapa contoh perbandingan antara urutan jenis yang sama:

(1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)
Perhatikan bahwa membandingkan objek dari berbagai jenis dengan <atau >legal asalkan objek memiliki metode perbandingan yang tepat. Sebagai contoh, jenis-jenis numerik campuran dibandingkan berdasarkan nilai numeriknya, jadi 0 sama dengan 0,0, dll. Sebaliknya, daripada menyediakan pemesanan acak, penerjemah akan meningkatkan TypeErrorpengecualian.
