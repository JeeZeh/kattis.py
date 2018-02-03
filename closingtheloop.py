n = int(input())
for i in range(0, n):
    blue = []
    red = []
    num_pieces = int(input())
    pieces = list(map(str, input().split(" ")))
    for piece in pieces:
        if 'R' in piece:
            red.append(int(piece[:-1]))
        elif 'B' in piece:
            blue.append(int(piece[:-1]))
    blue = sorted(blue)
    red = sorted(red)
    length = 0
    last = ""
    first = ""
    for x in range(0, num_pieces):
        top_blue = 0
        top_red = 0
        if ((last == "red" or first == "red") and len(blue) == 0)\
                or ((last == "blue" or first == "blue") and len(red) == 0) \
                or (last == "" and (len(blue) == 0 or len(red) == 0)):
            break
        if len(blue) != 0:
            top_blue = blue.pop()
        if len(red) != 0:
            top_red = red.pop()
        if last == "red" or x ==0:
            if x == 0:
                first = "blue"
            last = "blue"
            if top_red > 0:
                red.append(top_red)
            length += top_blue -1
        else:
            if x == 0:
                first = "red"
            last = "red"
            if top_blue > 0:
                blue.append(top_blue)
            length += top_red-1
    print("Case #%d: %d" % (i+1, length))
