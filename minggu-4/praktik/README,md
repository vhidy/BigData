# 6. Modules

Pertama buat file fibo.py di folder Python seperti contoh D:\python<br>
di dalam file fibo.py , copy kan code berikut ini:

> `def fib(n):    # write Fibonacci series up to n` <br>
`    a, b = 0, 1` <br>
`    while a < n:` <br>
`        print(a, end=' ')` <br>
`        a, b = b, a+b` <br>
`    print()` <br>
`##` <br>
`def fib2(n):   # return Fibonacci series up to n
`    result = []` <br>
`    a, b = 0, 1` <br>
`    while a < n:` <br>
`        result.append(a)` <br>
`        a, b = b, a+b` <br>
`    return result` <br>

Setelah itu save di D:\python.<br>
Kemudian di Python 3.7.exe jalankan code seperti di bawah: <br>

> `import sys`<br>
`sys.path.append(r'D:\python')`<br>
`import fibo`<br>

maka fibo selesai di import. Kemudian coba fibo tersebut dengan code dibawah : <br>

> `fibo.fib(1000)`<br>

Maka hasilnya seperti di samping : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987


# 6.1 More on Modules

> `import fibo as fib`<br> 
`fib.fib(500)`<br>

Maka hasilnya : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
 
Maksud dari 'as' adalah inisialisasi nama file untuk mempersingkat code. <br>


# 6.2 Standard Modules

> ` import sys`<br>
` sys.ps1`<br>
`'>>> '`<br>
` sys.ps1 = 'C>'`<br>
`C>print('Yeah!')`<br>
`Yeah!`<br>
`C>`<br>

Membuat sebuah perintah menuju directory C. <br>


# 6.3 The dir() Function

> ` a = [1,2,3,4,5]`<br>
` fib = fibo.fib`<br>
` dir()`<br>
`['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'fib', 'fibo', 'sys']`<br>

Fungsi dir adalah fungsi mem-builtin apa saja yang sudah di built. <br>

# 7.1 Fancier Output Formatting
> `year = 2016`<br>
`event = 'Referendum'`<br>
`f'Results of the {year} {event}'`<br>
`Results of the 2016 Referendum'`<br>

Fungsi diatas untuk memanggil variable year dan event tanpa menggunakan print<br>
dipersingkat dengan mengetik fungsi f<br>

# 7.1.1.Formatted String Literals
>` table = {'Sjoerd' : 4127, 'Jack' : 4098, 'Dcab': 7678}`<br>
` for name, phone in table.items():`<br>
`     print(f'{name:10} ==> {phone:10d}')`<br>
`....`<br>
`Sjoerd     ==>       4127`<br>
`Jack       ==>       4098`<br>
`Dcab       ==>       7678`<br>

Perkembangan dari fungsi f atau formatted, fungsi ini bisa berguna juga walaupun dalam bentuk for<br>

# 7.1.2 The String format() Method
> ` print('This {food} is {adjective}.'.format(`<br>
`     food='spam', adjective='absolutely horrible'))`<br>
`This spam is absolutely horrible.`<br>

Maksud dari code diatas merupakan penggunaan formatted di dalam bentuk string <br>

# 7.1.3. Manual String Formatting
> `for x in range(1,11):`<br>
`     print(repr(x).rjust(2),repr(x*x).rjust(3), end=' ')`<br>
`     print(repr(x*x*x).rjust(4))`<br>
`...`<br>
` 1   1    1`<br>
` 2   4    8`<br>
` 3   9   27`<br>
` 4  16   64`<br>
` 5  25  125`<br>
` 6  36  216`<br>
` 7  49  343`<br>
` 8  64  512`<br>
` 9  81  729`<br>
`10 100 1000`<br>

diatas merupakan for dari sebuah range, dan menampilkan sebuah data yang berulang dari perulangan diatas. <br>

# 7.1.4 Old string formatting
> ` import math`<br>
` print('The value of pi is approximately %5.3f.'% math.pi)`<br>
`The value of pi is approximately 3.142.`<br>

fungsi diatas merupakan untuk mengimport sebuah fungsi matematika.

# 7.2 Reading and Writing Files
> ` f = open('workfile','w')`<br>
` with open('workfile') as f:`<br>
`     read_data = f.read()`<br>
` ... `<br>
` f.closed`<br>
`True`<br>

Diatas adalah fungsi membaca dan menutup sebuah file. <br>

# 7.2.1 Methods of File Objects
> ` f = open('workfile','rb+')`<br>
` f.write(b'0123456789abcdef')`<br>
`16`<br>
` f.seek(5)`<br>
`5`<br>
` f.read(1)`<br>
`b'5'`<br>
` f.seek(-3,2)`<br>
`13`<br>
` f.read(1)`<br>
`b'd'`<br>

Ini untuk mengedit sebuah file dengan menggunakan methods. <br>

# 7.2.2. Saving structured data with json
> ` import json`<br>
` json.dumps([1,'simple','list'])`<br>
`'[1, "simple", "list"]'`<br>

fungsi diatas merupakan untuk mengimport sebuah fungsi matematika. <br>

# 8.1. Syntax Errors
> ` while True print('Hello world')`<br>
`  File "<stdin>", line 1`<br>
`    while True print('Hello world')`<br>
`                   ^`<br>
`SyntaxError: invalid syntax`<br>
 
 Diatas merupakan contoh syntax error yang ditampilkan di python.<br>
 
# 8.2 Exceptions
> ` 10 * (1/0)`<br>
`Traceback (most recent call last):`<br>
`  File "<stdin>", line 1, in <module>`<br>
`ZeroDivisionError: division by zero`<br>
` 4 + spam*3`<br>
`Traceback (most recent call last):`<br>
`  File "<stdin>", line 1, in <module>`<br>
`NameError: name 'spam' is not defined`<br>
` '2' + 2`<br>
`Traceback (most recent call last):`<br>
`  File "<stdin>", line 1, in <module>`<br>
`TypeError: can only concatenate str (not "int") to str`<br>

Di ini adalah TypeError exception dari Python.<br>

# 8.3 Handling Exceptions
> ` def this_fails():`<br>
`     x = 1/0`<br>
`....`<br>
` try:`<br>
`     this_fails()`<br>
` except ZeroDivisionError as err:`<br>
`     print('Handling run-time error:', err)`<br>
`....`<br>
`Handling run-time error: division by zero`<br>

Diatas merupakan cara untuk mengatasi error. <br>

# 8.4 Raising Exceptions
> ` try:`<br>
`     raise NameError('HiThere')`<br>
` except NameError:`<br>
`     print('An exception flew by!')`<br>
`     raise`<br>
`...`<br>
`An exception flew by!`<br>
`Traceback (most recent call last):`<br>
`  File "<stdin>", line 2, in <module>`<br>
`NameError: HiThere`<br>

Ini merupakan menunjukan tempat dan nama peringatan dari error tersebut. <br>

# 8.6 Defining Clean-up Actions
> ` try : `<br>
`     raise KeyboardInterrupt`<br>
` finally:`<br>
`     print('Goodbye, world!')`<br>
``<br>
`Goodbye, world!`<br>
`Traceback (most recent call last):`<br>
`  File "<stdin>", line 2, in <module>`<br>
`KeyboardInterrupt`<br>

Fungsi ini adalah ketika penggunaan yang salah dari keyboard. <br>

# 9.2.1 Scopes and Namespaces Example
> ` def scope_test():`<br>
`     def do_local():`<br>
`             spam = "local spam"`<br>
`     def do_nonlocal():`<br>
`             nonlocal spam`<br>
`             spam = "nonlocal spam"`<br>
`     def do_global():`<br>
`             global spam`<br>
`             spam = "global spam"`<br>
`     spam = "test spam"`<br>
`     do_local()`<br>
`     print("After local assigment:", spam)`<br>
`     do_nonlocal()`<br>
`     print("After nonlocal assigment:", spam)`<br>
`     do_global()`<br>
`     print("After global assigment:", spam)`<br>
`  `<br>
` scope_test()`<br>
`After local assigment: test spam`<br>
`After nonlocal assigment: nonlocal spam`<br>
`After global assigment: nonlocal spam`<br>
` print("In global scope:" ,spam)`<br>
`In global scope: global spam`<br>

# 9.3.2. Class Objects
> ` class Complex:`<br>
`     def __init__(self, realpart, imagpart):`<br>
`             self.r = realpart`<br>
`             self.i = imagpart`<br>
`    `<br>
` x = Complex(3.0,-4.5)`<br>
` x.r,x.i`<br>
`(3.0, -4.5)`<br>

# 9.3.3 Instance Objects
> `  x.counter = 1`<br>
`  while x.counter < 10:`<br>
`      x.counter = x.counter * 2`<br>
` `<br>
`  print(x.counter)`<br>
` 16`<br>
`  del x.counter`<br>

# 9.3.5 Class and Instance Variables
>` class Dog:`<br>
`     def __init__(self,name):`<br>
`             self.name = name`<br>
`             self.tricks = []`<br>
`     def add_trick(self,trick):`<br>
`             self.tricks.append(trick)`<br>
`  `<br>
` d = Dog('Fido')`<br>
` e = Dog('Horsea')`<br>
` d.add_trick('roll over')`<br>
` e.add_trick('play dead')`<br>
` d.tricks`<br>
`['roll over']`<br>
` e.tricks`<br>
`['play dead']`<br>

#9.4 Random Remarks
> ` def f1(self, x, y):`<br>
`     return min(x, x+y)`<br>
`...`<br>
` class C:`<br>
`     f = f1`<br>
`     def g(self):`<br>
`             return 'hello world'`<br>
`     h = g`<br>
`...`<br>
`  `<br>

#9.6 Private Variables
> ` class Mapping:`<br>
`     def __init__(self, iterable):`<br>
`             self.items_list = []`<br>
`             self.__update(iterable)`<br>
`     def update(self, iterable):`<br>
`             for item in iterable:`<br>
`                     self.items_list.append(item)`<br>
`     __update = update`<br>
`   `<br>
` class MappingSubclass(Mapping):`<br>
`     def update(self,keys,values):`<br>
`             for item in zip(keys, values):`<br>
`                     self.items_list.append(item)`<br>
`   `<br>

#9.7 Odds and Ends
>` class Employee:`<br>
`     pass`<br>
`  `<br>
` john = Employee()`<br>
` john.name = 'john doe'`<br>
` john.dept = 'computer lab'`<br>
` john.salary = 1000`<br>

#9.8 Iterators
> ` class Reverse:`<br>
`     def __init__(self, data):`<br>
`             self.data = data`<br>
`             self.index = len(data)`<br>
`     def __iter__(self):`<br>
`             return self`<br>
`     def __next__(self):`<br>
`             if self.index == 0:`<br>
`                     raise StopIteration`<br>
`             self.index = self.index - 1`<br>
`             return self.data[self.index]`<br>
``<br>
` rev = Reverse('spam')`<br>
` iter(rev)`<br>
`<__main__.Reverse object at 0x00957910>`<br>
` for char in rev:`<br>
`     print(char)`<br>
` `<br>
`m`<br>
`a`<br>
`p`<br>
`s`<br>

#9.9 Generators
> ` def reverse(data):`<br>
`     for index in range(len(data)-1,-1,-1):`<br>
`             yield data[index]`<br>
`  `<br>
` for char in reverse('golf'):`<br>
`     print(char)`<br>
`  `<br>
`f`<br>
`l`<br>
`o`<br>
`g`<br>

#9.10 Generator Expressions
> ` data = 'golf'`<br>
` list(data[i] for i in range(len(data)-1,-1,-1))`<br>
`['f', 'l', 'o', 'g']`<br>
