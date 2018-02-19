for i in range(0, int(input())):
    categories = {}
    combinations = 1
    for j in range(0, int(input())):
        item, attrib = list(map(str, input().split(" ")))

        if not attrib in categories:
            categories[attrib] = 2
        else:
            categories[attrib] = categories.get(attrib) + 1

    loop = 0
    for j in categories:
        mulp = 1
        sum = 0
        count = 0
        combinations *= categories.get(j)
    print(combinations-1)




