class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS=[0]*26
        CountT=[0]*26
        if len(s)!=len(t):
            return False
        for c in s:
            CountS[ord(c)-ord('a')]+=1
        for c in t:
            CountT[ord(c)-ord('a')]+=1
        return CountS==CountT