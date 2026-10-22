class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        lis = self.m.get(key, [])
        lis.append((value, timestamp))
        self.m[key] = lis
      

    def get(self, key: str, timestamp: int) -> str:
        lst = self.m.get(key)
        if lst is None:
            return ""

        l, r = 0, len(lst) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if lst[m][1] <= timestamp:
                res = lst[m][0]
                l = m + 1
            else:
                r = m - 1

        return res


