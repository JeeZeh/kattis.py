n = int(input())
opps = ['*', '+', '-', '//']
alt = ['*', '+', '-', '/']
for i in range(0, n):
    solved = False
    ans = int(input())
    opp1, opp2, opp3 = 0, 0, 0
    while not solved:
        if int(eval("4 " + opps[opp1] + " 4 " + opps[opp2] + " 4 " + opps[opp3] + " 4")) == ans:
            out = "4 " + alt[opp1] + " 4 " + alt[opp2] + " 4 " + alt[opp3] + " 4" + " = " + str(ans)
            solved = True
            print(out)
        else:
            opp1 += 1
            if opp1 == 4:
                opp1 = 0
                opp2 += 1
            if opp2 == 4:
                opp2 = 0
                opp3 += 1
            if opp3 == 4:
                opp3 = 0
                print("no solution")
                break
