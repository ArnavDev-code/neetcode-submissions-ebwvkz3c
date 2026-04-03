class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = sorted(set(nums))
        longest_streak = 1
        for i in range(len(result)):
            streak = 1
            current = result[i]
            for j in range(i+1 ,len(result)):
                if result[j] == current + 1:
                    streak = streak + 1
                    current = result[j]
                else:
                    break
            if streak > longest_streak:
                longest_streak = streak
        return longest_streak