word = input()
last = ""
out =  ""
for l in word:
    if(l != last):
        out += l
        last = l
print(out)