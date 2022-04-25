#Making a list then solve

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.l = []
        while iterator.hasNext():
            self.l.append(iterator.next())

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.l:
            return self.l[0]

    def next(self):
        """
        :rtype: int
        """
        if self.l: 
            return self.l.pop(0)
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.l) != 0
