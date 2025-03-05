class RecentCounter(object):

    def __init__(self):
        self.deq =   deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.deq.append(t)

        validator = t - 3000
        

        while self.deq[0] < validator:
            self.deq.popleft()

        return len(self.deq)
        



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)