from collections import OrderedDict

class LRU_Cache:
    def __init__(self, capacity=5):
        self.capacity = max(capacity, 0)
        self.cache = OrderedDict()

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            self.cache.move_to_end(key)
            return value                     # Cache hit
        else:
            return -1                        # Cache miss

    def set(self, key, value):
        if key is None:
            print('NoneType Key is not allowed.')
            return

        if self.capacity == 0:
            print('Warning. Cannot set any value. Capacity is ZERO.')
            return

        if self.__len__() >= self.capacity:
            self.cache.popitem(last=False)               # Cache is at capacity, remove least recently used item

        self.cache[key] = value

    def __len__(self):
        return len(self.cache)

    def __repr__(self):
        str_cache = '\n==================\nCache:\n'
        for item in self.cache:
            str_cache += str(item) + ' -> ' + str(self.cache[item]) + '\n'
        str_cache += '==================\n'

        return str_cache

######################################### TEST ##################################################
def test_none_key():
    print('\n--------------------   TEST_NONE_KEY   ------------------')

    cache = LRU_Cache(2)
    cache.set(1, 1)
    cache.set(None, 2)        # Print 'NoneType Key is not allowed.'

    print(cache)              # cache only contains 1

    print('--------------------   END: TEST_NONE_KEY   ------------------\n')

def test_zero_cache():
    print('\n--------------------   TEST_ZERO_CACHE   ------------------')

    cache = LRU_Cache(0)
    cache.set(1, 1)           # Print 'Warning. Cannot set any value. Capacity is ZERO.'
    print(cache)              # Print empty cache

    print('Get 1 from cache, return: {}, expected: {}'.format(cache.get(1), -1))     # return -1. No element is in Cache

    print('--------------------   END: TEST_ZERO_CACHE   ------------------\n')

def test_negative_cache_capa():
    print('\n--------------------   TEST_NEGATIVE_CACHE_CAPA   ------------------')

    cache = LRU_Cache(-1)
    cache.set(1, 1)           # Print 'Warning. Cannot set any value. Capacity is ZERO.'
    print(cache)              # Print empty cache

    print('Get 1 from cache, return: {}, expected: {}'.format(cache.get(1), -1))     # return -1. No element is in Cache

    print('--------------------   END: TEST_NEGATIVE_CACHE_CAPA   ------------------\n')
        
def test():
    print('\n--------------------   TEST   ------------------')

    cache = LRU_Cache(5)

    cache.set(1, 1)
    cache.set(2, 2)
    cache.set(3, 3)
    cache.set(4, 4)
    print(cache)                                                                      # Cache should contain: 1 2 3 4

    print('Get 1 from cache, return: {}, expected: {}'.format(cache.get(1), 1))       # Cache hit: returns 1
    print('Get 2 from cache, return: {}, expected: {}'.format(cache.get(2), 2))       # Cache hit: returns 2
    print('Get 9 from cache, return: {}, expected: {}'.format(cache.get(9), -1))      # Cache miss: returns -1 because 9 is not present in the cache

    cache.set(5, 5) 
    cache.set(6, 6)                                                                   # Cache reachs capacity. The least recent used element 3 is removed.
    print(cache)                                                                      # Cache: 4 1 2 5 6 (least recently -> most recently)

    print('Get 3 from cache, return: {}, expected: {}'.format(cache.get(3), -1))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

    print('--------------------   END: TEST   ------------------\n')

def TEST_SUITE():
    test()
    test_zero_cache()
    test_negative_cache_capa()
    test_none_key()

TEST_SUITE()