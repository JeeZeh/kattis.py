n = int(input())
cost = 0
prices = []
for x in range(0,n):
    prices.append(int(input()))

prices.sort()
prices.reverse()

count = 1

for x in range(0,n):
    if count%3 != 0:
        cost += prices[x]
    count += 1

print(cost)
