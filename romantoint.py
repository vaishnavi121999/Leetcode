# class Solution:
#     def romanToInt(self, s:str) -> int:
#         result = 0
#         romanDict = {'I':1, 
#                     'V':5, 
#                     'X':10, 
#                     'L':50, 
#                     'C':100, 
#                     'D':500, 
#                     'M':1000
#                     }
#         for i in range (len(s)):
#             if i > len(s) and romanDict[s[i]] < romanDict [s[i+1]]:
#                 result -= romanDict[s[i]]
#             else:
#                 result += romanDict[s[i]]
#         return result


class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
    
solution = Solution()
result = solution.romanToInt("VIII")
print(result)
