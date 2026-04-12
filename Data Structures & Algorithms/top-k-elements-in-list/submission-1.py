class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict()
        rev=defaultdict(list)
        for n in nums:
            res[n]=1+res.get(n,0)
        rev=defaultdict(list)
        for key,v in res.items():
            rev[v].append(key)
        result=[]
        for i in range(len(nums),0,-1):
            if i in rev:
                result.extend(rev[i])
        return result[:k]