# # FINDING WORDS CONTAINING CHARACETER:
# class Solution:
#     def findWordsContaining(self, words: List[str], x: str) -> List[int]:
#         result = []
#         a = len(words)
#         for i in range(a):
#             if x in words[i]:
#                 result.append(i)
#         return result
    

# # Richest Customer Wealth
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         maximum = 0;
#         for i in accounts:
#             w = sum(i)
#             maximum = max(maximum,w)
#         return maximum
# # kids-with-the-greatest-number-of-candies
# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         list1 = []
#         maxCandies = max(candies)
#         # print(maxCandies)
#         for i in range(len(candies)):
#             sum1 = extraCandies + candies[i]
#             # print(sum1)
#             if sum1>=maxCandies:
#                 # print(True)
#                 list1.append(True)
#             else:
#                 # print(False)
#                 list1.append(False)
#         return list1   
    
# # count-pairs-whose-sum-is-less-than-target
# class Solution:
#     def countPairs(self, nums: List[int], target: int) -> int:
#         sum1 = 0
#         d = len(nums)
#         for i in range(d):
#             for j in range(i+1,d):
#                 if ((nums[i] + nums[j]) < target):
#                     print(nums[i],nums[j])
#                     sum1 = sum1 +1
            
#         return sum1
                    

# # Two Sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         list = []
#         d = len(nums)
#         for i in range(d-1):
#             for j in range(i+1,d):
#                 if (nums[i] + nums[j]==target):
#                     list.append(i)
#                     list.append(j)
#         return list
# # Palindrom

                


            