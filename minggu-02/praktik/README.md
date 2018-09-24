## 2.1 Invoking the Interpreter
> `Python 3.7.0`
Ini menandakan bahwa Python yang digunakan merupakan python 3.7

## 2.1.2 Interactive Mode 
> `the_world_is_flat = True`<br>
`if the_world_is_flat:`<br>
`...     print("Be careful not to fall off!")`<br>
`... `<br>
`Be careful not to fall off!`

Ini menggunakan if ... jadi jika variable tersebut true, maka if tersebut akan bernilai true

## 3.1.1. Number
> `50 - 5*6`<br>
`20`<br>
`(50 - 5*6) / 4`<br>
`5.0`<br>
`8 / 5`<br>
`1.6`<br>
`8 // 5`<br>
`1` --Operasi ini adalah menghilangkan bagian belakang koma<br>

Ada berbagai jenis perhitungan number, salah satunya seerti diatas. <br>
Perhitungan ini seperti perhitungan yang ada pada kalkulator umum. <br>
Ini adalah operansi perhitungan yang biasa terjadi di sebuah program dasar ataupun menengah.

## 3.1.2. Strings
> `text = "She really doesn't come to here"`<br>
`text` --Ini memanggil variable text, bisa tanpa menggunakan perintah print<br>
`"She really doesn't come to here"`<br>
`text[5]`<br>
`'e'`<br>
`len(text)`<br>
`31`<br>

Ini adalah operasi String, cara memanggil text string, ini dasar yang musti diketahui untuk memenggunakan string.<br> 
Ada penggunaan array dan ada juga penggunaan len(), itu dimaksudkan untuk menghitung panjangnya karakter yang diinputkan<br>

## 3.1.3. List
> `squares = [1,3,5,7,9]`<br>
`squares`<br>
`[1, 3, 5, 7, 9]`<br>
`squares[:]`<br>
`[1, 3, 5, 7, 9]`<br>
`4 ** 3`<br>
`64`<br>
`squares[3] = 64`<br>
`squares`<br>
`[1, 3, 5, 64, 9]`<br>
`squares(11)`<br>
`squares.append(11)`<br>
`squares`<br>
`[1, 3, 5, 64, 9, 11]`<br>

Kali ini, cara membuat list pada Python, hampir sama pada umumnya tapi ciri khas dari Python tidak memiliki tag-tag seperti di php, <br>
contoh ' ; ',' $ ', etc<br>
Ada fungsi membuat array list, mengubah, menambahkan bahkan mengedit array list itu sendiri. <br>

## 4.1. if Statements
>`x = int(input("please enter an integer: "))`<br>
`please enter an integer: 28`<br>
`if x<0:`<br>
`     x=0`<br>
`     print('negative change to zero')`<br>
` elif x == 1:`<br>
`     print('single')`<br>
` else:`<br>
`     print('more')`<br>
`...`<br>
`more`<br>

Untuk if statements, hampir sama diseluruh bahasa pemograman. if true maka melakukan yang true jika false, maka ia melakukan perintah false.<br>

## 4.2 for statements
>` words = ['cat','window','defenestrate']`<br>
` for w in words:`<br>
`     print(w, len(w))`<br>
`...`<br>
`cat 3`<br>
`window 6`<br>
`defenestrate 12`<br>

Sama seperti if, for statements juga sama dengan bahasa pemograman yang lain. Perulangan data yang sudah di inputkan.<br>

## 4.3 range()
>` a = ['mary','had','a','little','lamb']`<br>
` for i in range(len(a)):`<br>
`     print(i,a[i])`<br>
`...`<br>
`0 mary`<br>
`1 had`<br>
`2 a`<br>
`3 little`<br>
`4 lamb`<br>

Ini operan menghitung berapa jarak dari angka pertama dan kedua, contoh range(5,10) maka 5,6,7,8,9<br>

## 4.4. break and continue Statements, and else Clauses on Loops
>` for n in range(2,10):`<br>
`     for x in range(2,n):`<br>
`             if n % x == 0:`<br>
`                     print(n, 'equals', x, ' * ', n//x)`<br>
`                     break`<br>
`             else:`<br>
`                     print(n, ' is a prime number')`<br>
`...`<br>
`3  is a prime number`<br>
`4 equals 2  *  2`<br>
`5  is a prime number`<br>
`5  is a prime number`<br>
`5  is a prime number`<br>
`6 equals 2  *  3`<br>
`7  is a prime number`<br>
`7  is a prime number`<br>
`7  is a prime number`<br>
`7  is a prime number`<br>
`7  is a prime number`<br>
`8 equals 2  *  4`<br>
`9  is a prime number`<br>
`9 equals 3  *  3`<br>

operasi break and continue bertujuan untuk jika ternyata for yang digunakan tepat maka ia akan berhenti, penggunaan break <br>
kalau ingin melanjutkan berarti countinue <br>

## 4.5 pass Statements
>`def initlog(*args):`<br>
`      pass`<br>
`...`<br>

Ini bertujuan statement itu tidak melakukan apapun. jika dia dipanggil maka maka langsung pass.<br>

## 4.6 Defining Functions
>` def fib(n):`<br>
`     a, b = 0, 1`<br>
`     while a < n:`<br>
`             print(a,end='  ')`<br>
`             a, b = b, a+b`<br>
`     print()`<br>
` ...`<br>
` fib(2000)`<br>
` 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377  610  987  1597`<br>

Mendefinisikan fungsi yang dipanggil seperti private ataupun public di JAVA.<br>
