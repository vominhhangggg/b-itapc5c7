# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:32:59 2024

@author: ADMIN
"""

import random
phantu = random.randint(20, 30)

giatribinhphuong = [random.uniform(18, 99) ** 2 for _ in range(phantu)]

print(f"Số lượng phần tử: {phantu}")
print("Các giá trị bình phương:", giatribinhphuong)