l = int(input())
d = int(input())
x = int(input())

lowest  = l
set = False
highest = -1
n = l

while(n <= d):
    total = 0
    temp = n
    while(temp > 0):
        total += temp % 10
        temp = temp//10
    if total == x:
        if not set:
            lowest = n
            set = True
        highest = n
    n += 1

print(lowest)
print(highest)
