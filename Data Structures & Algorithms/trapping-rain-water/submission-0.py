class Solution:
    def trap(self, height: List[int]) -> int:
        maxl=height[0]
        maxr=height[-1]
        res=0
        l=0
        r=len(height)-1
        while l<r:
            if maxl<maxr:
                l+=1
                maxl=max(height[l],maxl)
                res+=maxl-height[l]
            else:
                r-=1
                maxr=max(height[r],maxr)
                res+=maxr-height[r]
        return res