class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #Sort intervals by start point
        intervals.sort()
        
        #Create indexed queries and sort (to maintain solution ordering)
        i_queries = [(queries[i], i) for i in range(len(queries))]
        i_queries.sort()
        
        res = [-1] * len(queries)
        min_heap = []  #(length, end)
        interval_idx = 0
        i_len = len(intervals)
        
        for q, i in i_queries:
            #Add all intervals that start at or before this query
            while interval_idx < i_len and intervals[interval_idx][0] <= q:
                start, end = intervals[interval_idx]
                length = end - start + 1
                heapq.heappush(min_heap, (length, end))
                interval_idx += 1
            
            #Remove intervals that end before this query (invalid)
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            #Append minimum valid interval to our result
            if min_heap:
                res[i] = min_heap[0][0]
        
        return res