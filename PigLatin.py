import sys
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
line_out = ""

for line in sys.stdin:
    line_out = ""
    words = list(map(str, line.lower().strip().split(" ")))
    count = 0
    for word in words:
        count += 1
        if count > 1:
            line_out += " "
        letters = list(word)
        for letter in letters:
            ind = letters.index(letter)
            if (letter in vowels) and ind == 0:
                word += "yay"
                line_out += word
                break
            elif (letter in vowels):
                word = word[ind:] + word[:ind] + "ay"
                line_out += word
                break

    print(line_out)
