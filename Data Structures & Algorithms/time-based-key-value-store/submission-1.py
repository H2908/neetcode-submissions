class TimeMap:

    def __init__(self):
        # key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key does not exist, create a new list
        if key not in self.store:
            self.store[key] = []

        # Store timestamp and value
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        # If key does not exist
        if key not in self.store:
            return ""

        values = self.store[key]

        low = 0
        high = len(values) - 1

        answer = ""

        # Binary search for largest timestamp <= given timestamp
        while low <= high:

            mid = (low + high) // 2

            if values[mid][0] <= timestamp:
                # This timestamp is valid, store the answer
                answer = values[mid][1]

                # Try to find a later timestamp
                low = mid + 1

            else:
                # Timestamp is too large, search left
                high = mid - 1

        return answer