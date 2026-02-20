
'''
#Running Sum in List

def runningSum(nums):
    res = []
    c = 0
    for v in nums:
        c += v
        res.append(c)
    return res

nums = [1, 2, 3, 4]
print(runningSum(nums))

ans = []

for i in range(1, len(nums) + 1):
    ans.append(sum(nums[:i]))           #res = [sum(nums[:i]) for i in range(1, len(nums) + 1)]

print(ans)


#Duplicate Values

nums = [1, 2, 3, 4, 2]
print(len(nums) != len(set(nums)))

'''
#Richest Customer Wealth

accounts = [[1, 2, 3],
            [3, 2, 1]]
res = []

for i in range(len(accounts)):
    res.append(sum(accounts[i]))

print(max(res))