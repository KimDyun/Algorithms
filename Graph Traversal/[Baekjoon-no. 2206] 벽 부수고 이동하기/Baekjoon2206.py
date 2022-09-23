import sys
from collections import deque
from itertools import combinations

def bfs():
    graph[0] = 1
    visit = [[0, 0] for _ in range(size)]
    visit[0][1] = 1
    queue = deque()
    queue.append((0, 1))
    while queue:
        i, c = queue.popleft() # c : 벽을 깰 수 있는 횟수
        if i == size - 1:
            print(visit[i][c])
            exit(0)
        x, y = i // M, i % M
        move = [
            i - M if 0 < x else -1,
            i + M if x < N - 1 else -1,
            i - 1 if 0 < y else -1,
            i + 1 if y < M - 1 else -1
        ]
        for m in move:
            if m == -1:
                continue
            if c == 1 and graph[m] == 1:
                queue.append((m, 0))
                visit[m][0] = visit[i][1] + 1
            elif graph[m] == 0 and visit[m][c] == 0:
                queue.append((m, c))
                visit[m][c] = visit[i][c] + 1

    print(-1)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    size = N * M
    graph = [[0] * size]
    for idx in range(0, size, M):
        graph[idx: idx + M] = [*map(int, sys.stdin.readline().rstrip())]

    bfs()
