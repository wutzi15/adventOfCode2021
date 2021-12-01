import numpy as np

prev = None
bigger = 0
nums = []
with open("input.txt", "r") as f:
    for line in f:
        if prev is not None:
            if int(line) > prev:
                bigger += 1
        prev = int(line)
        nums.append(int(line))
print(bigger)

# Part 2
sums = []
# A bit more elegant, but found online
#sums = np.convolve(nums,np.ones(3,dtype=int),'valid')
for i in range(len(nums)-2):
    tmp = nums[i] + nums[i+1] + nums[i+2]
    sums.append(tmp)

bigger_sums = 0
for i in range(len(sums) -1 ):
    if sums[i+1] > sums[i]:
        bigger_sums += 1
print(bigger_sums)
