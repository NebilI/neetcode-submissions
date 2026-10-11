import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        square_dist = lambda x: x[0] ** 2 + x[1] ** 2
        min_heap = []
        heapq.heapify(min_heap)

        for point in points:
            heapq.heappush(min_heap, (-square_dist(point), point))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [x[1] for x in min_heap]

        