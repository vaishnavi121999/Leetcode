# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] == nums[j]:
#                     return True
#         return False


# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for i in nums:
#             if i in seen:
#                 return True
#             seen.add(i)
#         return False
    
# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         nums.sort()
#         n = len(nums)
#         for i in range(n - 1):
#             if nums[i] == nums[i + 1]:
#                 return True
#         return False
    
#BRILLIANT SOLUTION
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(numSet) != len(nums):
            return True
        return False
        
solution =  Solution()
result = solution.containsDuplicate([1,2,3,1])
print(result)
