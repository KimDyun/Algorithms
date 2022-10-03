import sys

"""
    Quick sort 구현
"""
def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    while low <= high:
        while arr[low] < pivot:
            low += 1
        while arr[high] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low

def qsort(arr, low, high):
    if high <= low:
        return

    mid = partition(arr, low, high)
    qsort(arr, low, mid - 1)
    qsort(arr, mid, high)


if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrtip())
    lectures = tuple(map(int, sys.stdin.readline().split()))
