class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        charS = {}
        charT = {}
        for c in s:
            charS[c] = 1+ charS.get(c,0)
        for c in t:
            charT[c] = 1+ charT.get(c,0)
        if charT == charS:
            return True
        else:
            return False