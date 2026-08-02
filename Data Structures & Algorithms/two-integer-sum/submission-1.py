class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        curr = 0
        for i,v in enumerate(nums):
            if target-v in seen:
                return[seen[target-v],i]
            else:
                seen[v] = i
        