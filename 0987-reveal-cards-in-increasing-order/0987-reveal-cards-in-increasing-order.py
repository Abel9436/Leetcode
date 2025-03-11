class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """

        deck.sort(reverse = True)

        ans = deque()

        for card in deck:
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(card)
        return list(ans)

        
        