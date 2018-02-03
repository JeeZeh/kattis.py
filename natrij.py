a, b, c = list(map(int, input().split(":"))) # Beginning Time
x, y, z = list(map(int, input().split(":"))) # End Time

f, g, h = 0, 0, 0 # Time Counter


while a != x or b !=y or c!=z: # Increment begin time until = end time while counting
    c += 1
    h += 1
    if c==60:
        c = 0
        b += 1
    if h == 60:
        h = 0
        g += 1

    if b == 60:
        b = 0
        a += 1
    if g == 60:
        g = 0
        f += 1

    if a == 24:
        a = 0

if f == 0 and g == 0 and h == 0: # If the times are the same, assume 24 hours have passed
    f = 24

print("%02d:%02d:%02d" % (f, g, h)) # Print the difference, formatted as xx:xx:xx
