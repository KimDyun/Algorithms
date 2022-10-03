import sys

"""
    Quick sort 구현
"""

def partition(arr, low, high):
    pivot = arr[(low+high)//2][1]

    while low <= high:
        while arr[low][1] < pivot:
            low += 1
        while arr[high][1] > pivot:
            high -= 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1
    return low


# Function to find the partition position
def quickSort(arr, low, high):
    if high <= low:
        return

    mid = partition(arr, low, high)
    quickSort(arr, low, mid - 1)
    quickSort(arr, mid, high)


def scheduling(lect):
    cnt = 1
    _, ff = lect[0]
    for s, f in lect[1:]:
        if s >= ff:
            cnt+=1
            ff = f
    print(cnt)

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    lectures = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    quickSort(lectures, 0, N-1)
    scheduling(lectures)