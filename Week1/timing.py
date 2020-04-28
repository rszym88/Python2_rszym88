# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

def delay(interval):
    time.sleep(interval / 1000)
    

delay(1500)
print("Hello World")


x = 0

while x <= 10:
    delay(1500)
    print("Going Up .1")
    x = x + 1
    print("......x = ", x)
    
print("done")

print()
print("Descent & Reverse Motor Direction")

while x > 0 and x <= 11:
    delay(1500)
    print("Going down .1")
    x = x - 1
    print("......x = .", x)