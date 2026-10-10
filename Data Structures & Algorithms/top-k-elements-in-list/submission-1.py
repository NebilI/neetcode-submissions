import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        c = []
        for key,v in counts.items():
            c.append((v,key))
        
        
        heapq.heapify_max(c)
        result = []
        for i in range(0,k):
            t = heapq.heappop_max(c)[1]
            print(i,t)
            result.append(t)

        return result
        
        