words = list(map(str, input().split(" ")))
size = len(words)-1
dupe = False
for i in range(0, size):
    word = words[i]
    words[i] = ""
    if word in words:
        dupe = True
        break

if dupe:
    print("no")
else:
    print("yes")