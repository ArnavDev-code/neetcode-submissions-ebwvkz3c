class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        final_answer = []
        # Create a list to track which words have already been put into a group
        visited = [False] * len(strs) 
        
        for i in range(len(strs)):
            # If we already grouped this word in a previous loop, skip it
            if visited[i]:
                continue
                
            # Start a new group with our current word
            current_group = [strs[i]]
            visited[i] = True
            
            # Start 'j' from 'i + 1' so we don't compare the word to itself (i==j) 
            # and don't look backwards at words we already processed
            for j in range(i + 1, len(strs)):
                
                # Fix 1: Use sorted() with parentheses, not brackets
                if sorted(strs[i]) == sorted(strs[j]):
                    
                    # Fix 2: Append the actual string, not the index 'j'
                    current_group.append(strs[j])
                    
                    # Mark this word as visited so the outer loop ignores it later
                    visited[j] = True 
                    
            # Fix 3: Move the append outside the inner loop so the whole group is saved
            final_answer.append(current_group)
            
        return final_answer