# https://leetcode.com/problems/lemonade-change/
from typing import *

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if not fives:
                    return False
                else:
                    fives -= 1
                    tens += 1
            else:
                # bill is 20
                # we show greedy property here,
                # where we prioritise giving back 10 notes over 5s
                # so that we can use 5s for future 10 $ bill
                if (tens and fives):
                    tens -= 1
                    fives -= 1
                elif (fives >= 3):
                    fives -= 3
                else:
                    return False
        
        return True

        