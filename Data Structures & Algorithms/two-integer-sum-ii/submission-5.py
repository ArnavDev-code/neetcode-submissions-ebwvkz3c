class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = 1
        while left < len(numbers) - 1:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            right += 1
            if right == len(numbers):
                left += 1         
                right = left + 1  