import sys

"""
    O(nlogn) 문제, 최장 증가 수열을 만들어주어야 함
    증가 수열 만들 시 인덱스 찾을 때 Binary Search 이용, BS를 할 때 항상 자료는 오름차순으로 정렬되어 있어야 함 (최장 증가 수열 만든 이유)
    정방향, 역방향 총 2회 계산하며, 각각 최대로 오를 수 있는 돌 수를 저장 
    증가 수열 만들 때 인덱스 찾기 : O(logN) - BS
    모든 돌 순차 탐색 : O(N) - 반복문
"""

def BS(arr, s, e, tar):
    _isend = False
    length = e
    mid = 0
    if not arr:
        arr.append(tar)
        return 0
    while s <= e:
        mid = (s + e) // 2
        if tar <= arr[mid]:
            e = mid - 1
            _isend = True
        else:
            s = mid + 1
            _isend = False
    idx = mid if _isend is True else mid + 1

    if idx > length:
        arr.append(tar)
    else:
        arr[idx] = tar
    return idx

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    rocks = list(map(int, sys.stdin.readline().split()))

    A = list()
    B = list()
    C = list()
    D = list()
    start, end, end2 = 0, 0, 0
    for i in range(N):
        # forward
        j = BS(A, start, end, rocks[i])
        B.append(j)
        if end < j:
            end = j
        # backward
        k = BS(C, start, end2, rocks[N-(i+1)])
        D.append(k)
        if end2 < k:
            end2 = k

    answer = 0
    for i in range(N):
        s = B[i]+D[N-(i+1)]
        if s > answer:
            answer = s
    print(answer + 1)

