class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        m = len(wordList[0])
        wordSet = set(wordList)    
        qb, qe = deque([beginWord]), deque([endWord])
        fromB, fromE = {beginWord: 1}, {endWord: 1}

        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                fromB, fromE = fromE, fromB
            for _ in range(len(qb)):
                w = qb.popleft()
                step = fromB[w]
                for i in range(m):
                    for c in range(ord('a'), ord('z') + 1):
                        char = chr(c)
                        if char == w[i]:
                            continue
                        nei = w[:i] + char + w[i+1:]
                        if nei in wordSet:
                            if nei in fromE:
                                return step + fromE[nei]
                            if nei not in fromB:
                                fromB[nei] = step + 1
                                qb.append(nei)
        return 0
        