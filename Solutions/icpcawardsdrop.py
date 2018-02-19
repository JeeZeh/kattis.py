winners = []
universities = []
for i in range(0, int(input())):
    a, b = list(map(str, input().split(" ")))

    if not a in universities:
        winners.append(a + " " + b)
        universities.append(a)

for i in range(0, 12):
    print(winners[i])
