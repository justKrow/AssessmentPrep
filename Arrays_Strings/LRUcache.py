# Problem: LRU Cache(Least Recently Used Cache)
# Operations to support in O(1) time:

# get(key) – Return the value of the key if it exists in the cache, otherwise return -1.

# put(key, value) – Insert or update the value. If the cache reaches its capacity, evict the least recently used item.

# lru = LRUCache(2)  # capacity = 2

# lru.put(1, 1)
# lru.put(2, 2)

# lru.get(1)         # returns 1 (1 is now most recently used)

# lru.put(3, 3)      # evicts key 2 (least recently used)

# lru.get(2)         # returns -1 (not found)

# lru.put(4, 4)      # evicts key 1

# lru.get(1)         # returns -1
# lru.get(3)         # returns 3
# lru.get(4)         # returns 4
