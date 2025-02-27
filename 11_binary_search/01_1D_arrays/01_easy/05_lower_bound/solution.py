# https://www.naukri.com/code360/problems/lower-bound_8165382
from typing import *

def lowerBound(arr: List[int], n: int, x: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= x:
            # go more left to see if there is anymore smaller index
            ans = mid
            high = mid - 1
        else:
            # go rightward
            low = mid + 1

    return ans