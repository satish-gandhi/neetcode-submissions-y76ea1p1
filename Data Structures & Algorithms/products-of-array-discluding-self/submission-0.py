class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        out=[1 for n in nums]
        for i in range(1,len(nums)):
            pre=pre*nums[i-1]
            out[i]=pre*out[i]
        print(out)
        post=1
        for i in range(len(nums)-2,-1,-1):
            post=post*nums[i+1]
            out[i]=post*out[i]
        print(out)
        return out
