a,b = list(map(int, input().split(" ")))
b -= 45
if b < 0:
    a -= 1
    if a < 0:
        a = 24 + a
    b = 60 + b

print("%s %s" % (a,b))