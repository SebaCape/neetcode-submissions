class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)

        if endWord not in wordList:
            return 0

        res, q = 0, deque([beginWord])

        while q:
            res += 1
            for _ in range(len(q)):
                node = q.popleft()

                if node == endWord:
                    return res

                for i in range(len(node)):
                    for char in range(97, 123):
                        if chr(char) == node[i]:
                            continue
                        neighbor = node[:i] + chr(char) + node[i + 1:]
                        if neighbor in wordList:
                            q.append(neighbor)
                            wordList.remove(neighbor)

        return 0

