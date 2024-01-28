# this algorithm has 0(sqrt(N)) worst case runtime!
# The question is: You have two crystal balls which will break every time below a certain floor of a building
# Figure out the highest floor the crystal balls break at in better than O(N) time complexity.
# Binary search is worst case the same as a linear search O(N) so, by stepping Square Root of N, you get worst case Root N runtime.

import math
from typing import List

def two_crystal_balls(breaks: List[bool]) -> int:
    jump_amount = math.floor(math.sqrt(len(breaks)))
    i = jump_amount

    # jump root N times, check for breaks
    while i < len(breaks):
        if breaks[i]:
            break
        i += jump_amount

    # go back root N once you do find a break
    i -= jump_amount

    # step up to root N times to find where the break occurs
    for j in range(jump_amount + 1):
        if i < len(breaks) and breaks[i]:
            return i
        i += 1
    
    return -1

breaks = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True]

print(two_crystal_balls(breaks))

