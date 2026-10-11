class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for s in strs:
            lenth = len(s)
            res += lenth + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(str):
            temp_list = str[i:].split('#', 1)
            len_num = len(temp_list[0])
            len_str = int(temp_list[0])
            i += len_num
            res.append(str[i:i + len_str])
            i += len_str

        return res
            

