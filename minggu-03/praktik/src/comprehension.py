#!/usr/bin/python3.7

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# atau

squares = [x**2 for x in range(10)]
print(squares)

list_dengan if = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(list_dengan_if)

list_dengan_if = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            list_dengan_if.append((x, y))

print(list_dengan_if)

from math import pi
list_math = [str(round(pi, i)) for i in range(1, 6)]
