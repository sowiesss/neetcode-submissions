class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_set = set(s)
        t_set = set(t)
        if s_set != t_set:
            return False

        s_dict, t_dict= {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1
    
        return s_dict == t_dict