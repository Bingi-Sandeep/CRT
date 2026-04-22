#Sorted check
def is_sortedArray(nums):
    if len(nums) <= 1:
        return True
    if nums[0] > nums[1]:
        return False
    return is_sortedArray(nums[1:])
print(is_sortedArray([10, 20, 30, 40, 50]))#True
print(is_sortedArray([10, 2, 30, 14, 50]))#False