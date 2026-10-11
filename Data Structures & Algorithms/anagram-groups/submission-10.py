class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)
        for i, s in enumerate(strs):
            chars = [0] * 26
            for c in s:
                chars[ord(c)-ord('a')] += 1
            freq[tuple(chars)].append(s) 
        res = []
        return res.extend(freq.values())
        
            
