class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        not_iterate = []
        answer = []
        for i in range(len(strs)):
            if i in not_iterate:
                continue
            current_group = []
            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    current_group.append(strs[j])
                    not_iterate.append(j)
            answer.append(current_group)
        return answer