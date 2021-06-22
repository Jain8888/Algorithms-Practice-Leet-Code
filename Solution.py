


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
                    
                    
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
                    
        self.x = x
        
        if x>=0:
            # convert to string to access elements
            x_str = str(x)
            reverse_str = x_str[::-1]
            reverse_x = int(reverse_str)
            if x == reverse_x:
                output = True
                return output
            else:
                output = False
                return output
        else:
            output = False
            return output
                
