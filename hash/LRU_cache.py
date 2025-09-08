class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curr_stored = []
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.curr_stored:
            self.curr_stored = [x for x in self.curr_stored if x != key]
            if len(self.curr_stored) == self.cap:
                self.curr_stored = self.curr_stored[1:]
            self.curr_stored.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.curr_stored = [x for x in self.curr_stored if x != key]
        if len(self.curr_stored) == self.cap:
            self.curr_stored = self.curr_stored[1:]
        self.curr_stored.append(key)
        # dont actually delete any keys
        self.cache[key] = value
        return
        

