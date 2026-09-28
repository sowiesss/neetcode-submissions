class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        
        # print(res)
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            temp_list = s[i:].split('#', 1)
            # print(temp_list)
            len_num = len(temp_list[0])
            len_str = int(temp_list[0])
            i += len_num + 1
            # print(i)
            res.append(s[i:i + len_str])
            i += len_str
            # print(i)

        return res
            

