nums = list(input().split(" "))
abc = ['A', 'B', 'C']
nums.sort()
reqs = list(input())
out = []
for req in reqs:
    out.append(int(nums[abc.index(req)]))

print("%d %d %d" % (out[0], out[1], out[2]))