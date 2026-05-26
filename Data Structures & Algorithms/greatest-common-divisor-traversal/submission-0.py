class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        #Handle edge cases
        N = len(nums)
        if N == 1:
            return True
        if any(num == 1 for num in nums):
            return False

        #Utilize prime sieve to find primes from our range of numbers
        MAX = max(nums)
        sieve = [0] * (MAX + 1)
        p = 2
        while p * p <= MAX:
            if sieve[p] == 0:
                for composite in range(p * p, MAX + 1, p):
                    sieve[composite] = p
            p += 1

        #Populate our adjacency list based on numerical connection to prime factors
        adj = defaultdict(list)
        for i in range(N):
            num = nums[i]
            if sieve[num] == 0:  # num is prime
                adj[i].append(N + num)
                adj[N + num].append(i)
                continue

            while num > 1:
                prime = sieve[num] if sieve[num] != 0 else num
                adj[i].append(N + prime)
                adj[N + prime].append(i)
                while num % prime == 0:
                    num //= prime

        #Utilize DFS to determine if graph is connected (GCD is bidirectional)
        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)

        #Check if all nodes are reachable, otherwise return False
        for i in range(N):
            if i not in visited:
                return False
            
        return True