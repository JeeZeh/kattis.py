m, n, r = list(map(int, (input().split(" "))))
out = ""

for i in range(1,r+1):
    out = ""
    if(i % m == 0):
        out += "Fizz"
    if(i % n == 0):
        out += "Buzz"
    if(len(out) == 0):
        print(i)
    else:
        print(out)
