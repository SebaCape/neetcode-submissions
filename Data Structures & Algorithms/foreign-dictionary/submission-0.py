class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #Create adjacency matrix based on dictionary words
        adj_list = {c: set() for w in words for c in w}

        #Populate adjacency matrix based on sorting order of our words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
            
        visited = {}
        res = []

        def dfs(letter):
            if letter in visited:
                return visited[letter]

            visited[letter] = True

            for neighbor in adj_list[letter]:
                if dfs(neighbor):
                    return True

            visited[letter] = False
            res.append(letter)

        for letter in adj_list:
            if dfs(letter):
                return ""

        res.reverse()
        return "".join(res)
 