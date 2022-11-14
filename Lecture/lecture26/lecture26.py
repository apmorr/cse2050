class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"Entry(key = {self.key}, value = {self.value})"

    # from here, if we defined e as a mapping class, e.key = self.key and e.value = self.value


class ListMapping:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def put(self, key, value): # Do not have entries with the same key. Duplicate keys are not allowed, this is how you handle those
        for e in self._entries:
            if key == e.key:
                e.value = value # Overrides previous value if key is a duplicate
                return

        # Otherwise, add a new entry
        self._entries.append(Entry(key, value))

    def get(self, key): # use __getitem__ magic method to support square brackets like L['jake']. If you do this, replace put with __setitem__
        for e in self._entries:
            if key == e.key:
                return e.value

        raise KeyError(f"{key} not in mapping")

    
print(hash(27))
print(hash("Test"))
print(hash(-3917256334740424286))

print(hash(1))
print(hash(6969696969696969))