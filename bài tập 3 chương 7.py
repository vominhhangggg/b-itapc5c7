# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 15:48:06 2024

@author: ADMIN
"""
#Bai 3 - slide trang 60
#1
import random
def tao_seqA():
    n = random.randint(30,80)
    seqA = []
    for i in range(n+1):
        if random.randint(0,1) == 0:
            seqA.append(round(random.uniform(-79,39),2))
        else:
            seqA.append(random.randint(-79,39))
    return seqA

#2
def ktra_dulieu(seqA):
    return[type(i).__name__ for i in seqA ]

#3
def thongke(seqA):
    return len(seqA)

#4
def sapxep(seqA):
    return sorted(seqA)

#5 
def trungbinh_seqA(seqA):
    return max(seqA) - min(seqA)

#6
def gia_tri_trung_binh_giua(seqB):
    N = len(seqB)
    if N % 2 == 0:
        return (seqB[N//2 - 1] + seqB[N//2])/2
    else:
        return seqB[N//2]

#7
def khoangcach(seq):
    return max(seq) - min(seq)

#8 
def sosanhtrungbinh(seqA, seqB):
    return (trungbinh_seqA(seqA), gia_tri_trung_binh_giua(seqB), trungbinh_seqA(seqA) == gia_tri_trung_binh_giua(seqB))

    
if __name__=="__main__":
    seqA=tao_seqA()
    print(seqA)
    print(ktra_dulieu(seqA))
    print(thongke(seqA))
    seqB = sapxep(seqA)
    print(seqB)
    print(trungbinh_seqA(seqA))
    print(khoangcach(seqA))
    print(khoangcach(seqB))
    sosanhAB = sosanhtrungbinh(seqA, seqB)
    print(sosanhAB)

    