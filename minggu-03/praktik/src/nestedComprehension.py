#!/usr/bin/python3.7
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

ubah_urutan_matrix = [[row[i] for row in matrix] for i in range(4)]
print(ubah_urutan_matrix)

matrix_dengan_zip = list(zip(*matrix))
print(matrix_dengan_zip)
