class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_set = set(s)
        t_set = set(t)
        if len(s_set) != len(t_set):
            return False

        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        for key, freq in s_dict.items():
            if t_dict[key] != freq:
                return False

        return True