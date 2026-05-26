class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #Initialize empty matrix of zeroes and coordinate matrix
        mat = [[0] * k for i in range(k)]
        coordinates = [[0,0] for _ in range(k)]
        
        #Create and populate adjacency matrices holding numerical relationships (above to below, left to right,) and their indegrees
        adj_list_rows, adj_list_cols = defaultdict(set), defaultdict(set)

        for abv, blw in rowConditions:
            adj_list_rows[abv].add(blw)
        for lft, rgt in colConditions:
            adj_list_cols[lft].add(rgt)

        indegrees_rows, indegrees_cols = [0] * k, [0] * k

        for i in range(k):
            for j in adj_list_rows[i + 1]:
                indegrees_rows[j - 1] += 1
            for l in adj_list_cols[i + 1]:
                indegrees_cols[l - 1] += 1

        #Run Kahns on each graph to find proper topological ordering and create coordinates for each number
        vq = deque([a + 1 for a in range(len(indegrees_rows)) if indegrees_rows[a] == 0])
        hq = deque([b + 1 for b in range(len(indegrees_cols)) if indegrees_cols[b] == 0])
        vres, hres = [], []

        #Graph with no indegree zero cannot be a DAG
        if not vq or not hq:
            return []

        while vq:
            cur_node = vq.popleft()
            for node in adj_list_rows[cur_node]:
                indegrees_rows[node - 1] -= 1
                if indegrees_rows[node - 1] == 0:
                    vq.append(node)
            vres.append(cur_node)

        while hq:
            cur_node = hq.popleft()
            for node in adj_list_cols[cur_node]:
                indegrees_cols[node - 1] -= 1
                if indegrees_cols[node - 1] == 0:
                    hq.append(node)
            hres.append(cur_node)

        #If all nodes are not processed a cycle exists
        if len(hres) != k or len(vres) != k:
            return []

        #Find coordinates, populate, and return resultant matrix
        for idx1, v in enumerate(vres):
            coordinates[v - 1][0] = idx1
        for idx2, h in enumerate(hres):
            coordinates[h - 1][1] = idx2

        for val, coord in enumerate(coordinates):
            mat[coord[0]][coord[1]] = val + 1

        return mat