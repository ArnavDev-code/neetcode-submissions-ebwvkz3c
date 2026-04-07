class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        answer = []
        
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
                
            mid = left + 1
            right = len(nums) - 1
            
            while mid < right:
                current_sum = nums[left] + nums[mid] + nums[right]
                
                if current_sum == 0:
                    answer.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1
                        
                elif current_sum < 0:
                    mid += 1
                else:
                    right -= 1
                    
        return answer