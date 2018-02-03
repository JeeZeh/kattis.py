m = int(input())

for i in range(0, m):
    n = int(input())
    if abs(n)%2 != 0:
        print("%d is odd" % n)
    else:
        print("%d is even" % n)