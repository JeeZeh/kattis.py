import sys
mydict = {}
for line in sys.stdin:
    if line.strip() == "":
        break
    else:
        a, b = list(map(str, line.strip().split(" ")))
        mydict[b] = a
for line in sys.stdin:
    if line.strip() in mydict:
        print(mydict[line.strip()])
    else:
        print("eh")

