# Runtime: 912 ms, faster than 16.74% of Python3 online submissions for Time Based Key-Value Store.
# Memory Usage: 86.6 MB, less than 20.00% of Python3 online submissions for Time Based Key-Value Store.

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[timestamp] = {key:value}
        if key not in self.keys.keys():
            self.keys[key] = [timestamp]
        else:
            self.keys[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys.keys() or timestamp < self.keys[key][0]:
            return ""

        elif timestamp in self.timestamps.keys():
            return self.timestamps[timestamp][key]

        else:

            l, r = 0, len(self.keys[key]) - 1
            while l <= r:
                m = l + (r - l) // 2
                if self.keys[key][m] < timestamp:
                    l = m + 1
                else:
                    r = m - 1
            return self.timestamps[self.keys[key][r]][key]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
