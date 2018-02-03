n = int(input())

for i in range(0, n):
    line = input()
    if line == "P=NP":
        print("skipped")
    else:
        print(eval(line))