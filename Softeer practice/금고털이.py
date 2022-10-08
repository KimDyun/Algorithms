import sys
from collections import deque

"""
    O(nlogn)의 sorting을 수행하면 N의 범위가 크기 때문에 시간초과가 남
    O(n+p) --> O(n)의 counting sort를 사용해야 함
"""
if __name__ == "__main__":
    W, N = map(int, sys.stdin.readline().split())
    PMmatrix = list()
    for i in range(1,(10**4)+1):
        PMmatrix.append([i, 0])
    for _ in range(N):
        m, p = map(int, sys.stdin.readline().split())
        PMmatrix[p-1][1] += m

    answer = 0
    sum_w = 0
    for i in range(10**4 - 1, -1, -1):
        weight = PMmatrix[i][1]
        if weight == 0 : continue
        if sum_w + weight >= W:
            res_w = W - sum_w
            answer += res_w * PMmatrix[i][0]
            break
        sum_w += weight
        answer += weight * PMmatrix[i][0]

    print(answer)
