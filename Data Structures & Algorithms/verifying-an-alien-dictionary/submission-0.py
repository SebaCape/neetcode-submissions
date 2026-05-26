class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #Create lexicographical weight map for each character
        order_index = {c: i for i, c in enumerate(order)}

        #Loop through all adjacent pairs of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            #Loop through all characters in word 1
            for j in range(len(w1)):
                #If we reach the end of word 2, we terminate because it implies non-sortedness
                if j == len(w2):
                    return False

                #In the case that both words share the same character at an index, ensure they are lexicographically sorted
                if w1[j] != w2[j]:
                    if order_index[w1[j]] > order_index[w2[j]]:
                        return False
                    #In the case that they are lexicographically sorted, we no longer have to compare any further characters
                    break
        return True