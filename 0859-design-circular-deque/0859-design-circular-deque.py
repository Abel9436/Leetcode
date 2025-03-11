class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.deque = deque()
        self.k = k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque.appendleft(value)
            return True
        return False
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if len(self.deque) < self.k:
            self.deque.append(value)
            return True
        return False
        

    def deleteFront(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.popleft()
            return True
        return False
        

    def deleteLast(self):
        """
        :rtype: bool
        """
        if len(self.deque) > 0:
            self.deque.pop()
            return True
        return False
        

    def getFront(self):
        """
        :rtype: int
        """
        return self.deque[0] if self.deque else -1
        

    def getRear(self):
        """
        :rtype: int
        """
        return self.deque[-1] if self.deque else -1

        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.deque == deque()
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.deque) == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()