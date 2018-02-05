n = int(input())

for i in range(0, n):
    in1 = list(input())
    in2 = list(input())
    out = []
    for j in range(0, len(in1)):
        if in1[j] == in2[j]:
            out.append('.')
        else:
            out.append('*')

    print(''.join(in1))
    print(''.join(in2))
    print(''.join(out))
    print()
