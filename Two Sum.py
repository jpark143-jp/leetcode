"""Solution 1"""
class Solution:
    def twoSum(self, nums, target) :
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

"""Solution 2"""
class Solution:
    def twoSum(self, nums, target) :
        complementMap = dict()
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[complement] = i

"""S=Solution()
   S.twoSum([2,7,11,15], 9)"""

