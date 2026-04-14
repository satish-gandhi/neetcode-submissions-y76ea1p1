class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''
        for s in strs:
            enc+=str(len(s))+'#'+s
        return enc
    def decode(self, s: str) -> List[str]:
        i=0
        strs = []
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length = int(s[i:j])
            i=j+1
            strs.append(s[i:i+length])
            i = i+length
        return strs

