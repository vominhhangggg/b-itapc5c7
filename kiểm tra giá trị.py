# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:34:37 2024

@author: ADMIN
"""

n = int(input("Nhập số vào từ [-99;99]: "))
while n < -99 or n > 99:
    n = int(input("Nhập lại n, n chỉ được từ [-99;99]: "))
print(n)