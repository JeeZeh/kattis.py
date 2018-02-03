n = int(input())

for i in range(0, n):
    m = input()
    if m[:10] == "Simon says":
        print(m[11:])
