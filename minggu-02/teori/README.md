# Belajar Python
## Bab 2. Menggunakan Interpreter Python
#### Pada bagian ini merupakan lokasi Python berada
    C:\Users\Bajingan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7
Karna saya menggunakan windows pada saat penginstalan dan di seting ke tempat penyimpanan tersebut

#### perintah di bawah ini merupakan langkah untuk menjalankan python
    python3.7
#### python dapat dilihat di cmd jika berjalan maka  muncul seperti ini jika menuliskan perintah di “Python3.7”
    Microsoft Windows [Version 10.0.16299.431]
    (c) 2017 Microsoft Corporation. All rights reserved.

    C:\Users\Bajingan>python
    Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
## Bab 3. Pengenalan Informal terhadap Python
### 3.1. Menggunakan Python sebagai Kalkulator
#### 3.1.1. Angka
##### contoh penulisan perintah seperti di bawah ini sebagai kalkulator dengan tipe angka
    >>> 2 + 2
    4
    >>> 50 - 5*6
    20
    >>> (50 - 5*6) / 4
    5.0
    >>> 8 / 5  # division always returns a floating point number
    1.6
    
#### 3.1.2. String
##### Python juga dapat memanipulasi string
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

#### 3.1.3. Daftar
##### contoh  penulisan agar Python mengetahui sejumlah tipe data majemuk yang digunakan untuk mengelompokkan nilai-nilai lainnya
yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku.

    >>> squares = [1, 4, 9, 16, 25]
    >>> squares
    [1, 4, 9, 16, 25]
    squares = [1, 4, 9, 16, 25]
    squares
    contoh data string  seperti ini
    >>> squares[0]  # indexing returns the item
    1
    >>> squares[-1]
    25
    >>> squares[-3:]  # slicing returns a new list
    [9, 16, 25]
    squares[0]  # indexing returns the item

    squares[-1]

    squares[-3:]  # slicing returns a new list
    
### 3.2. Langkah Pertama Menuju Pemrograman
Contoh penulisan sub-urutan awal deret Fibonacci sebagai berikut:

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
    # Fibonacci series:
    # the sum of two elements defines the next
    a, b = 0, 1
    while a < 10:
        print(a)
        a, b = b, a+b

## Bab 4. Alat Kontrol Aliran Lainnya
Selain whilepernyataan yang baru saja diperkenalkan, Python mengetahui pernyataan aliran kontrol yang biasa dikenal dari bahasa lain, dengan beberapa tikungan.

### contoh statement dengan tipe IF
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
    x = int(input("Please enter an integer: "))

    if x < 0:
        x = 0
        print('Negative changed to zero')
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')

### contoh statement dengan tipe FOR
    >>> # Measure some strings:
    ... words = ['cat', 'window', 'defenestrate']
    >>> for w in words:
    ...     print(w, len(w))
    ...
    cat 3
    window 6
    defenestrate 12
    # Measure some strings:
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))

### contoh penulisan fungsi the range()
Fungsi ini untuk mengurutkan angka

    >>> for i in range(5):
    ...     print(i)
    ...
    0
    1
    2
    3
    4
    for i in range(5):
        print(i)
