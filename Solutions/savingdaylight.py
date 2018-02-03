import sys

for line in sys.stdin:
    stamp = list(map(str, line.split(" ")))
    T_in, T_out = stamp[3], stamp[4]

    def count(T_in, T_out):
        H_in, M_in = map(int, T_in.split(":"))
        H_out, M_out = map(int, T_out.split(":"))
        hours = 0
        mins = 0
        while H_in != H_out or M_in != M_out:
            M_in += 1
            mins += 1
            if M_in == 60:
                H_in += 1
                M_in = 0
            if mins == 60:
                hours += 1
                mins = 0
            
        return "%d hours %d minutes" % (hours, mins)

    print("%s %s %s %s" % (stamp[0], stamp[1], stamp[2], count(T_in, T_out)))