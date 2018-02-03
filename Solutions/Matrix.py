import string
import random
import time
out = []
chars = '!£€*%-<>.&,#@?'

t = True

for i in range(0, 50000):
    for i in range(0, 75):
        out.append(random.choice(chars))
    print(*out)
    time.sleep(.04)
    del out[:]