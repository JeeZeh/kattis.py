n = int(input())
names = []

for count in range(0, n):
    names.append(input())

if sorted(names) == names:
    print("INCREASING")
elif names == sorted(names)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")