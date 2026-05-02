'''
189. Rotate Array
'''
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(key=lambda x: x*10, reverse=True)
        return str(int(''.join(nums)))
        