class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        strset = set()
        maxL = 0
        for r in range(len(s)):
            while s[r] in strset:
                strset.remove(s[l])
                l+=1
            strset.add(s[r])
            L = r-l+1
            maxL = max(maxL, L)
        return maxL
            
        
            
