#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import winsound
from datetime import datetime

# Versiyon 3

file = open("zaman.txt", 'r')
sure = file.readline()
file.close()

# Ses kontrol
winsound.Beep(3000, 100)
winsound.Beep(2500, 100)
winsound.Beep(2000, 100)
winsound.Beep(1000, 100)
winsound.Beep(500, 100)

oncekiZaman = datetime.now()
print(oncekiZaman)
print(sure)
time.sleep(int(sure))
simdiZaman = datetime.now()
print(simdiZaman)
farkZaman = simdiZaman - oncekiZaman
print(farkZaman)

# Ses kontrol
winsound.Beep(3000, 100)
winsound.Beep(2500, 100)
winsound.Beep(2000, 100)
winsound.Beep(1000, 100)
winsound.Beep(500, 100)



# Versiyon 2

# import time
# import winsound
# from datetime import datetime

# Ses kontrol
# winsound.Beep(3000, 100)
# winsound.Beep(2500, 100)
# winsound.Beep(2000, 100)
# winsound.Beep(1000, 100)
# winsound.Beep(500, 100)
#
# oncekiZaman = datetime.now()
# print(oncekiZaman)
# time.sleep(60 * 60)
# simdiZaman = datetime.now()
# print(simdiZaman)
# farkZaman = simdiZaman - oncekiZaman
# print(farkZaman)
# Ses kontrol
# winsound.Beep(3000, 100)
# winsound.Beep(2500, 100)
# winsound.Beep(2000, 100)
# winsound.Beep(1000, 100)
# winsound.Beep(500, 100)


# Versiyon 1

# import time
# import winsound
# from datetime import datetime

# simdiZaman = datetime.now()
# print(simdiZaman)
#
# time.sleep(1)
#
# sonraZaman = datetime.today()
#
# print(sonraZaman)
#
# farkZaman = sonraZaman - simdiZaman
#
# print(farkZaman)
# print(farkZaman.days)
# print(farkZaman.total_seconds())
# print(farkZaman.seconds)
# print(farkZaman.microseconds)
#
# if farkZaman.total_seconds() > (1 * 60) :
#     print("Büyük")
# else:
#     print("Küçüktür")
#
# while farkZaman.total_seconds() < (1 * 60) :
#     time.sleep(1)
#     sonraZaman = datetime.today()
#     print(sonraZaman)
#     farkZaman = sonraZaman - simdiZaman
#     print(farkZaman)
