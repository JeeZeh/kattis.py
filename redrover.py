directions = input()
complete = False
length = len(directions)
best_saved = 0
best_count = 0
best_sub = ""
start = 0
end = int(length / 2) - 1

while end >= 0:
    nend = end
    while nend < length:
        sub = directions[start:nend]
        sub_len = len(sub)
        count = directions.count(sub)
        saved = count * sub_len - (count + sub_len)
        if (saved > best_saved):
            best_sub = sub
            best_saved = saved
            best_count = count
        start+= 1
        nend+=1
    end-= 1
    start = 0

print(length - best_saved)
