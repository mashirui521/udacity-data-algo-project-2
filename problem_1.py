class LRU_Cache:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.cache = dict()
        self.lookup_frequency = dict()

    def get(self, key):
        if key in self.cache:
            self.lookup_frequency[key] = self.lookup_frequency.get(key, 0) + 1
            return self.cache[key]           # Cache hit
        else:
            return -1                        # Cache miss

    def set(self, key, value):
        if self.__len__() >= self.capacity:
            self.remove_lru()                # Cache is at capacity, remove least recently used item
        self.cache[key] = value
        self.lookup_frequency[key] = 0

    def remove_lru(self):
        least_used_key = min(self.lookup_frequency, key=self.lookup_frequency.get)
        self.cache.pop(least_used_key)
        self.lookup_frequency.pop(least_used_key)

    def __len__(self):
        return len(self.cache)

    def __repr__(self):
        str_cache = '\n==================\nCache:\n'
        for item in self.cache:
            str_cache += str(item) + ' -> ' + str(self.cache[item]) + '\n'
        str_cache += '==================\n'

        return str_cache

######################################### TEST ##################################################
        
def test():
    cache = LRU_Cache(5)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    print(cache)

    print('Get 1 from cache, return: {}, expected: {}'.format(cache.get(1), 1))       # returns 1
    print('Get 2 from cache, return: {}, expected: {}'.format(cache.get(2), 2))       # returns 2
    print('Get 9 from cache, return: {}, expected: {}'.format(cache.get(9), -1))      # returns -1 because 9 is not present in the cache

    cache.set(5, 5) 
    cache.set(6, 6)
    print(cache)

    print('Get 3 from cache, return: {}, expected: {}'.format(cache.get(3), -1))       # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

test()