import sys
from collections import deque

if __name__ == "__main__":
    W, N = map(int, sys.stdin.readline().split())
    jews = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

    kf = (lambda x: x[0]*x[1])
    jews.sort(key = kf, reverse = True)

    jews = deque(jews)
    answer = 0
    total_W, total_P = 0, 0

    m, p = jews.popleft()
    if m < W:
        total_W = m
        total_P = m*p

    while jews:
        m, p = jews.popleft()
        if total_W + m > W:
            break
        total_W += m
        total_P += m*p
    res = W - total_W
    total_P += res*p

    print(total_P)