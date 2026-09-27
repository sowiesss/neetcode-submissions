class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = {}
        for i, s in enumerate(strs):
            sort = "".join(sorted(s))
            sublist = sorted_strs.get(sort, [])
            sublist.append(s)
            sorted_strs[sort] = sublist
        
        result = []
        for k, l in sorted_strs.items():
            result.append(l)

        return result
