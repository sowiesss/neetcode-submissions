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

        times = sorted(m2, reverse=True)
        if times and times[0] <= timestamp:
            return m2[times[0]]

        return res


