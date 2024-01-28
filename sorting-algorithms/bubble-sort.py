from typing import List
def bubble_sort(arr: List[int]) -> None:
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # swap the elements
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp
                
arr = [1, 5, 3, 8, 6, 3, 6, 8, 9, 5, 6, 1, 2, 4, 6, 0]

bubble_sort(arr)
print(arr)