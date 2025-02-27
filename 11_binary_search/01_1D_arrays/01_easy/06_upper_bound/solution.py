# https://www.naukri.com/code360/problems/implement-upper-bound_8165383
from typing import *

def upperBound(arr: List[int], x: int, n: int) -> int:
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            # go more left to see if there is anymore smaller index
            ans = mid
            high = mid - 1
        else:
            # go rightward
            low = mid + 1

    return ans