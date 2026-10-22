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

        times = sorted(m2, reverse=True)
        
        for t in times:
            if t <= timestamp:
                return m2[t]

        return ""


