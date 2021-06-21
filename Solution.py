


class Solution(object):
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.
        
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        self.nums = nums
        self.target = target
        
        
        for j in range(len(nums)):
            for i in range(len(nums)):
                if i != j:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        output = [i,j]
                        return output
                    else:
                        continue
                else: 
                    continue
