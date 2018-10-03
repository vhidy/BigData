6. Modul 
Jika Anda keluar dari interpreter Python dan memasukkannya lagi, definisi yang Anda buat (fungsi dan variabel) hilang. Oleh karena itu, jika Anda ingin menulis program yang agak lebih panjang, Anda lebih baik menggunakan editor teks untuk menyiapkan masukan bagi juru bahasa dan menjalankannya dengan file itu sebagai masukan. Ini dikenal sebagai membuat skrip . Seiring program Anda menjadi lebih panjang, Anda mungkin ingin membaginya menjadi beberapa file untuk memudahkan perawatan. Anda mungkin juga ingin menggunakan fungsi berguna yang telah Anda tulis di beberapa program tanpa menyalin definisinya ke dalam setiap program.

Untuk mendukung ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter. File seperti itu disebut modul ; definisi dari modul dapat diimpor ke modul lain atau ke dalam modul utama (kumpulan variabel yang Anda miliki akses ke skrip yang dijalankan di tingkat atas dan dalam mode kalkulator).

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .pyditambahkan. Dalam modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__. Misalnya, gunakan editor teks favorit Anda untuk membuat file yang disebut fibo.pydi direktori saat ini dengan konten berikut:

# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
Sekarang masukkan interpreter Python dan impor modul ini dengan perintah berikut:

>>>
>>> import fibo
Ini tidak memasukkan nama fungsi yang didefinisikan fibo secara langsung di tabel simbol saat ini; itu hanya memasukkan nama modul di fibosana. Menggunakan nama modul Anda dapat mengakses fungsi:

>>>
>>> fibo.fib(1000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
>>> fibo.fib2(100)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> fibo.__name__
'fibo'
Jika Anda berniat menggunakan fungsi sering Anda dapat menetapkannya ke nama lokal:

>>>
>>> fib = fibo.fib
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
6.1. Lebih lanjut tentang Modul 
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan-pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali nama modul ditemukan dalam pernyataan impor. [1] (Mereka juga dijalankan jika file dijalankan sebagai skrip.)

Setiap modul memiliki tabel simbol pribadi, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, penulis modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika Anda tahu apa yang Anda lakukan Anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk fungsinya modname.itemname,.

Modul dapat mengimpor modul lain. Ini adalah kebiasaan tetapi tidak diperlukan untuk menempatkan semua importpernyataan di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor ditempatkan di tabel simbol global modul impor.

Ada varian dari importpernyataan yang mengimpor nama dari modul langsung ke tabel simbol modul pengimpor. Sebagai contoh:

>>>
>>> from fibo import fib, fib2
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Ini tidak memperkenalkan nama modul dari mana impor diambil di tabel simbol lokal (jadi dalam contoh, fibotidak didefinisikan).

Bahkan ada varian untuk mengimpor semua nama yang didefinisikan oleh modul:

>>>
>>> from fibo import *
>>> fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Ini mengimpor semua nama kecuali yang diawali dengan underscore ( _). Dalam kebanyakan kasus, programmer Python tidak menggunakan fasilitas ini karena memperkenalkan kumpulan nama yang tidak dikenal ke interpreter, mungkin menyembunyikan beberapa hal yang sudah Anda definisikan.

Perhatikan bahwa pada umumnya praktik pengimporan *dari modul atau paket dikecam, karena sering menyebabkan kode yang tidak dapat dibaca dengan baik. Namun, boleh saja menggunakannya untuk menyimpan pengetikan dalam sesi interaktif.

Jika nama modul diikuti as, maka nama berikut asterikat langsung ke modul yang diimpor.

>>>
>>> import fibo as fib
>>> fib.fib(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Ini secara efektif mengimpor modul dengan cara yang sama yang akan dilakukan, dengan satu-satunya perbedaan itu tersedia sebagai .import fibofib

Ini juga dapat digunakan saat memanfaatkan fromdengan efek serupa:

>>>
>>> from fibo import fib as fibonacci
>>> fibonacci(500)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
Catatan Untuk alasan efisiensi, setiap modul hanya diimpor sekali per sesi interpreter. Oleh karena itu, jika Anda mengubah modul Anda, Anda harus me-restart interpreter - atau, jika itu hanya satu modul yang ingin Anda uji secara interaktif, gunakan importlib.reload(), misalnya .import importlib; importlib.reload(modulename)
6.1.1. Melaksanakan modul sebagai skrip 
Ketika Anda menjalankan modul Python dengan

python fibo.py <arguments>
kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__set ke "__main__". Itu berarti bahwa dengan menambahkan kode ini di akhir modul Anda:

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
Anda dapat menjadikan file dapat digunakan sebagai skrip dan juga modul yang dapat diimpor, karena kode yang mem-parsing baris perintah hanya berjalan jika modul dijalankan sebagai file "utama":

$ python fibo.py 50
0 1 1 2 3 5 8 13 21 34
Jika modul diimpor, kode tidak dijalankan:

>>>
>>> import fibo
>>>
Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul sebagai skrip mengeksekusi rangkaian uji).

6.1.2. Jalur Pencarian Modul 
Ketika sebuah modul bernama spamdiimpor, interpreter pertama mencari modul built-in dengan nama itu. Jika tidak ditemukan, kemudian mencari file yang disebutkan spam.pydalam daftar direktori yang diberikan oleh variabel sys.path. sys.pathdiinisialisasi dari lokasi berikut:

Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).
PYTHONPATH (daftar nama direktori, dengan sintaks yang sama dengan variabel shell PATH).
Standar yang tergantung pada instalasi.
Catatan Pada sistem file yang mendukung symlink, direktori yang berisi skrip input dihitung setelah symlink diikuti. Dengan kata lain direktori yang mengandung symlink tidak ditambahkan ke jalur pencarian modul.
Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang dijalankan ditempatkan di awal jalur pencarian, di depan jalur perpustakaan standar. Ini berarti skrip di direktori itu akan dimuat alih-alih modul dengan nama yang sama di direktori pustaka. Ini adalah kesalahan kecuali pengganti itu dimaksudkan. Lihat bagian Modul Standar untuk informasi lebih lanjut.

6.1.3. "Dikompilasi" file Python 
Untuk mempercepat pemuatan modul, Python menyimpan versi terkompilasi dari setiap modul di __pycache__direktori di bawah nama , di mana versi mengkodekan format file yang dikompilasi; biasanya berisi nomor versi Python. Sebagai contoh, dalam CPython rilis 3.3 versi yang dikompilasi dari spam.py akan di-cache sebagai . Konvensi penamaan ini memungkinkan modul yang dikompilasi dari rilis yang berbeda dan versi Python yang berbeda untuk hidup berdampingan.module.version.pyc__pycache__/spam.cpython-33.pyc

Python memeriksa tanggal modifikasi dari sumber terhadap versi yang dikompilasi untuk melihat apakah sudah kedaluwarsa dan perlu dikompilasi ulang. Ini adalah proses yang sepenuhnya otomatis. Juga, modul yang dikompilasi adalah platform-independen, sehingga perpustakaan yang sama dapat dibagi di antara sistem dengan arsitektur yang berbeda.

Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, tidak memeriksa cache jika tidak ada modul sumber. Untuk mendukung distribusi non-sumber (yang dikompilasi saja), modul yang dikompilasi harus berada di direktori sumber, dan tidak boleh ada modul sumber.

Beberapa tips untuk para ahli:

Anda dapat menggunakan -Oatau -OOmengaktifkan perintah Python untuk mengurangi ukuran modul yang dikompilasi. The -Osaklar menghilangkan menegaskan pernyataan, yang -OOberalih menghilangkan kedua menegaskan pernyataan dan string __doc__. Karena beberapa program mungkin mengandalkan ketersediaannya, Anda hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan. Modul "Dioptimalkan" memiliki opt-tag dan biasanya lebih kecil. Rilis mendatang dapat mengubah efek pengoptimalan.
Program tidak berjalan lebih cepat ketika dibaca dari .pyc file daripada saat dibaca dari .pyfile; satu-satunya hal yang lebih cepat tentang .pycfile adalah kecepatan yang dimuatnya.
Modul compilealldapat membuat file .pyc untuk semua modul dalam direktori.
Ada detail lebih lanjut tentang proses ini, termasuk diagram alur dari keputusan, di PEP 3147 .
6.2. Modul Standar 
Python dilengkapi dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Perpustakaan Python ("Referensi Perpustakaan" selanjutnya). Beberapa modul dibangun ke interpreter; ini memberikan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke primitif sistem operasi seperti panggilan sistem. Kumpulan modul tersebut adalah opsi konfigurasi yang juga bergantung pada platform yang mendasarinya. Misalnya, winregmodul hanya disediakan pada sistem Windows. Satu modul tertentu layak mendapat perhatian:, sysyang dibangun ke setiap interpreter Python. Variabel sys.ps1dan sys.ps2menentukan string yang digunakan sebagai petunjuk utama dan sekunder:

>>>
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
Kedua variabel ini hanya ditentukan jika interpreter berada dalam mode interaktif.

Variabel sys.pathadalah daftar string yang menentukan jalur pencarian interpreter untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkunganPYTHONPATH, atau dari bawaan bawaan jika PYTHONPATHtidak diatur. Anda dapat memodifikasinya menggunakan operasi daftar standar:

>>>
>>> import sys
>>> sys.path.append('/ufs/guido/lib/python')
6.3. The dir()Fungsi 
Fungsi built-in dir()digunakan untuk mencari tahu nama-nama yang didefinisikan modul. Ini mengembalikan daftar string yang diurutkan:

>>>
>>> import fibo, sys
>>> dir(fibo)
['__name__', 'fib', 'fib2']
>>> dir(sys)  
['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
 '__package__', '__stderr__', '__stdin__', '__stdout__',
 '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
 '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
 'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
 'call_tracing', 'callstats', 'copyright', 'displayhook',
 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
 'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
 'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
 'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
 'thread_info', 'version', 'version_info', 'warnoptions']
Tanpa argumen, dir()cantumkan nama yang telah Anda tentukan saat ini:

>>>
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
Perhatikan bahwa ini mencantumkan semua jenis nama: variabel, modul, fungsi, dll.

dir()tidak mencantumkan nama fungsi dan variabel bawaan. Jika Anda menginginkan daftar itu, mereka didefinisikan dalam modul standar builtins:

>>>
>>> import builtins
>>> dir(builtins)  
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError',
 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError',
 'MemoryError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented',
 'NotImplementedError', 'OSError', 'OverflowError',
 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError',
 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError',
 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError',
 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError',
 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning',
 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__',
 '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs',
 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits',
 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit',
 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass',
 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview',
 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property',
 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice',
 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars',
 'zip']
6.4. Paket 
Paket adalah cara menyusun ruang nama modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul A.Bmenunjuk sebuah submodul yang dinamai Bdalam paket bernama A. Sama seperti penggunaan modul menyimpan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul putus-putus menyimpan penulis paket multi-modul seperti NumPy atau Bantal karena harus khawatir tentang nama-nama modul masing-masing .

Misalkan Anda ingin merancang koleksi modul ("paket") untuk penanganan seragam file suara dan data suara. Ada berbagai format file suara (biasanya diakui oleh ekstensi mereka, misalnya: .wav, .aiff, .au), sehingga Anda mungkin perlu untuk membuat dan memelihara koleksi tumbuh modul untuk konversi antara berbagai format file. Ada juga berbagai operasi yang Anda mungkin ingin lakukan pada data suara (seperti pencampuran, menambahkan gema, menerapkan fungsi equalizer, menciptakan efek stereo buatan), jadi selain itu Anda akan menulis aliran modul yang tidak pernah berakhir untuk melakukan operasi ini. Berikut adalah struktur yang mungkin untuk paket Anda (dinyatakan dalam sistem file hirarkis):

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
Ketika mengimpor paket, Python mencari melalui direktori pada sys.pathmencari subdirektori paket.

The __init__.pyfile yang diperlukan untuk membuat Python memperlakukan direktori sebagai mengandung paket; ini dilakukan untuk mencegah direktori dengan nama umum, seperti string, dari secara tidak sengaja menyembunyikan modul valid yang terjadi nanti di jalur pencarian modul. Dalam kasus yang paling sederhana, __init__.pyhanya bisa menjadi file kosong, tetapi juga dapat mengeksekusi kode inisialisasi untuk paket atau mengatur __all__variabel, yang dijelaskan kemudian.

Pengguna paket dapat mengimpor modul individual dari paket, misalnya:

import sound.effects.echo
Ini memuat submodule sound.effects.echo. Itu harus direferensikan dengan nama lengkapnya.

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
Cara alternatif untuk mengimpor submodul adalah:

from sound.effects import echo
Ini juga memuat submodul echo, dan membuatnya tersedia tanpa awalan paket, sehingga dapat digunakan sebagai berikut:

echo.echofilter(input, output, delay=0.7, atten=4)
Namun variasi lain adalah mengimpor fungsi atau variabel yang diinginkan secara langsung:

from sound.effects.echo import echofilter
Sekali lagi, ini memuat submodule echo, tetapi ini membuat fungsinya echofilter()langsung tersedia:

echofilter(input, output, delay=0.7, atten=4)
Perhatikan bahwa ketika menggunakan , item dapat berupa submodul (atau sub-paket) paket, atau beberapa nama lain yang didefinisikan dalam paket, seperti fungsi, kelas atau variabel. The Pernyataan tes dulu apakah item tersebut didefinisikan dalam paket; jika tidak, ia menganggap itu adalah modul dan mencoba untuk memuatnya. Jika gagal menemukannya, sebuah pengecualian dinaikkan.from package import itemimportImportError

Sebaliknya, ketika menggunakan sintaks seperti , setiap item kecuali yang terakhir harus paket; item terakhir dapat berupa modul atau paket tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.import item.subitem.subsubitem

6.4.1. Mengimpor * Dari Paket 
Sekarang apa yang terjadi ketika pengguna menulis ? Idealnya, orang akan berharap bahwa ini entah bagaimana keluar ke filesystem, menemukan submodul yang hadir dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor sub-modul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika sub-modul secara eksplisit diimpor.from sound.effects import *

Satu-satunya solusi adalah untuk penulis paket untuk memberikan indeks eksplisit dari paket tersebut. The importpernyataan menggunakan konvensi berikut: jika paket ini __init__.pykode mendefinisikan daftar nama __all__, itu diambil untuk menjadi daftar nama modul yang harus diimpor saat ditemui. Terserah penulis paket untuk menjaga daftar ini tetap terbaru ketika versi baru dari paket tersebut dirilis. Penulis paket juga dapat memutuskan untuk tidak mendukungnya, jika mereka tidak melihat penggunaan untuk mengimpor * dari paket mereka. Misalnya, file dapat berisi kode berikut:from package import *sound/effects/__init__.py

__all__ = ["echo", "surround", "reverse"]
Ini berarti bahwa akan mengimpor tiga submodul bernama paket.from sound.effects import *sound

Jika __all__tidak didefinisikan, pernyataan itu tidak tidak mengimpor semua submodul dari paket ke dalam namespace saat ini; hanya memastikan bahwa paket telah diimpor (mungkin menjalankan kode inisialisasi apa pun di dalamnya ) dan kemudian mengimpor nama apa pun yang ditetapkan dalam paket. Ini termasuk nama apa pun yang didefinisikan (dan submodul yang dimuat secara eksplisit) oleh . Ini juga termasuk submodules dari paket yang secara eksplisit dimuat oleh pernyataan sebelumnya . Pertimbangkan kode ini:from sound.effects import *sound.effectssound.effects__init__.py__init__.pyimport

import sound.effects.echo
import sound.effects.surround
from sound.effects import *
Dalam contoh ini, echodan surroundmodul diimpor dalam namespace saat ini karena mereka didefinisikan dalam sound.effectspaket saat from...importpernyataan dijalankan. (Ini juga berfungsi saat __all__ditentukan.)

Meskipun modul tertentu dirancang untuk mengekspor hanya nama yang mengikuti pola tertentu ketika Anda menggunakan , itu masih dianggap praktik buruk dalam kode produksi.import *

Ingat, tidak ada yang salah dengan menggunakan ! Sebenarnya, ini adalah notasi yang disarankan kecuali modul pengimpor perlu menggunakan submodul dengan nama yang sama dari paket yang berbeda.from Package import specific_submodule

6.4.2. Referensi Intra-paket 
Ketika paket terstruktur menjadi sub-paket (seperti dengan soundpaket dalam contoh), Anda dapat menggunakan impor mutlak untuk merujuk ke paket submodul dari saudara kandung. Misalnya, jika modul sound.filters.vocoderperlu menggunakan echomodul dalam sound.effectspaket, itu bisa digunakan .from sound.effects import echo

Anda juga dapat menulis impor relatif, dengan bentuk pernyataan impor. Impor ini menggunakan titik-titik utama untuk menunjukkan paket saat ini dan induk yang terlibat dalam impor relatif. Dari modul misalnya, Anda mungkin menggunakan:from module import namesurround

from . import echo
from .. import formats
from ..filters import equalizer
Perhatikan bahwa impor relatif didasarkan pada nama modul saat ini. Karena nama modul utama selalu "__main__", modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan impor mutlak.

6.4.3. Paket di Beberapa Direktori 
Paket mendukung satu lagi atribut khusus __path__,. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan paket __init__.pysebelum kode di file tersebut dieksekusi. Variabel ini dapat dimodifikasi; hal ini mempengaruhi pencarian modul dan sub-paket di masa mendatang yang terkandung dalam paket.

Meskipun fitur ini tidak sering dibutuhkan, fitur ini dapat digunakan untuk memperluas set modul yang ditemukan dalam paket.

7. Input dan Output 
Ada beberapa cara untuk menyajikan output dari suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang. Bab ini akan membahas beberapa kemungkinan.

7.1. Fancier Output Formatting 
Sejauh ini kita telah menemukan dua cara penulisan nilai: pernyataan ekspresi dan print()fungsi. (Cara ketiga adalah menggunakan write()metode objek file; file output standar dapat direferensikan sebagai sys.stdout. Lihat Referensi Perpustakaan untuk informasi lebih lanjut tentang ini.)

Seringkali Anda akan menginginkan lebih banyak kontrol atas pemformatan output Anda daripada hanya mencetak nilai-nilai yang dipisahkan ruang. Ada beberapa cara untuk memformat output.

Untuk menggunakan literal string berformat , mulailah string dengan fatau Fsebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda dapat menulis ekspresi Python antara {dan } karakter yang dapat merujuk ke variabel atau nilai literal.

>>>
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
The str.format()Metode string membutuhkan usaha lebih manual. Anda masih akan menggunakan {dan }menandai di mana variabel akan digantikan dan dapat memberikan arahan pemformatan mendetail, tetapi Anda juga harus memberikan informasi yang akan diformat.

>>>
>>> yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
Akhirnya, Anda dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengiris dan penggabungan string untuk membuat tata letak apa pun yang dapat Anda bayangkan. Jenis string memiliki beberapa metode yang melakukan operasi yang bermanfaat untuk string bantalan ke lebar kolom yang diberikan.

Ketika Anda tidak membutuhkan keluaran yang mewah tetapi hanya ingin menampilkan beberapa variabel untuk keperluan debugging, Anda dapat mengkonversi nilai apa pun ke string dengan fungsi repr()atau str().

The str()Fungsi dimaksudkan untuk mengembalikan representasi dari nilai-nilai yang cukup terbaca-manusia, sementara repr()dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh interpreter (atau akan memaksa SyntaxErrorjika tidak ada setara sintaks). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str()akan mengembalikan nilai yang sama repr(). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan salah satu fungsi. String, khususnya, memiliki dua representasi berbeda.

Beberapa contoh:

>>>
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'
>>> repr(s)
"'Hello, world.'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
>>> print(s)
The value of x is 32.5, and y is 40000...
>>> # The repr() of a string adds string quotes and backslashes:
... hello = 'hello, world\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, world\n'
>>> # The argument to repr() may be any Python object:
... repr((x, y, ('spam', 'eggs')))
"(32.5, 40000, ('spam', 'eggs'))"
The stringmodul berisi Templatekelas yang belum menawarkan cara lain untuk menggantikan nilai-nilai ke dalam string, menggunakan placeholder seperti $xdan menggantinya dengan nilai-nilai dari sebuah kamus, tapi menawarkan kontrol jauh lebih sedikit dari format.

7.1.1. String Literal Terformat 
String literal terformat (juga disebut f-string untuk pendek) memungkinkan Anda menyertakan nilai ekspresi Python di dalam string dengan mengawali string denganfatauFdan menulis ekspresi sebagai {expression}.

Penentu format opsional dapat mengikuti ekspresi. Ini memungkinkan kontrol lebih besar atas bagaimana nilai diformat. Berikut contoh putaran pi ke tiga tempat setelah desimal:

>>>
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
Melewati integer setelah ':'akan menyebabkan bidang itu menjadi jumlah karakter minimum yang lebar. Ini berguna untuk membuat kolom berbaris.

>>>
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
Pengubah lain dapat digunakan untuk mengonversi nilai sebelum diformat. '!a'berlaku ascii(), '!s'berlaku str(), dan '!r' berlaku repr():

>>>
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
Untuk referensi pada spesifikasi format ini, lihat panduan referensi untuk Bahasa Mini Spesifikasi Format .

7.1.2. Format String () Metode 
Penggunaan dasar dari str.format()metode ini terlihat seperti ini:

>>>
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
Tanda kurung dan karakter di dalamnya (disebut kolom format) diganti dengan objek yang dilewatkan ke dalam str.format()metode. Angka dalam tanda kurung dapat digunakan untuk merujuk pada posisi objek yang dilewatkan ke dalam str.format()metode.

>>>
>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
Jika argumen kata kunci digunakan dalam str.format()metode, nilainya akan dirujuk dengan menggunakan nama argumen.

>>>
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
Argumen posisi dan kata kunci dapat digabungkan secara sewenang-wenang:

>>>
>>> print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                       other='Georg'))
The story of Bill, Manfred, and Georg.
Jika Anda memiliki string format yang sangat panjang sehingga Anda tidak ingin berpisah, alangkah baiknya jika Anda bisa mereferensikan variabel yang akan diformat dengan nama alih-alih berdasarkan posisi. Ini dapat dilakukan hanya dengan melewati dikt dan menggunakan tanda kurung siku '[]'untuk mengakses kunci

>>>
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
Ini juga bisa dilakukan dengan melewatkan tabel sebagai argumen kata kunci dengan notasi '**'.

>>>
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
Ini sangat berguna dalam kombinasi dengan fungsi built-in vars(), yang mengembalikan kamus yang berisi semua variabel lokal.

Sebagai contoh, garis-garis berikut menghasilkan satu set kolom-kolom yang diratakan memberikan integer dan kotak dan kubus mereka:

>>>
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
Untuk gambaran lengkap tentang pemformatan string dengan str.format(), lihat Format String Syntax .

7.1.3. Pemformatan String Manual 
Ini adalah tabel kuadrat dan kubus yang sama, diformat secara manual:

>>>
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
(Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan dengan cara print()kerjanya: itu selalu menambahkan spasi di antara argumennya.)

The str.rjust()Metode string benda kanan membenarkan string dalam bidang lebar yang diberikan oleh padding dengan spasi di sebelah kiri. Ada metode serupa str.ljust()dan str.center(). Metode-metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda tetapi biasanya lebih baik daripada alternatif, yang akan berbohong tentang suatu nilai. (Jika Anda benar-benar ingin pemotongan, Anda selalu dapat menambahkan operasi slice, seperti pada x.ljust(n)[:n].)

Ada metode lain str.zfill(),, yang memberikan string numerik di sebelah kiri dengan nol. Ia mengerti tentang tanda plus dan minus:

>>>
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'
7.1.4. Pemformatan string lama 
The %Operator juga dapat digunakan untuk string format. Ini menafsirkan argumen kiri seperti sprintf()string format -style untuk diterapkan ke argumen yang tepat, dan mengembalikan string yang dihasilkan dari operasi format ini. Sebagai contoh:

>>>
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
Informasi lebih lanjut dapat ditemukan di bagian String Formatting bergaya printf .

7.2. Membaca dan Menulis File 
open()mengembalikan file objek , dan ini paling sering digunakan dengan dua argumen: .open(filename, mode)

>>>
>>> f = open('workfile', 'w')
Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan. mode bisa 'r'ketika file hanya akan dibaca, 'w' untuk hanya menulis (file yang sudah ada dengan nama yang sama akan dihapus), dan 'a'membuka file untuk menambahkan; data apa pun yang ditulis ke file ditambahkan secara otomatis ke bagian akhir. 'r+'membuka file untuk membaca dan menulis. The Modus argumen adalah opsional; 'r'akan diasumsikan jika dihilangkan.

Biasanya, file dibuka dalam mode teks , itu berarti, Anda membaca dan menulis string dari dan ke file, yang dikodekan dalam pengkodean tertentu. Jika pengkodean tidak ditentukan, standarnya tergantung pada platform (lihat open()). 'b'ditambahkan ke mode membuka file dalam mode biner : sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak mengandung teks.

Dalam mode teks, default ketika membaca adalah untuk mengkonversi ujung baris platform-spesifik ( \npada Unix, \r\npada Windows) ke hanya \n. Saat menulis dalam mode teks, defaultnya adalah untuk mengonversi kejadian \nback to platform-specific line endings. Modifikasi di belakang layar untuk data file ini baik-baik saja untuk file teks, tetapi akan merusak data biner seperti itu di dalam JPEGatau EXEfile. Berhati-hatilah menggunakan mode biner saat membaca dan menulis file seperti itu.

Ini adalah praktik yang baik untuk menggunakan withkata kunci ketika berhadapan dengan objek file. Keuntungannya adalah bahwa file ditutup dengan benar setelah rangkaian selesai, bahkan jika pengecualian dibesarkan di beberapa titik. Penggunaannya withjuga jauh lebih pendek daripada menulis setara try- finallyblok:

>>>
>>> with open('workfile') as f:
...     read_data = f.read()
>>> f.closed
True
Jika Anda tidak menggunakan withkata kunci, maka Anda harus menelepon f.close()untuk menutup file dan segera membebaskan sumber daya sistem yang digunakan olehnya. Jika Anda tidak secara eksplisit menutup file, kolektor sampah Python akhirnya akan menghancurkan objek dan menutup file yang terbuka untuk Anda, tetapi file tersebut dapat tetap terbuka untuk sementara waktu. Risiko lain adalah implementasi Python yang berbeda akan melakukan pembersihan ini pada waktu yang berbeda.

Setelah objek file ditutup, baik oleh withpernyataan atau dengan menelepon f.close(), upaya untuk menggunakan objek file secara otomatis akan gagal.

>>>
>>> f.close()
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
7.2.1. Metode Objek File 
Sisa dari contoh di bagian ini akan menganggap bahwa objek file yang disebut ftelah dibuat.

Untuk membaca isi file, panggilan f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau byte objek (dalam mode biner). ukuran adalah argumen numerik opsional. Ketika ukuran dihapus atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file itu dua kali lebih besar dari memori mesin Anda. Jika tidak, paling banyak ukuran byte dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read()akan mengembalikan string kosong ( '').

>>>
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
f.readline()membaca satu baris dari file; karakter baris baru ( \n) dibiarkan di ujung string, dan hanya dihilangkan pada baris terakhir file jika file tidak berakhir di baris baru. Ini membuat nilai pengembalian tidak ambigu; jika f.readline()mengembalikan string kosong, akhir file telah tercapai, sementara garis kosong diwakili oleh '\n', string yang hanya berisi satu baris baru.

>>>
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''
Untuk membaca garis dari sebuah file, Anda dapat mengulang objek file. Ini adalah memori yang efisien, cepat, dan mengarah ke kode sederhana:

>>>
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
Jika Anda ingin membaca semua baris file dalam daftar, Anda juga dapat menggunakan list(f)atau f.readlines().

f.write(string)menulis isi string ke file, mengembalikan jumlah karakter yang ditulis.

>>>
>>> f.write('This is a test\n')
15
Jenis objek lain perlu dikonversi - baik ke string (dalam mode teks) atau objek byte (dalam mode biner) - sebelum menulisnya:

>>>
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
18
f.tell() mengembalikan sebuah integer yang memberikan posisi terkini file objek dalam file yang direpresentasikan sebagai jumlah byte dari awal file ketika dalam mode biner dan nomor buram ketika dalam mode teks.

Untuk mengubah posisi objek file, gunakan . Posisi dihitung dari penambahan offset ke titik referensi; titik referensi dipilih oleh argumen from_what . A from_what nilai 0 pengukuran dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan ujung file sebagai titik referensi. from_what dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.f.seek(offset, from_what)

>>>
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)      # Go to the 6th byte in the file
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)  # Go to the 3rd byte before the end
13
>>> f.read(1)
b'd'
Dalam file teks (yang dibuka tanpa bstring mode), hanya mencari relatif ke permulaan file yang diizinkan (pengecualian sedang mencari ke akhir file dengan ) dan satu-satunya nilai offset yang valid adalah yang dikembalikan dari , atau nol. Nilai offset lainnya menghasilkan perilaku tidak terdefinisi.seek(0, 2)f.tell()

Objek file memiliki beberapa metode tambahan, seperti isatty()dan truncate()yang lebih jarang digunakan; lihat Referensi Perpustakaan untuk panduan lengkap ke objek file.

7.2.2. Menyimpan data terstruktur dengan json
String dapat dengan mudah ditulis dan dibaca dari file. Angka perlu lebih banyak usaha, karena read()metode hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil string seperti '123' dan mengembalikan nilai numeriknya 123. Bila Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar bertingkat dan kamus, parsing dan serialisasi dengan tangan menjadi rumit.

Daripada meminta pengguna terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan Anda untuk menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation) . Modul standar yang disebut jsondapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serialisasi . Rekonstruksi data dari representasi string disebut deserializing . Antara serialisasi dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.

Catatan Format JSON umumnya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Banyak programmer sudah terbiasa dengannya, yang menjadikannya pilihan yang bagus untuk interoperabilitas.
Jika Anda memiliki objek x, Anda dapat melihat representasi string JSON-nya dengan baris kode sederhana:

>>>
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'
Varian lain dari dumps()fungsi, yang disebut dump(), hanya serializes objek ke file teks . Jadi jika fadalah file teks objek dibuka untuk menulis, kita bisa melakukan ini:

json.dump(x, f)
Untuk memecahkan kode objek lagi, jika fadalah file teks objek yang telah dibuka untuk membaca:

x = json.load(f)
Teknik serialisasi sederhana ini dapat menangani daftar dan kamus, tetapi serialisasi instance kelas arbitrer di JSON memerlukan sedikit usaha ekstra. Referensi untuk jsonmodul berisi penjelasan tentang ini.


8. Kesalahan dan Pengecualian 
Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contoh yang mungkin Anda lihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaksis dan pengecualian .

8.1. Kesalahan Sintaks 
Kesalahan sintaksis, juga dikenal sebagai kesalahan penguraian, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python:

>>>
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
Parser mengulangi garis yang menyinggung dan menampilkan sedikit 'panah' yang menunjuk pada titik paling awal di garis tempat kesalahan terdeteksi. Kesalahan ini disebabkan oleh (atau setidaknya terdeteksi pada) token yang mendahului panah: pada contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua ( ':') hilang sebelum itu. Nama file dan nomor baris dicetak sehingga Anda tahu di mana harus mencari jika input berasal dari skrip.

8.2. Pengecualian 
Bahkan jika pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan saat upaya dilakukan untuk mengeksekusinya. Kesalahan terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera belajar bagaimana menangani mereka dalam program Python. Sebagian besar pengecualian tidak ditangani oleh program, namun, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:

>>>
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
Baris terakhir dari pesan kesalahan menunjukkan apa yang terjadi. Pengecualian datang dalam berbagai jenis, dan jenis dicetak sebagai bagian dari pesan: jenis dalam contoh adalah ZeroDivisionError, NameErrordan TypeError. String yang dicetak sebagai tipe pengecualian adalah nama pengecualian built-in yang terjadi. Ini berlaku untuk semua pengecualian built-in, tetapi tidak perlu benar untuk pengecualian yang ditentukan pengguna (meskipun ini adalah konvensi yang berguna). Nama pengecualian standar adalah pengenal bawaan (bukan kata kunci yang dipesan).

Sisa baris memberikan detail berdasarkan jenis pengecualian dan apa yang menyebabkannya.

Bagian sebelumnya dari pesan kesalahan menunjukkan konteks di mana pengecualian terjadi, dalam bentuk traceback tumpukan. Secara umum ini berisi daftar baris sumber traceback stack; Namun, itu tidak akan menampilkan garis yang dibaca dari input standar.

Pengecualian Terpasang mencantumkan pengecualian built-in dan artinya.

8.3. Menangani Pengecualian 
Adalah mungkin untuk menulis program yang menangani pengecualian tertentu. Lihatlah contoh berikut, yang meminta pengguna untuk memasukkannya sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk mengganggu program (menggunakan Control-Catau apa pun yang didukung oleh sistem operasi); perhatikan bahwa interupsi yang dihasilkan pengguna ditandai dengan meningkatkan KeyboardInterruptpengecualian.

>>>
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
The tryPernyataan bekerja sebagai berikut.

Pertama, klausa coba (pernyataan antara trydan exceptkata kunci) dijalankan.
Jika tidak ada pengecualian, kecuali klausa dilewati dan eksekusi trypernyataan selesai.
Jika pengecualian terjadi selama pelaksanaan klausa coba, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan pengecualian yang dinamai setelah exceptkata kunci, kecuali klausa dijalankan, dan kemudian eksekusi berlanjut setelah trypernyataan.
Jika pengecualian terjadi yang tidak cocok dengan pengecualian yang disebutkan dalam klausul kecuali, itu diteruskan ke trypernyataan luar ; jika tidak ada handler yang ditemukan, itu adalah eksepsi yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.
Sebuah trypernyataan mungkin memiliki lebih dari satu kecuali klausa, untuk menentukan handler untuk pengecualian yang berbeda. Paling banyak satu handler akan dieksekusi. Penangan hanya menangani pengecualian yang terjadi dalam klausa percobaan yang sesuai, bukan pada penangan lain dari trypernyataan yang sama . Kecuali klausa dapat menyebutkan beberapa pengecualian sebagai tupel yang disisipkan, misalnya:

... except (RuntimeError, TypeError, NameError):
...     pass
Kelas dalam exceptklausa kompatibel dengan pengecualian jika kelas yang sama atau kelas dasar daripadanya (tetapi bukan sebaliknya - klausul kecuali klausul kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
Perhatikan bahwa jika kecuali klausa dibalik (dengan pertama), itu akan mencetak B, B, B - pencocokan pertama kecuali klausa dipicu.except B

Klausul terakhir kecuali klausa dapat menghilangkan nama pengecualian (s), untuk melayani sebagai wildcard. Gunakan ini dengan sangat hati-hati, karena mudah untuk menutupi kesalahan pemrograman nyata dengan cara ini! Ini juga dapat digunakan untuk mencetak pesan kesalahan dan kemudian kembali menaikkan pengecualian (memungkinkan pemanggil untuk menangani pengecualian juga):

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
The try... exceptPernyataan memiliki opsional lain klausul , yang, ketika hadir, harus mengikuti semua kecuali klausa. Ini berguna untuk kode yang harus dijalankan jika klausa coba tidak meningkatkan pengecualian. Sebagai contoh:

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
Penggunaan elseklausul lebih baik daripada menambahkan kode tambahan ke tryklausa karena menghindari secara tidak sengaja menangkap pengecualian yang tidak dibangkitkan oleh kode yang dilindungi oleh try... exceptpernyataan.

Ketika pengecualian terjadi, mungkin memiliki nilai terkait, juga dikenal sebagai argumen pengecualian . Kehadiran dan jenis argumen bergantung pada jenis pengecualian.

Kecuali klausa dapat menentukan variabel setelah nama pengecualian. Variabel terikat pada instance pengecualian dengan argumen yang disimpan di instance.args. Untuk kenyamanan, contoh pengecualian mendefinisikan __str__()sehingga argumen dapat dicetak secara langsung tanpa harus referensi .args. Seseorang juga dapat memberi contoh pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan.

>>>
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
Jika pengecualian memiliki argumen, mereka dicetak sebagai bagian terakhir ('detail') dari pesan untuk pengecualian yang tidak tertangani.

Penangan pengecualian tidak hanya menangani pengecualian jika terjadi segera dalam klausa coba, tetapi juga jika terjadi di dalam fungsi yang dipanggil (bahkan secara tidak langsung) dalam klausa coba. Sebagai contoh:

>>>
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
8.4. Meningkatkan Pengecualian 
The raisepernyataan memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Sebagai contoh:

>>>
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
Argumen tunggal untuk raisemenunjukkan pengecualian yang akan dibangkitkan. Ini harus berupa instance pengecualian atau kelas pengecualian (kelas yang berasal dari Exception). Jika kelas pengecualian dilewatkan, maka akan secara implisit diinformasikan dengan memanggil konstruktornya tanpa argumen:

raise ValueError  # shorthand for 'raise ValueError()'
Jika Anda perlu menentukan apakah pengecualian dibangkitkan tetapi tidak berniat untuk mengatasinya, bentuk raisepernyataan yang lebih sederhana memungkinkan Anda untuk kembali menaikkan pengecualian:

>>>
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
8,5. Pengecualian yang ditentukan pengguna 
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat Kelas untuk lebih lanjut tentang kelas Python). Pengecualian biasanya harus berasal dari Exceptionkelas, baik secara langsung maupun tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa saja yang dapat dilakukan kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan untuk diekstraksi oleh penangan untuk pengecualian. Saat membuat modul yang dapat meningkatkan beberapa kesalahan berbeda, praktik umum adalah membuat kelas dasar untuk pengecualian yang ditentukan oleh modul itu, dan subkelas itu untuk membuat kelas pengecualian khusus untuk berbagai kondisi kesalahan:

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
Kebanyakan pengecualian didefinisikan dengan nama yang diakhiri dengan "Kesalahan", mirip dengan penamaan pengecualian standar.

Banyak modul standar menentukan pengecualian mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi dalam fungsi yang mereka tetapkan. Informasi lebih lanjut tentang kelas disajikan di Kelas bab .

8.6. Mendefinisikan Tindakan Pembersihan 
The trypernyataan memiliki klausul opsional lain yang dimaksudkan untuk menentukan tindakan bersih-bersih yang harus dijalankan dalam semua keadaan. Sebagai contoh:

>>>
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
Sebuah akhirnya klausul selalu dijalankan sebelum meninggalkan try pernyataan, apakah pengecualian telah terjadi atau tidak. Ketika pengecualian telah terjadi dalam tryklausa dan belum ditangani oleh exceptklausa (atau telah terjadi dalam klausa exceptatau elseklausul), pengecualian itu dinaikkan kembali setelah finallyklausa telah dieksekusi. The finallyklausul juga dieksekusi “di jalan keluar” ketika salah klausul lain dari trypernyataan yang tersisa melalui break, continueatau returnpernyataan. Contoh yang lebih rumit:

>>>
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
Seperti yang Anda lihat, finallyklausa dijalankan dalam hal apa pun. Yang TypeErrordibangkitkan dengan membagi dua string tidak ditangani oleh exceptklausa dan karena itu dibesarkan kembali setelah finally klausa telah dieksekusi.

Dalam aplikasi dunia nyata, finallyklausa ini berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya berhasil.

8.7. Aksi bersih-bersih yang telah ditentukan sebelumnya 
Beberapa objek menetapkan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka file dan mencetak isinya ke layar.

for line in open("myfile.txt"):
    print(line, end="")
Masalah dengan kode ini adalah bahwa ia membiarkan file terbuka untuk waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. The withPernyataan memungkinkan objek seperti file yang akan digunakan dengan cara yang menjamin mereka selalu dibersihkan segera dan benar.

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
Setelah pernyataan dijalankan, file f selalu tertutup, bahkan jika ada masalah saat memproses garis. Objek yang, seperti file, menyediakan tindakan bersih-bersih yang telah ditentukan akan menunjukkan ini dalam dokumentasi mereka.


9. Kelas 
Kelas menyediakan sarana untuk menggabungkan data dan fungsi bersama. Membuat kelas baru menciptakan jenis objek baru, yang memungkinkan instance baru dari jenis itu dibuat. Setiap instance kelas dapat memiliki atribut yang melekat padanya untuk mempertahankan statusnya. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi keadaannya.

Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambahkan kelas dengan minimum sintaks dan semantik yang baru. Ini adalah campuran dari mekanisme kelas yang ditemukan di C ++ dan Modula-3. Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat mengesampingkan metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang sewenang-wenang. Seperti benar untuk modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.

Dalam terminologi C ++, biasanya anggota kelas (termasuk anggota data) bersifat publik (kecuali lihat di bawah Variabel Pribadi ), dan semua fungsi anggota adalah virtual . Seperti dalam Modula-3, tidak ada singkatan untuk mereferensikan anggota objek dari metodenya: fungsi metode dideklarasikan dengan argumen pertama eksplisit yang mewakili objek, yang diberikan secara implisit oleh panggilan. Seperti dalam Smalltalk, kelas itu sendiri adalah objek. Ini menyediakan semantik untuk mengimpor dan mengganti nama. Tidak seperti C ++ dan Modula-3, tipe built-in dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C ++, sebagian besar operator built-in dengan sintaks khusus (operator aritmatika, subscripting, dll.) Dapat didefinisikan ulang untuk instance kelas.

(Kurang terminologi yang diterima secara universal untuk berbicara tentang kelas, saya akan menggunakan istilah Smalltalk dan C ++ sesekali. Saya akan menggunakan istilah Modula-3, karena semantik berorientasi objeknya lebih dekat dengan Python daripada C ++, tapi saya berharap bahwa beberapa pembaca telah mendengarnya.)

9.1. Sebuah Kata Tentang Nama dan Objek 
Objek memiliki individualitas, dan beberapa nama (dalam berbagai cakupan) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama Python, dan dapat dengan aman diabaikan ketika berhadapan dengan tipe dasar yang tidak dapat diubah (angka, string, tupel). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang dapat berubah seperti daftar, kamus, dan sebagian besar jenis lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias bertindak seperti pointer dalam beberapa hal. Sebagai contoh, melewati suatu objek adalah murah karena hanya pointer yang dilewatkan oleh implementasi; dan jika fungsi memodifikasi objek yang dilewatkan sebagai argumen, pemanggil akan melihat perubahan - ini menghilangkan kebutuhan untuk dua mekanisme pengalihan argumen yang berbeda seperti dalam Pascal.

9.2. Lingkup Python dan Namespaces 
Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda sesuatu tentang aturan lingkup Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama, dan Anda perlu tahu bagaimana ruang lingkup dan ruang nama berfungsi untuk memahami apa yang terjadi. Kebetulan, pengetahuan tentang subjek ini berguna untuk programmer Python maju.

Mari kita mulai dengan beberapa definisi.

Sebuah namespace adalah pemetaan dari nama ke objek. Kebanyakan ruang nama saat ini diimplementasikan sebagai kamus Python, tetapi itu biasanya tidak terlihat dengan cara apa pun (kecuali untuk kinerja), dan mungkin berubah di masa depan. Contoh ruang nama adalah: kumpulan nama bawaan (berisi fungsi seperti abs(), dan nama pengecualian internal); nama-nama global dalam sebuah modul; dan nama-nama lokal dalam doa fungsi. Dalam arti set atribut suatu objek juga membentuk namespace. Yang penting untuk diketahui tentang ruang nama adalah bahwa sama sekali tidak ada hubungan antara nama di ruang nama yang berbeda; misalnya, dua modul yang berbeda dapat mendefinisikan fungsi maximizetanpa kebingungan - pengguna modul harus menambahkannya dengan nama modul.

By the way, saya menggunakan atribut kata untuk setiap nama mengikuti titik - misalnya, dalam ekspresi z.real, realadalah atribut objek z. Secara tegas, referensi untuk nama dalam modul adalah referensi atribut: dalam ekspresi modname.funcname, modnameadalah objek modul dan funcnamemerupakan atributnya. Dalam hal ini terjadi pemetaan langsung antara atribut modul dan nama global yang didefinisikan dalam modul: mereka berbagi namespace yang sama! [1]

Atribut dapat bersifat hanya-baca atau dapat ditulis. Dalam kasus terakhir, penugasan ke atribut dimungkinkan. Atribut modul dapat ditulis: Anda dapat menulis . Atribut yang dapat ditulis mungkin juga dihapus dengan pernyataan itu. Misalnya, akan menghapus atribut dari objek yang bernama oleh .modname.the_answer = 42deldel modname.the_answerthe_answermodname

Namespaces dibuat pada momen yang berbeda dan memiliki masa kehidupan yang berbeda. Namespace yang berisi nama built-in dibuat ketika interpreter Python dijalankan, dan tidak pernah dihapus. Namespace global untuk modul dibuat ketika definisi modul dibaca; biasanya, ruang nama modul juga bertahan sampai juru bahasa berhenti. Pernyataan yang dieksekusi oleh permintaan tingkat tinggi dari interpreter, baik dibaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut __main__, sehingga mereka memiliki namespace global mereka sendiri. (Nama-nama bawaan sebenarnya juga tinggal di modul; ini disebut builtins.)

Namespace lokal untuk fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi mengembalikan atau memunculkan eksepsi yang tidak ditangani dalam fungsi. (Sebenarnya, melupakan akan menjadi cara yang lebih baik untuk menggambarkan apa yang sebenarnya terjadi.) Tentu saja, rekursif panggilan masing-masing memiliki namespace lokal mereka sendiri.

Sebuah lingkup adalah wilayah tekstual dari program Python di mana namespace secara langsung dapat diakses. "Langsung dapat diakses" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk nama berusaha untuk menemukan nama di ruang nama.

Meskipun ruang lingkup ditentukan secara statis, cakupannya digunakan secara dinamis. Kapan saja selama eksekusi, setidaknya ada tiga lingkup bersarang yang namespace-nya dapat diakses secara langsung:

ruang lingkup paling dalam, yang dicari pertama kali, berisi nama-nama lokal
lingkup dari setiap fungsi melampirkan, yang dicari dimulai dengan lingkup melampirkan terdekat, mengandung non-lokal, tetapi juga nama-nama non-global
lingkup berikutnya-ke-akhir berisi nama global modul saat ini
ruang lingkup terluar (dicari terakhir) adalah namespace yang berisi nama-nama bawaan
Jika nama dideklarasikan secara global, maka semua referensi dan tugas langsung ke ruang lingkup tengah yang berisi nama global modul. Untuk variabel rebind ditemukan di luar ruang lingkup paling dalam, nonlocalpernyataan dapat digunakan; jika tidak dideklarasikan nonlocal, variabel-variabel tersebut bersifat read-only (sebuah upaya untuk menulis ke variabel tersebut hanya akan membuat variabel lokal baru dalam ruang lingkup paling dalam, meninggalkan variabel luar yang bernama identik tidak berubah).

Biasanya, lingkup lokal referensi nama-nama lokal dari fungsi (tekstual) saat ini. Di luar fungsi, ruang lingkup lokal referensi namespace yang sama dengan lingkup global: namespace modul. Definisi kelas menempatkan namespace lain di lingkup lokal.

Penting untuk menyadari bahwa lingkup ditentukan secara tekstual: ruang lingkup global dari fungsi yang didefinisikan dalam modul adalah ruang nama modul, tidak peduli dari mana atau oleh apa alias fungsi tersebut dipanggil. Di sisi lain, pencarian nama yang sebenarnya dilakukan secara dinamis, pada saat dijalankan - namun, definisi bahasa sedang berkembang menuju resolusi nama statis, pada waktu "kompilasi", jadi jangan bergantung pada resolusi nama dinamis! (Faktanya, variabel lokal sudah ditentukan secara statis.)

Sebuah quirk khusus dari Python adalah bahwa - jika tidak ada globalpernyataan yang berlaku - tugas untuk nama selalu masuk ke ruang lingkup terdalam. Tugas tidak menyalin data - mereka hanya mengikat nama ke objek. Hal yang sama berlaku untuk penghapusan: pernyataan ini menghapus pengikatan dari ruang nama yang direferensikan oleh lingkup lokal. Bahkan, semua operasi yang memperkenalkan nama-nama baru menggunakan lingkup lokal: khususnya, pernyataan dan definisi fungsi mengikat modul atau nama fungsi dalam lingkup lokal.del xximport

The globalpernyataan dapat digunakan untuk menunjukkan bahwa variabel tertentu hidup dalam lingkup global dan harus pulih di sana; yang nonlocalpernyataan menunjukkan bahwa variabel tertentu hidup di lingkup melampirkan dan harus pulih sana.

9.2.1. Ruang Lingkup dan Ruang Lingkup Contoh 
Ini adalah contoh yang menunjukkan bagaimana referensi ruang lingkup dan ruang nama yang berbeda, dan bagaimana globaldan nonlocalmempengaruhi pengikatan variabel:

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)
Output dari kode contoh adalah:

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
Perhatikan bagaimana penugasan lokal (yang merupakan default) tidak mengubah pengalih lingkup lingkup_test untuk spam . The nonlocaltugas berubah scope_test ‘s pengikatan spam yang , dan globaltugas mengubah modul-tingkat mengikat.

Anda juga dapat melihat bahwa tidak ada pengikatan sebelumnya untuk spam sebelum globalpenugasan.

9.3. Pandangan Pertama di Kelas 
Kelas memperkenalkan sedikit sintaks baru, tiga jenis objek baru, dan beberapa semantik baru.

9.3.1. Sintaks Definisi Kelas 
Bentuk definisi kelas yang paling sederhana terlihat seperti ini:

class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
Definisi kelas, seperti definisi fungsi ( defpernyataan) harus dijalankan sebelum mereka memiliki efek apa pun. (Anda mungkin bisa menempatkan definisi kelas dalam cabang ifpernyataan, atau di dalam suatu fungsi.)

Dalam praktiknya, pernyataan di dalam definisi kelas biasanya akan menjadi definisi fungsi, tetapi pernyataan lain diperbolehkan, dan terkadang berguna - kita akan kembali ke ini nanti. Definisi fungsi di dalam kelas biasanya memiliki bentuk aneh daftar argumen, didikte oleh konvensi pemanggilan untuk metode - lagi, ini dijelaskan nanti.

Ketika sebuah definisi kelas dimasukkan, sebuah namespace baru dibuat, dan digunakan sebagai ruang lingkup lokal - dengan demikian, semua tugas untuk variabel lokal masuk ke ruang nama baru ini. Secara khusus, definisi fungsi mengikat nama fungsi baru di sini.

Ketika definisi kelas dibiarkan secara normal (melalui akhirnya), objek kelas dibuat. Ini pada dasarnya adalah pembungkus di sekitar isi dari namespace yang dibuat oleh definisi kelas; kita akan belajar lebih banyak tentang objek kelas di bagian selanjutnya. Lingkup lokal asli (yang berlaku tepat sebelum definisi kelas dimasukkan) dipulihkan, dan objek kelas terikat di sini ke nama kelas yang diberikan di header definisi kelas ( ClassNamedalam contoh).

9.3.2. Objek Kelas 
Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.

Atribut referensi menggunakan sintaks standar yang digunakan untuk semua referensi atribut dengan Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di ruang nama kelas ketika objek kelas dibuat. Jadi, jika definisi kelas terlihat seperti ini:

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
kemudian MyClass.idan MyClass.freferensi atribut yang valid, mengembalikan sebuah integer dan objek fungsi, masing-masing. Atribut kelas juga dapat ditetapkan, sehingga Anda dapat mengubah nilai MyClass.iberdasarkan tugas. __doc__juga merupakan atribut yang valid, mengembalikan docstring milik kelas: ."A simple example class"

Instansiasi kelas menggunakan notasi fungsi. Hanya berpura-pura bahwa objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas. Misalnya (dengan asumsi kelas di atas):

x = MyClass()
membuat instance baru dari kelas dan memberikan objek ini ke variabel lokal x.

Operasi instantiasi ("memanggil" objek kelas) menciptakan objek kosong. Banyak kelas suka membuat objek dengan instance yang disesuaikan dengan keadaan awal tertentu. Oleh karena itu kelas dapat menentukan metode khusus bernama __init__(), seperti ini:

def __init__(self):
    self.data = []
Ketika sebuah kelas mendefinisikan __init__()metode, instantiasi kelas secara otomatis memanggil __init__()untuk instance kelas yang baru dibuat. Jadi dalam contoh ini, instance baru yang diinisialisasi dapat diperoleh dengan:

x = MyClass()
Tentu saja, __init__()metode ini mungkin memiliki argumen untuk fleksibilitas yang lebih besar. Dalam hal ini, argumen yang diberikan kepada operator Instansiasi kelas diteruskan ke __init__(). Sebagai contoh,

>>>
>>> class Complex:
...     def __init__(self, realpart, imagpart):
...         self.r = realpart
...         self.i = imagpart
...
>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
9.3.3. Instance Objek 
Sekarang apa yang bisa kita lakukan dengan objek contoh? Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid, atribut data dan metode.

atribut data sesuai dengan "variabel instan" di Smalltalk, dan ke "anggota data" di C ++. Atribut data tidak perlu dideklarasikan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan. Misalnya, jika xinstance MyClassdibuat di atas, potongan kode berikut akan mencetak nilainya 16, tanpa meninggalkan jejak:

x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
Jenis referensi atribut instan lainnya adalah metode . Metode adalah fungsi yang "milik" suatu objek. (Dalam Python, metode jangka tidak unik untuk instance kelas: jenis objek lain dapat memiliki metode juga. Misalnya, objek daftar memiliki metode yang disebut append, insert, remove, sort, dan sebagainya. Namun, dalam diskusi berikut, kami akan menggunakan metode istilah secara eksklusif untuk mengartikan metode objek instance kelas, kecuali secara eksplisit dinyatakan sebaliknya.)

Nama metode yang valid dari objek instance bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi menentukan metode yang sesuai dari instance-nya. Jadi dalam contoh kita, x.fadalah referensi metode yang valid, karena MyClass.fmerupakan fungsi, tetapi x.itidak, karena MyClass.itidak. Tetapi x.ftidak sama dengan MyClass.f- itu adalah objek metode , bukan objek fungsi.

9.3.4. Objek Metode 
Biasanya, metode dipanggil tepat setelah terikat:

x.f()
Dalam MyClasscontoh, ini akan mengembalikan string . Namun, tidak perlu memanggil metode segera: adalah objek metode, dan dapat disimpan dan dipanggil di lain waktu. Sebagai contoh:'hello world'x.f

xf = x.f
while True:
    print(xf())
akan terus dicetak hingga akhir waktu.hello world

Apa sebenarnya yang terjadi ketika sebuah metode dipanggil? Anda mungkin telah memperhatikan bahwa x.f()dipanggil tanpa argumen di atas, meskipun definisi fungsi untuk f()menentukan argumen. Apa yang terjadi dengan argumen itu? Tentunya Python memunculkan eksepsi ketika sebuah fungsi yang membutuhkan argumen dipanggil tanpa - bahkan jika argumen tersebut tidak benar-benar digunakan ...

Sebenarnya, Anda mungkin telah menebak jawabannya: hal khusus tentang metode adalah objek instance dilewatkan sebagai argumen pertama dari fungsi. Dalam contoh kami, panggilan x.f()persis sama dengan MyClass.f(x). Secara umum, memanggil metode dengan daftar n argumen sama dengan memanggil fungsi yang terkait dengan daftar argumen yang dibuat dengan memasukkan objek contoh metode sebelum argumen pertama.

Jika Anda masih tidak mengerti cara kerja metode, melihat implementasi mungkin bisa memperjelas masalah. Ketika atribut non-data dari suatu instance direferensikan, kelas instance akan dicari. Jika nama menunjukkan atribut kelas yang valid yang merupakan objek fungsi, objek metode dibuat dengan mengepak (menunjuk ke) objek contoh dan objek fungsi hanya ditemukan bersama-sama dalam objek abstrak: ini adalah objek metode. Ketika objek metode dipanggil dengan daftar argumen, daftar argumen baru dibangun dari objek contoh dan daftar argumen, dan objek fungsi dipanggil dengan daftar argumen baru ini.

9.3.5. Kelas dan Instance Variabel 
Secara umum, variabel instan adalah untuk data unik untuk setiap instance dan variabel kelas untuk atribut dan metode yang dibagikan oleh semua instance kelas:

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
Sebagaimana dibahas dalam A Word About Names and Objects , data yang dibagikan dapat memiliki efek yang mengejutkan dengan melibatkan objek yang dapat berubah seperti daftar dan kamus. Misalnya, daftar trik dalam kode berikut tidak boleh digunakan sebagai variabel kelas karena hanya satu daftar yang akan dibagikan oleh semua instance Anjing :

class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
Desain kelas yang benar harus menggunakan variabel instan sebagai gantinya:

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
9.4. Komentar Acak 
Atribut data mengesampingkan atribut metode dengan nama yang sama; untuk menghindari konflik nama yang disengaja, yang dapat menyebabkan bug yang sulit ditemukan dalam program besar, adalah bijaksana untuk menggunakan beberapa jenis konvensi yang meminimalkan kemungkinan konflik. Konvensi yang mungkin termasuk mengkapitalisasi nama metode, mengawali nama atribut data dengan string unik kecil (mungkin hanya garis bawah), atau menggunakan kata kerja untuk metode dan kata benda untuk atribut data.

Atribut data dapat direferensikan oleh metode serta oleh pengguna biasa ("klien") dari suatu objek. Dengan kata lain, kelas tidak dapat digunakan untuk mengimplementasikan tipe data abstrak murni. Bahkan, tidak ada dalam Python memungkinkan untuk menegakkan penyembunyian data - itu semua didasarkan pada konvensi. (Di sisi lain, implementasi Python, yang ditulis dalam C, benar-benar dapat menyembunyikan detail implementasi dan mengontrol akses ke objek jika perlu; ini dapat digunakan oleh ekstensi untuk Python yang ditulis dalam C.)

Klien harus menggunakan atribut data dengan hati-hati - klien dapat mengacaukan invariants yang dikelola oleh metode dengan memberi stempel pada atribut datanya. Perhatikan bahwa klien dapat menambahkan atribut data mereka sendiri ke objek instan tanpa mempengaruhi validitas metode, selama konflik nama dihindari - lagi, konvensi penamaan dapat menghemat banyak sakit kepala di sini.

Tidak ada singkatan untuk referensi atribut data (atau metode lain!) Dari dalam metode. Saya menemukan bahwa ini benar-benar meningkatkan pembacaan metode: tidak ada kemungkinan untuk membingungkan variabel lokal dan variabel instan ketika melirik melalui suatu metode.

Seringkali, argumen pertama dari suatu metode dipanggil self. Ini tidak lebih dari sebuah konvensi: nama selfsama sekali tidak memiliki arti khusus untuk Python. Perhatikan, bagaimanapun, bahwa dengan tidak mengikuti konvensi, kode Anda mungkin kurang dapat dibaca oleh pemrogram Python lainnya, dan juga dapat dibayangkan bahwa program browser kelas mungkin ditulis yang bergantung pada konvensi semacam itu.

Objek fungsi apa pun yang merupakan atribut kelas mendefinisikan metode untuk instance kelas tersebut. Tidak perlu definisi fungsi dilampirkan secara tekstual dalam definisi kelas: menetapkan objek fungsi ke variabel lokal di kelas juga ok. Sebagai contoh:

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g
Sekarang f, gdan hsemua atribut kelas Cyang mengacu pada objek fungsi, dan akibatnya mereka semua metode contoh C- hyang persis setara dengan g. Perhatikan bahwa praktik ini biasanya hanya berfungsi untuk membingungkan pembaca program.

Metode dapat memanggil metode lain dengan menggunakan atribut metode self argumen:

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
Metode dapat merujuk nama global dengan cara yang sama seperti fungsi biasa. Ruang lingkup global yang terkait dengan suatu metode adalah modul yang berisi definisinya. (Sebuah kelas tidak pernah digunakan sebagai ruang lingkup global.) Sementara seseorang jarang menemukan alasan yang baik untuk menggunakan data global dalam suatu metode, ada banyak penggunaan yang sah dari lingkup global: untuk satu hal, fungsi dan modul yang diimpor ke dalam lingkup global dapat digunakan oleh metode, serta fungsi dan kelas yang ditentukan di dalamnya. Biasanya, kelas yang berisi metode itu sendiri didefinisikan dalam lingkup global ini, dan di bagian berikutnya kita akan menemukan beberapa alasan bagus mengapa suatu metode ingin mereferensikan kelasnya sendiri.

Setiap nilai adalah objek, dan oleh karena itu memiliki kelas (juga disebut jenisnya ). Itu disimpan sebagai object.__class__.

9.5. Warisan 
Tentu saja, fitur bahasa tidak akan layak untuk nama "kelas" tanpa mendukung warisan. Sintaks untuk definisi kelas turunan terlihat seperti ini:

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
Nama BaseClassNameharus didefinisikan dalam ruang lingkup yang berisi definisi kelas turunan. Di tempat dari nama kelas dasar, ekspresi arbitrer lainnya juga diperbolehkan. Ini dapat bermanfaat, misalnya, ketika kelas dasar didefinisikan dalam modul lain:

class DerivedClassName(modname.BaseClassName):
Eksekusi definisi kelas turunan berlangsung sama dengan kelas dasar. Ketika objek kelas dibangun, kelas dasar dikenang. Ini digunakan untuk menyelesaikan referensi atribut: jika atribut yang diminta tidak ditemukan di kelas, pencarian dilanjutkan ke kelas dasar. Aturan ini diterapkan secara rekursif jika kelas dasar itu sendiri berasal dari beberapa kelas lain.

Tidak ada yang istimewa tentang Instansiasi kelas turunan: DerivedClassName()membuat instance baru dari kelas. Referensi metode diselesaikan sebagai berikut: atribut kelas yang sesuai dicari, menuruni rantai kelas dasar jika diperlukan, dan referensi metode valid jika ini menghasilkan objek fungsi.

Kelas turunan dapat menggantikan metode kelas dasar mereka. Karena metode tidak memiliki hak khusus ketika memanggil metode lain dari objek yang sama, metode kelas dasar yang memanggil metode lain yang didefinisikan dalam kelas dasar yang sama dapat berakhir dengan memanggil metode kelas turunan yang menimpanya. (Untuk programmer C ++: semua metode dalam Python efektif virtual.)

Metode override di kelas turunan mungkin sebenarnya ingin memperpanjang bukan hanya mengganti metode kelas dasar dengan nama yang sama. Ada cara sederhana untuk memanggil metode kelas dasar secara langsung: panggil saja . Ini kadang-kadang bermanfaat untuk klien juga. (Perhatikan bahwa ini hanya berfungsi jika kelas dasar dapat diakses seperti dalam lingkup global.)BaseClassName.methodname(self, arguments)BaseClassName

Python memiliki dua fungsi built-in yang berfungsi dengan warisan:

Gunakan isinstance()untuk memeriksa jenis instance: hanya akan jika ada atau beberapa kelas berasal .isinstance(obj, int)Trueobj.__class__intint
Gunakan issubclass()untuk memeriksa warisan kelas: adalah karena merupakan subclass dari . Namun, adalah karena tidak subclass dari .issubclass(bool, int)Trueboolintissubclass(float, int)Falsefloatint
9.5.1. Warisan Ganda 
Python mendukung bentuk multiple inheritance juga. Definisi kelas dengan beberapa kelas dasar terlihat seperti ini:

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
Untuk sebagian besar tujuan, dalam kasus yang paling sederhana, Anda dapat memikirkan pencarian atribut yang diwarisi dari kelas induk sebagai kedalaman-pertama, kiri-ke-kanan, tidak mencari dua kali di kelas yang sama di mana ada tumpang tindih dalam hierarki. Jadi, jika suatu atribut tidak ditemukan DerivedClassName, ia dicari di dalam Base1, kemudian (secara rekursif) dalam kelas-kelas dasar Base1, dan jika tidak ditemukan di sana, ia ditelusuri Base2, dan seterusnya.

Sebenarnya, ini sedikit lebih kompleks dari itu; urutan resolusi metode berubah secara dinamis untuk mendukung panggilan kooperatif super(). Pendekatan ini dikenal dalam beberapa bahasa multi-warisan lainnya sebagai metode panggilan-berikutnya dan lebih kuat daripada panggilan super yang ditemukan dalam bahasa warisan tunggal.

Urutan dinamis diperlukan karena semua kasus pewarisan berganda menunjukkan satu atau lebih hubungan berlian (di mana setidaknya satu dari kelas induk dapat diakses melalui beberapa jalur dari kelas paling bawah). Sebagai contoh, semua kelas mewarisi dari object, jadi setiap kasus multiple inheritance menyediakan lebih dari satu jalur untuk dijangkau object. Agar kelas dasar tidak dapat diakses lebih dari satu kali, algoritme dinamis akan membuat garis keturunan urutan pencarian dengan cara mempertahankan urutan kiri-ke-kanan yang ditentukan di setiap kelas, yang memanggil setiap orang tua hanya sekali, dan itu monotonik (artinya kelas dapat digolongkan tanpa mempengaruhi urutan prioritas dari orang tuanya). Secara bersama-sama, properti ini memungkinkan untuk mendesain kelas yang dapat diandalkan dan diperluas dengan multiple inheritance. Untuk detail lebih lanjut, lihat https://www.python.org/download/releases/2.3/mro/ .

9,6. Variabel Pribadi 
Variabel instan "Pribadi" yang tidak dapat diakses kecuali dari dalam objek tidak ada dalam Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: sebuah nama yang diawali dengan garis bawah (misalnya _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data). Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.

Karena ada kasus penggunaan yang valid untuk anggota kelas-pribadi (yaitu untuk menghindari bentrokan nama nama dengan nama yang ditentukan oleh subclass), ada dukungan terbatas untuk mekanisme seperti itu, yang disebut pengawetan nama . Setiap pengidentifikasi bentuk __spam(setidaknya dua garis bawah yang menonjol, paling banyak satu garis bawah trailing) diganti secara tekstual dengan _classname__spam, di mana classnamenama kelas saat ini dengan garis bawah terdistorsi (s) dilucuti. Penggerebekan ini dilakukan tanpa memperhatikan posisi sintaksis identifier, selama itu terjadi dalam definisi kelas.

Name mangling sangat membantu untuk membiarkan subclass mengesampingkan metode tanpa melanggar panggilan metode intraclass. Sebagai contoh:

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
Perhatikan bahwa aturan pengurusan dirancang sebagian besar untuk menghindari kecelakaan; masih dimungkinkan untuk mengakses atau memodifikasi variabel yang dianggap pribadi. Ini bahkan dapat berguna dalam keadaan khusus, seperti di debugger.

Perhatikan bahwa kode diteruskan ke exec()atau eval()tidak mempertimbangkan nama kelas dari kelas yang meminta untuk menjadi kelas saat ini; ini mirip dengan efek globalpernyataan, efeknya juga dibatasi pada kode yang dikompilasi bersama-sama. Pembatasan yang sama berlaku untuk getattr(), setattr()dan delattr(), serta ketika referensi __dict__secara langsung.

9,7. Peluang dan Berakhir 
Terkadang berguna untuk memiliki tipe data yang mirip dengan "record" Pascal atau C "struct", menggabungkan beberapa item data bernama. Definisi kelas kosong akan dilakukan dengan baik:

class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000
Sepotong kode Python yang mengharapkan tipe data abstrak tertentu sering dapat dilewatkan kelas yang mengemulasi metode dari tipe data itu sebagai gantinya. Misalnya, jika Anda memiliki fungsi yang memformat beberapa data dari objek file, Anda dapat menentukan kelas dengan metode read()dan readline()yang mendapatkan data dari penyangga string sebagai gantinya, dan menyebarkannya sebagai argumen.

Objek metode Instance memiliki atribut juga: m.__self__adalah objek contoh dengan metode m(), dan m.__func__merupakan objek fungsi yang sesuai dengan metode.

9,8. Iterator 
Sekarang Anda mungkin telah memperhatikan bahwa sebagian besar objek kontainer dapat diulang menggunakan forpernyataan:

for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
Gaya akses ini jelas, ringkas, dan nyaman. Penggunaan iterator meliputi dan menyatukan Python. Di belakang layar, forpernyataan itu memanggil iter()objek kontainer. Fungsi mengembalikan objek iterator yang mendefinisikan metode __next__()yang mengakses elemen dalam wadah satu per satu. Ketika tidak ada lagi elemen, __next__()memunculkan StopIterationeksepsi yang memberitahu forloop untuk mengakhiri. Anda dapat memanggil __next__()metode menggunakan fungsi next()built-in; contoh ini menunjukkan cara kerjanya:

>>>
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
Setelah melihat mekanisme di balik protokol iterator, mudah untuk menambahkan perilaku iterator ke kelas Anda. Tentukan __iter__()metode yang mengembalikan objek dengan __next__()metode. Jika kelas mendefinisikan __next__(), maka __iter__()dapat kembali self:

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
>>>
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
9.9. Generator 
Generator s adalah alat sederhana dan kuat untuk menciptakan iterator. Mereka ditulis seperti fungsi biasa tetapi gunakanyieldpernyataan kapan pun mereka ingin mengembalikan data. Setiap kalinext()dipanggil, generator meneruskannya kembali (mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi). Contoh menunjukkan bahwa generator dapat mudah dibuat dengan mudah:

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
>>>
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
Apa pun yang dapat dilakukan dengan generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan di bagian sebelumnya. Apa yang membuat generator begitu kompak adalah bahwa __iter__()dan __next__()metode dibuat secara otomatis.

Fitur kunci lainnya adalah bahwa variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat fungsi lebih mudah ditulis dan lebih jelas daripada pendekatan menggunakan variabel instan seperti self.index dan self.data.

Selain pembuatan metode otomatis dan menyimpan negara program, ketika generator berhenti, mereka secara otomatis meningkat StopIteration. Dalam kombinasi, fitur-fitur ini membuatnya mudah untuk membuat iterator tanpa upaya lebih dari menulis fungsi biasa.

9.10. Ekspresi Generator 
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaks yang mirip dengan daftar pemahaman tetapi dengan tanda kurung bukan tanda kurung siku. Ekspresi ini dirancang untuk situasi di mana generator digunakan langsung oleh fungsi melampirkan. Ekspresi generator lebih ringkas tetapi kurang serbaguna daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar ekuivalen.

Contoh:

>>>
>>> sum(i*i for i in range(10))                 # sum of squares
285

>>> xvec = [10, 20, 30]
>>> yvec = [7, 5, 3]
>>> sum(x*y for x,y in zip(xvec, yvec))         # dot product
260

>>> from math import pi, sin
>>> sine_table = {x: sin(x*pi/180) for x in range(0, 91)}

>>> unique_words = set(word  for line in page  for word in line.split())

>>> valedictorian = max((student.gpa, student.name) for student in graduates)

>>> data = 'golf'
>>> list(data[i] for i in range(len(data)-1, -1, -1))
['f', 'l', 'o', 'g']
