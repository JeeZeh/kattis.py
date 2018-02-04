a, b, c = list(map(int, input().split(" ")))

def solution(x, y, z):
    outs = ['+', '-', '*', '/', '=']
    ops = ['+', '-', '*', '/', '==']
    for op1 in ops:
        for op2 in ops:
            test = "%d%s%d%s%d" % (x, op1, y, op2, z)
            if eval(test) is True and (op1 == '==' or op2 == '=='):
                return "%d%s%d%s%d" % (x, outs[ops.index(op1)], y, outs[ops.index(op2)], z)
    return 0

print(solution(a, b, c))
