scores = []
biggest = 0
index = 0
for i in range(0, 5):
    points = eval(input().replace(" ", "+"))
    scores.append(points)
    if points > biggest:
        biggest  = points
        index = i

print("%d %d" % (index+1, biggest))