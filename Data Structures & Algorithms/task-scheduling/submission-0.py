import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq_map = {}
        for task in tasks:
            if task in freq_map:
                freq_map[task] += 1
            else:
                freq_map[task] = 1

        freq_max_heap = [-value for value in freq_map.values()]
        heapq.heapify(freq_max_heap)

        time = 0
        cooldown_queue = deque()

        while freq_max_heap or cooldown_queue:
            time += 1

            if freq_max_heap:
                remaining_tasks = heapq.heappop(freq_max_heap) + 1

                if remaining_tasks < 0:
                    cooldown_queue.append((remaining_tasks, time + n))

            if cooldown_queue and cooldown_queue[0][1] == time:
                freq_left, _ = cooldown_queue.popleft()
                heapq.heappush(freq_max_heap, freq_left)

        return time



