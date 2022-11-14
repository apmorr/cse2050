from BSTNode import BSTNode

class BSTMap:
    def __init__(self):
        """Creates a new BSTMap"""
        self._root = None

    def put(self, key, value):
        """adds k:v pair to BSTMap"""
        if self._root is None:
            self._root = BSTNode(key, value)
            return
        else:
            self._root = self._root.put(key, value)

    def get(self, key):
        """Returns value associated w/ key"""
        if self._root is None: raise KeyError

        return self._root.get(key)

    def __contains__(self, key):
        """Returns true if key is in BSTMap, false otherwise"""
        if self._root is None: return False

        return key in self._root

    def __repr__(self):
        """Returns string representation of BSTMap"""
        return repr(self._root)

if __name__ == '__main__':
     
    bst1 = BSTMap()
    for i in range(8):
        assert not i in bst1        # test contains (false)
        bst1.put(i, str(i))
        assert bst1.get(i) == str(i)    # tests put/get 
        assert i in bst1            # tests contains (true)

    print(bst1)

# 0 <--bst1._root
#  \
#   1
#    \
#     2 
#    /
#  1.5