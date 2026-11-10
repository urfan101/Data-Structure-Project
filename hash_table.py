class HashTable:
    """Separate chaining ilə sadə Hash Table.
    Hər bucket bir list-dir, kolliziya olduqda elementlər həmin list-ə əlavə olunur."""

    def __init__(self, capacity=8, max_load=0.75):
        self.capacity = capacity
        self.max_load = max_load
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:              # açar artıq var -> yenilə
                bucket[i] = (key, value)
                return
        bucket.append((key, value))   # yeni açar -> zəncirə əlavə et
        self.size += 1
        if self.size / self.capacity > self.max_load:
            self._resize()

    def get(self, key, default=None):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        return default

    def remove(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return True
        return False

    def _resize(self):
        old = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old:
            for k, v in bucket:
                self.put(k, v)

    def items(self):
        for bucket in self.buckets:
            yield from bucket

    # Python-un adi sintaksisi üçün
    def __setitem__(self, key, value): self.put(key, value)
    def __delitem__(self, key):
        if not self.remove(key):
            raise KeyError(key)
    def __getitem__(self, key):
        sentinel = object()
        v = self.get(key, sentinel)
        if v is sentinel:
            raise KeyError(key)
        return v
    def __contains__(self, key): return self.get(key, _MISSING) is not _MISSING
    def __len__(self): return self.size
    def __repr__(self): return "{" + ", ".join(f"{k!r}: {v!r}" for k, v in self.items()) + "}"


_MISSING = object()


if __name__ == "__main__":
    ht = HashTable(capacity=4)
    ht["alma"] = 5
    ht["armud"] = 3
    ht["nar"] = 7
    ht["heyva"] = 2
    ht["alma"] = 10          # yenilənmə
    ht["gilas"] = 1          # resize tetikləyə bilər

    print(ht)
    print("alma:", ht["alma"])
    print("var?", "nar" in ht, "| yoxdur?", "banan" in ht)
    del ht["armud"]
    print("ölçü:", len(ht), "| capacity:", ht.capacity)
