# https://www.naukri.com/code360/problems/allocate-books_1090540
from typing import *

def findPages(arr: List[int], n: int, m: int) -> int:

    def isBookAllocationPossible(pageHoldingCapacity, totalStudents):
        cntStudent = 1
        prevStudentHolding = 0

        for pages in arr:
            if prevStudentHolding + pages <= pageHoldingCapacity:
                prevStudentHolding += pages
            else:
                # prev student has reached his capacity
                # we move to next student
                cntStudent += 1
                if cntStudent > totalStudents:
                    return False
                prevStudentHolding = pages

        return True

    # if students are more than books, return -1
    if m > n:
        return -1

    # to make sure each student can read one book,
    # we say one student can read book with max page available        
    low = max(arr)

    # highest search space is one student alone can read all the books
    high = sum(arr)
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if isBookAllocationPossible(mid, m):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result
         