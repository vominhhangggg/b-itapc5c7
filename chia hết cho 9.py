# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:46:39 2024

@author: ADMIN
"""

dssochan = [i for i in range(2020, 3839) if i % 2 == 0]

chiahet9 = [i for i in dssochan if i % 9 == 0]

print("\t".join(map(str, chiahet9)))