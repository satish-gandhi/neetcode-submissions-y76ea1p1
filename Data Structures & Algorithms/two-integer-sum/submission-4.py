class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valpos = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in valpos:
                return [valpos[diff], i]
            valpos[v]=i