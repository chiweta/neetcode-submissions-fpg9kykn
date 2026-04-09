class Solution:
    def isPalindrome(self, s: str) -> bool:
       fixedstr=""

       for char in s:
            if char.isalnum():
                fixedstr += char.lower()
       left = 0
       right = len(fixedstr)-1

       while left < right:
            if fixedstr[left] != fixedstr[right]:
                return False
            left+=1
            right-=1
       return True

