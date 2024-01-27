from typing import List

def binary_search(nums: List[int], target: int) -> bool:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mp = (l + r) // 2
        if nums[mp] == target:
            return mp
        elif nums[mp] < target:
            l = mp + 1
        else:
            r = mp - 1

    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5

print(binary_search(nums, target))