class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a =0
        b = 0
        while piles:
            if piles[0]>=piles[-1]:
                a+=piles.pop(0)
            else:
                a+=piles.pop()
            
            if piles[0]>=piles[-1]:
                a+=piles.pop(0)
            else:
                a+=piles.pop()

        return a>b