#1 Two Sum
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))

#53 Maximum Subarray
def max_subarray(nums):
    a = nums[0]
    b = nums[0]

    for i in range(1, len(nums)):
        a = max(nums[i], a + nums[i])
        b = max(b, a)
    return b

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))

#169. Majority Element
from collections import Counter
def majority_element(nums):
    d1 = dict(Counter(nums))
    n = len(nums)
    for key, val in d1.items():
        if val > (n // 2):
            return key
nums = [2,2,1,1,1,2,2]
print(majority_element(nums))