class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amt = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                if i == j :
                    continue
                curr_amt = min(heights[i] , heights[j]) * (j-i)
                if curr_amt > max_amt:
                    max_amt = curr_amt
        return max_amt