from typing import List

def qs(arr: List[int], lo: int, hi: int,) -> None:
    if lo >= hi:
        return
    
    pivotIdx = partition(arr, lo, hi)
    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)
    

def partition(arr: List[int], lo: int, hi: int) -> int:
    pivot = arr[hi]
    idx = lo - 1

    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
    
    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx

def quick_sort(arr: List[int]) -> None:
    qs(arr, 0, len(arr) - 1)


# example

arr = [9, 3, 7, 4, 69, 420, 42]

quick_sort(arr)
print(arr)