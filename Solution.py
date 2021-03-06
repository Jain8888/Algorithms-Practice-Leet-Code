


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
    
    
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s

        # plan - iterate from end to look for first letter, then start count and look for a space 

        # case when inout is all spaces
        if s.count(' ') == len(s):
            output = 0
            return output

        elif s != '':
            # iterate to get index of first letter from the end
            index_of_first_letter = 1
            for i in range(1,len(s)+1):
                i = -(i)
                letter = s[i]
                if letter != ' ':
                    index_of_first_letter = i

                    count = 0
                    for j in range(-index_of_first_letter,len(s)+1):
                        j = -(j)
                        letter = s[j]
                        if letter == ' ':
                            break
                        else:
                            count += 1
                    output = count
                    return count
                    break


                   
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # sum =  1 + (n-1)C1 + (n-2)C2 + .....
        
        def factorial(x):
            fact = 1
            for i in range(1,x+1):
                fact = fact * i
            return fact

        def combination(n,r):
            out = factorial(n)/(factorial(r)*(factorial(n-r)))
            return out

        self.n = n
        r = 0
        sum = 0
        while n >= r:
            sum = sum + combination(n,r)
            n = n-1
            r = r+1
        return sum
    
    
    def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums.sort()
    sumsi = 0
    for i in range(int(len(nums)/2)):

            sums = min(nums[i],nums[i+1])
            sumsi = sumsi + sums
            del nums[i+1]

    return sumsi


    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        self.digits = digits
        
        # case when all is 9
        if digits.count(9) == len(digits):
            out = [1]
            for i in range(len(digits)):
                out.append(0)
            return out
        else:
            last_digit = digits[-1]
            i = -1
            while last_digit == 9:
                digits[i] = 0
                last_digit = digits[i-1]
                i = i-1

            digits[i] = digits[i] + 1
            return digits
        
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        self.num = num

        div = [0]

        if num%2 == 0 and str(num)[-1] != '0':
            for i in range(1,int(round(num/2))+1):
                if num%i == 0:
                    div[0] = div[0] + i
                    if div[0] > num:
                        break

            if div[0] == num:
                out = True
            else:
                out = False
        else:
            out=False

        return out     
    
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        
        for i in nums:
            if nums.count(i) == 1:
                return i
            
            
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
   
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def recurse(node):
            if node == None:
                return (0,True)
            
            else:
                left_height, left_balance = recurse(node.left)
                right_height, right_balance = recurse(node.right)
                
                node_height = 1 + max(left_height, right_height)
                if abs(left_height-right_height) <= 1 and left_balance and right_balance:
                    node_balance = True
                else:
                    node_balance = False
            
                return node_height, node_balance
        
        return recurse(self.root)[1]  
    
    
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def helper(node_1,node_2):
            if node_1 == None and node_2 == None:
                return True

            
            if (node_1 and node_2) and node_1.val == node_2.val:
                left_check = helper(node_1.left,node_2.left)
                right_check = helper(node_1.right, node_2.right)
            
                return left_check and right_check
            else:
                return False
        return helper(p,q)
    
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(node):
            height = 0

            if node == None:
                return height
            
            elif node != None:
                left_h = helper(node.left) + 1
                right_h = helper(node.right) + 1
                height = max(left_h,right_h)
                return height

        return helper(root)
    
    
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        self.numRows = numRows
        
        out = [[1]]
        for j in range(numRows-1):
            trial = [1]
            num_elements = len(out[-1])+1
            elem = out[-1]
            for i in range(num_elements-2):
                new = elem[i] + elem[i+1]
                trial.append(new)
            trial.append(1)
            out.append(trial)
        return out
    
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        
        nums.sort()
            
        return nums[len(nums)/2]
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        self.targetSum = targetSum
        # add until both child are null
        def helper(node):
            if node:
                if node.left == None and node.right == None:
                    return node.val

                if node.left:
                    node.left.val = node.left.val + node.val
                    check = helper(node.left)
                    if check == targetSum:
                        return check
                    
                if node.right:
                    node.right.val = node.right.val + node.val
                    check_1 = helper(node.right)
                    if check_1 == targetSum:
                        return check_1  
            else:
                b = 1.5
                return b
        trial = helper(root)
        if trial == targetSum:
            return True
        else:
            return False
        
        
    def romanToInt(self, s: str) -> int:
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        # problematic items - IV IX XL XC CD CM
        prob_items_dict = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}

        s_copy = s
        sum= 0
        for key,value in prob_items_dict.items():
            if key in s_copy:
                s_copy = s_copy.replace(key,'') 
                sum += value
        for key in s_copy:
                sum += roman_dict.get(key)
        
        return sum
