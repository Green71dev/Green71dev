# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 07:33:05 2021

Fibanachi soni
"""
print("Fibanachi sonini hisoblovchi dastur")
x = int(input("qancha takrorlansin? >>>>"))
a, b, s = 1, 0, 0
print("fibonachi ko'einishi: ")
for i in range(x):
    s = s + a
    print("  ", a, "  ")
    a = a + b
    b = a - b
print("Yig'indi = ", s)



