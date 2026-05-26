class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda t: t[1])

        minHeap = []
        passengers = 0

        for t in trips:
            p, s, e = t

            while minHeap and minHeap[0][0] <= s:
                passengers -= minHeap[0][1]
                heapq.heappop(minHeap)

            passengers += p

            if passengers > capacity:
                return False

            heapq.heappush(minHeap, [e, p])

        return True
