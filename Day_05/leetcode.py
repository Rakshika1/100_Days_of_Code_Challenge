class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        secondnums = nums
        nums.extend(secondnums)
        return nums


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            p = nums[i]
            if (p<target):
                c = c+1
        return c

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        p = int((num**(1/2)))
    
        t = int(p*p)
        print(t)
        if (t==num):
            return True
        else:
            return False
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if (i==0):
                nums.append(i)
                nums.remove(i)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count =0
        h = len(s)
        k = len(t)
        p = list(s)
        t = list(t)
        for i in p[:]:
            if i in t:
                count = count + 1
                t.remove(i)
                
        if ((count == h) and (count ==k)):
            return True
        else:
            return False