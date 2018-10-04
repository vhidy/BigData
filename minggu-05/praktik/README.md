10.1. Antarmuka Sistem Operasi

The osmodul menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi:

>>>
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python37'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0

Built-in dir()dan help()fungsi berguna sebagai bantuan interaktif untuk bekerja dengan modul besar seperti os:

>>>
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>

Untuk tugas-tugas harian dan manajemen direktori, shutilmodul ini menyediakan antarmuka tingkat yang lebih tinggi yang lebih mudah digunakan:

>>>
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'

10.2. File Wildcard 


The globmodul menyediakan fungsi untuk membuat daftar file dari pencarian direktori wildcard:


>>>
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
