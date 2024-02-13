from typing import List

def linear_search(haystack: List[int], needle: int) -> bool:
    for each in haystack:
        if each == needle:
            return True
    return False

# example

haystack = [3, 4, 5, 6, 7, 8, 9]
print(linear_search(haystack, 10))