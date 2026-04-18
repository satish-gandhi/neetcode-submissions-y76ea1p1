class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = {}
        charT = {}
        for c in s:
            charS[c] = 1 + charS.get(c, 0)
        for c in t:
            charT[c] = 1 + charT.get(c, 0)
        return charS == charT
