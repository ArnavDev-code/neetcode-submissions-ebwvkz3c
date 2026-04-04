class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = 1
        
        # We use a while loop so we have 100% control over the pointers
        while left < len(numbers) - 1:
            
            # Your exact check!
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
                
            # Always move right forward first
            right += 1
            
            # THE FIX: If right falls off the end of the list...
            if right == len(numbers):
                left += 1         # Move left forward by 1
                right = left + 1  # Reset right to sit right next to left