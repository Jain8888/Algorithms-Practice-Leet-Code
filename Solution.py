


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
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        self.n = n

        track_list = []
        while True:
            # obtain a list of square elements
            n_str = str(n)
            n_list = []
            for i in range(len(n_str)):
               n_int = int(n_str[i])
               n_int_sq = n_int**2
               n_list.append(n_int_sq)

            # add squared elements
            add = sum(n_list)
            track_list.append(add)

            if add == 1:
                output = True
                return output
            else:
                for elem in track_list:
                    if track_list.count(elem) > 1:
                        output = False
                        return output

            # update n
            n = add
            
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        self.strs = strs

        # cases
        if strs == []:
            output = ''
            return output
        elif len(strs) == 1:
            output = strs[0]
            return output
        else:
            word = strs[0]
            common = []
            for i in range(len(strs)-1):
                out = []
                for letter in range(len(word)):
                    string = strs[i+1]
                    if len(string) > letter:
                        if word[letter] == string[letter]:
                            out.append(word[letter])
                        else:
                            break
                    else:
                        continue
                common_join = ''.join(out)
                common.append(common_join)

            length_letters = []
            for letters in common:
                length_letters.append(len(letters))
            index_min = length_letters.index(min(length_letters))
            output = common[index_min]
            return output


    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        self.s = s

        output = -1
        for i in s:
            count = s.count(i)
            if count == 1:
                output = i
                break

        if output != -1:
            output = s.index(output)
        return output

                   
