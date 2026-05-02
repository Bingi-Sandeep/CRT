
#283 Move Zeroes
def moveZeroes(nums):
    pos = 0
    for i in range(len(nums)):
         if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)

#268 Missing Number
def missingNumber(nums):
    n = len(nums)
    res = (n * (n + 1)) // 2
    return res - sum(nums)

nums = [0,1,2,3,5]
print(missingNumber(nums))