class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(wordList)
        wildsearch = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]
                wildsearch[pattern].add(word)

        visit = set([beginWord])    
        q = deque([beginWord])
        step = 1
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return step
                for i in range(len(w)):
                    pattern = w[:i] + '*' + w[i+1:]
                    for nei in wildsearch[pattern]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            step += 1
        return 0
        