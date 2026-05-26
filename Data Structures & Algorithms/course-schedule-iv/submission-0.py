class Solution:
    def checkIfPrerequisite(self, num_courses, prerequisites, queries):
        req_map = defaultdict(list)

        #Keep track of prerequisites
        for req, course in prerequisites:
            req_map[req].append(course)

        #Keep sets of which nodes are reachable from each node
        reachable = defaultdict(set)

        def dfs(node):
            for neighbor in req_map[node]:
                if neighbor not in reachable[node]:
                    reachable[node].add(neighbor)
                    dfs(neighbor)
                    #Join reachable sets of all nodes that can be reached
                    reachable[node] |= reachable[neighbor]

        #Populate each reachable set for each node
        for num in range(num_courses):
            dfs(num)

        return [q2 in reachable[q1] for q1, q2 in queries]