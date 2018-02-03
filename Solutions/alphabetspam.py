word = input()
size = len(word)
letters = list(word)
upper = 0
lower = 0
space = 0
symbol = 0

for letter in letters:
    if letter.isalpha():
        if letter.isupper():
            upper += 1
        else:
            lower += 1
    elif letter == "_":
        space += 1
    else:
        symbol += 1

print(space/size)
print(lower/size)
print(upper/size)
print(symbol/size)
