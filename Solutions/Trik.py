a = input()
pos = [1,0,0]
for l in a:
    if(l == 'A'):
        pos[0], pos[1] = pos[1], pos[0]
    elif(l == 'B'):
        pos[1], pos[2] = pos[2], pos[1]
    elif(l == 'C'):
        pos[0], pos[2] = pos[2], pos[0]
print()
print(pos.index(1)+1)