# class Solution:
#     def isPalindrome(self, x:int) -> bool:
#         string_num = str(x)
#         return string_num == string_num[::-1]
    
# solution = Solution() #Creating an instance of the class solution
# result = solution.isPalindrome(121)
# print(result)

# result = solution.isPalindrome(-121)
# print(result)

class Solution:
    def isPalindrome(self, x:int) -> bool:
        n = x
        rev = 0
        if x < 0:
            return False
        while x > 0:
            rev = (rev * 10) + (x % 10)
            x //= 10
        if rev == n:
            return True
        return False 
    
solution = Solution()
result = solution.isPalindrome(121)
print(result)