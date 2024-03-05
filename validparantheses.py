class Solution:
    def isValid(self, s:str) -> bool:
        for char in s:
            if char == '(' and char + 1 != ')':
                return False
            elif char == '[' and char + 1 