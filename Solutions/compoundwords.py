import re
words = []
comps = []
while True:
    try:
        line = re.split('\W', input())
        for word in line:
            words.append(word)
    except EOFError:
        for i in range(0, len(words)):
            for j in range(0, len(words)):
                comp = words[i] + words[j]
                if (words[j] != words[i] and not (comp in comps)):
                    comps.append(words[i] + words[j])
        break

comps.sort()

for comp in comps:
    print(comp)
