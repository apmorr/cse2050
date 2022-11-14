# See assignment for class attributes.
# Remember to include docstrings.
# Start with unittests
import random

class LocalRecord:
    def __init__(self, pos, max=None, min=None, precision=0):
        """Initialize local record with position and temps"""
        #round position to first decimal
        self.pos = (round(pos[0], precision), round(pos[1], precision))
        self.max = max
        self.min = min

    def add_report(self, temp):
        """Update max and min temps based on given report"""
        if self.max is None:
            self.max = temp
            self.min = temp
        elif temp > self.max:
            self.max = temp
        elif temp < self.min:
            self.min = temp

    def __eq__(self, other):
        """returns true iff two records are for same position"""
        return self.pos == other.pos

    def __hash__(self):
        """returns hash for object based on its position"""
        return hash(self.pos)

    def __repr__(self):
        """Returns object in string format"""
        return f"Record(pos={self.pos}, max={self.max}, min={self.min}"

class RecordsMap:
    def __init__(self):
        """Initializes record map with buckets, records, and length"""
        self._buckets = 100
        self._records = [[] for _ in range(self._buckets)]
        self._len = 0

    def __len__(self):
        """Returns length of Record Map"""
        return self._len

    def add_report(self, pos, temp):
        """Update max and min temps for given pos if needed"""
        new_record = LocalRecord(pos, max = temp, min = temp)
        bucket = self._records[hash(new_record) % self._buckets]

        # IF ITEM IS IN MAPPING:
        for record in bucket:
            if record == new_record:
                record.add_report(temp)
                return

        # OTHERWISE
        bucket.append(new_record)
        self._len += 1
        if len(self) > self._buckets * 2:
            self._rehash(self._buckets * 2)

    def __getitem__(self, pos):
        """Returns a desired record via brackets. Ex: rm[r1]"""
        new_record = LocalRecord(pos, 0)
        bucket = self._records[hash(new_record) % self._buckets]

        for record in bucket:
            if record == new_record:
                return (record.min, record.max)

        # UR AN IDIOT IF U GET THIS ERROR
        raise KeyError

    def __contains__(self, pos):
        """Returns true if a given pos is in the RecordsMap, false otherwise"""
        new_record = LocalRecord(pos, 0)
        bucket = self._records[hash(new_record) % self._buckets]
        for record in bucket:
            if record == new_record:
                return True
        return False

    def _rehash(self, m_new):
        """Rehash function for periodic rehashing of RecordMap for efficiency sake"""
        self._buckets *= 2
        new_L = [[] for i in range (self._buckets)]

        for bucket in self._records:
            for item in bucket:
                new_L[hash(item) % self._buckets].append(item)

        self._records = new_L[:]