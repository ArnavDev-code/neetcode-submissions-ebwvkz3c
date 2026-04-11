class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        l, r, m, c = 0, 0, 0, 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                c = r - l + 1  
                if c > m:
                    m = c
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return m