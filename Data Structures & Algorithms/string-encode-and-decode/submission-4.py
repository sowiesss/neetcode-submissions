class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            temp_list = s[i:].split('#', 1)
            len_num = len(temp_list[0])
            len_str = int(temp_list[0])
            i += len_num
            res.append(s[i:i + len_str])
            i += len_str

        return res
            

