line = list(input())
out = list()
for letter in line:
    if letter == '<':
        out.pop()
    else:
        out.append(letter)
print(''.join(out))
