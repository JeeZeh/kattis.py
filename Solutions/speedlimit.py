x = 0
y = 0
cont = True
while cont:
    y = 0
    dist = 0
    n = int(input())
    if n == -1:
        cont = False
    else:
        for i in range(0, n):
            a, b = list(map(int, input().split(" ")))
            b = b - y
            y = b + y
            dist += a * b
        print("%d miles" % dist)

