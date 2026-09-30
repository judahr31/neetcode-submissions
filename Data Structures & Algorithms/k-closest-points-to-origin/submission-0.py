import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for coor_set in points:
            x = coor_set[0]
            y = coor_set[1]

            distance = math.sqrt((x)**2 + (y)**2)

            min_heap.append((distance, [x ,y]))

        heapq.heapify(min_heap)

        results = []

        for i in range(k):
            results.append((heapq.heappop(min_heap))[1])
        return results
