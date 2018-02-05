string = input()
vowels = ['a', 'e', 'i', 'o', 'u']
out = []

skip = 0
for letter in string:
    if letter == ' ':
        skip = 0
        out.append(letter)
    elif skip != 0:
        skip -= 1
    elif letter in vowels:
        out.append(letter)
        skip = 2
    elif skip == 0:
        out.append(letter)

print(''.join(out))
