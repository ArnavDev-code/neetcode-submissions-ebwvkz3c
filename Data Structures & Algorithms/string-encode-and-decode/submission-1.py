class Solution:
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            # Glue together: Length + "#" + The actual string
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        # Our Explorer pointer runs through the encoded string
        while i < len(s):
            
            # 1. Find the delimiter '#'
            j = i
            while s[j] != "#":
                j += 1
                
            # 2. Extract the length number (everything between i and j)
            length = int(s[i:j])
            
            # 3. Extract the actual string using the length we just found
            # The string starts immediately after '#' (which is j + 1)
            # It ends exactly 'length' characters later (which is j + 1 + length)
            extracted_word = s[j+1 : j+1+length]
            res.append(extracted_word)
            
            # 4. Jump the 'i' pointer completely over the word we just extracted 
            # so it is perfectly positioned to read the next number!
            i = j + 1 + length
            
        return res