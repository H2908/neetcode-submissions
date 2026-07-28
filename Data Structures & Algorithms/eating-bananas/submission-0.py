from math import ceil

class Solution:
    def minEatingSpeed(self, piles, h):
        max_pile = max(piles)

        for k in range(1, max_pile + 1):
            hours = 0

            for pile in piles:
                hours += ceil(pile / k)

            if hours <= h:
                return k