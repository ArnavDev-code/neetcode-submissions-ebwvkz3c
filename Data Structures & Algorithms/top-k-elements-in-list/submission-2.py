class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = list(set(nums))
        output = []
        frequency = []
        for i in range(len(check)):
            count = 0
            for j in range(len(nums)):
                if check[i] == nums[j]:
                    count = count + 1
            frequency.append([count,check[i]])
        
        frequency.sort(reverse = True)
        for x in range(k):
            output.append(frequency[x][1])
        return output
                