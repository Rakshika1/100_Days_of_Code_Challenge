class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count =0
        for i in nums[:]:
            p = min(nums)
            if (p<k):
                count = count+1
                nums.remove(p)
                # print(nums)
        return count            

        

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        p = min(nums)
        # print(p)
        arr = []
        while nums:
            a = min(nums)
            nums.remove(a)
            b = min(nums)
            nums.remove(b)
            arr.append(b)
            arr.append(a)
        return arr
