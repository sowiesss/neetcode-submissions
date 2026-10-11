class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c)-ord('a')] += 1
            sublist = group.get(chars, []).append(s)
            group[chars] = sublist
        
        res = []
        for k, l in result.items():
            res.append(l)
        return res
            
