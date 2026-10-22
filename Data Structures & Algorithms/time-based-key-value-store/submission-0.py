class TimeMap:

    def __init__(self):
        self.m = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        m2 = self.m.get(key, {})
        m2[timestamp] = value
        self.m[key] = m2
        

    def get(self, key: str, timestamp: int) -> str:
        m2 = self.m.get(key)
        if m2 is None:
            return ""

        max_stamp = -1
        res = ""

        for t in m2:
            if t <= timestamp and t > max_stamp:
                res = m2[t]
                max_stamp = t

        return res


