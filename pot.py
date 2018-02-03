n = int(input())
out = 0
for i in range(0, n):
    s = int(input())
    p = s % 10
    out += pow(int(s/10), p)

