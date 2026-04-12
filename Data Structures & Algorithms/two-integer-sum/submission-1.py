class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past={}
        for i,n in enumerate(nums):
            if target-n in past:
                return [past[target-n],i]
            past[n]=i