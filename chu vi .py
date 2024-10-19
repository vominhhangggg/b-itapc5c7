# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 13:21:48 2024

@author: ADMIN
"""
import math 
def chu_vi(hinh, *args, **kwargs):
    if hinh == "vuong":
        canh = args[0]
        return 4 * canh
    elif hinh == "chunhat":
        dai = args[0]
        rong = args[1]
        return 2 * (dai + rong)
    elif hinh == "hinhtron":
        ban_kinh = args[0]
        return 2 * math.pi * ban_kinh
    else:
        return"Hình không hợp lệ"
        
if __name__=="__main__":
    print("Chu vi hình vuông: ", chu_vi('vuong',5))
    print("Chu vi hình chữ nhật: ", chu_vi('chunhat',7,8))
    print("Chu vi hình tròn: ", chu_vi('hinhtron',2))
    