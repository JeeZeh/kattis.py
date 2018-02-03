monthly = int(input())
months = int(input())
total = 0

for i in range(0, months):
    total += int(input())

print((monthly*(months+1)) - total)
