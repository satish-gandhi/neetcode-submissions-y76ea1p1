class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxL= 0
        for n in nums:
            count = 1
            if n-1 in nums:
                continue
            while n+count in nums:
                count+=1
            maxL = max(maxL, count)
        return maxL
