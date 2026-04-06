class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s:
            if char.isalnum():
                s_list.append(char.lower())
        if s_list == s_list[::-1]:
            return True
        else:
            return False