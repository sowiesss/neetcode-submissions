class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        m2 = self.m.get(key, {})
        m2[timestamp] = value
        self.m[key] = m2
        # print(self.m)

    def get(self, key: str, timestamp: int) -> str:
        m2 = self.m.get(key)
        if m2 is None:
            return ""

        times = sorted(m2)
        l, r = 0, len(times) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if times[m] <= timestamp:
                res = m2[times[m]]
                l = m + 1
            else:
                r = m - 1

        return res


