# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    current.next = LinkedPair(key, value)
                    return
                current = current.next
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        index = self._hash_mod(key)

        if self.storage[index] is None:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    current = None
                    return
                current = current.next
            return
        self.storage[index] = None

    def retrieve(self, key):
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            if self.storage[index].key == key:
                return self.storage[index].value
            else:
                current = self.storage[index]
                while current is not None:
                    if current.key == key:
                        return current.value
                    current = current.next
        else:
            return None

    def resize(self):
        self.capacity *= 2
        old_storage = self.storage
        new_storage = [None] * self.capacity
        self.storage = new_storage
        for item in old_storage:
            current = item
            while current is not None:
                self.insert(current.key, current.value)
                current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")

###
