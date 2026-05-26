class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Create and populate our graph (reverse lexicographical order)
        adj_list = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj_list[src].append(dst)

        stack = ["JFK"]
        res = []

        #Push flights from our current stack top if adjacent flights exist, otherwise pop our current airport into res
        while stack:
            curr = stack[-1]
            if not adj_list[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj_list[curr].pop())
        
        return res[::-1]