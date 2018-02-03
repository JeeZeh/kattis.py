a,b = list(map(int, input().split(" ")))
if a <= b:
    print("too late")
else:
    rooms = [True] * a
    for x in range(0,b):
        rooms[int(input())-1] = False
    print(rooms.index(True)+1)