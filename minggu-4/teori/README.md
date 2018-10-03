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
