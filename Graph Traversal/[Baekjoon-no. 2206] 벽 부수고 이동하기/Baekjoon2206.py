import sys
from collections import deque
from itertools import combinations

def bfs():
    graph[0] = 1
    queue = deque()
    queue.append((0, 0))
    
    while queue:
        i, c = queue.popleft()
        x, y = i // M, i % M
        move = [
            i - M if 0 < x else -1,
            i + M if x < N - 1 else -1,
            i - 1 if 0 < y else -1,
            i + 1 if y < M - 1 else -1
        ]
        for m in move:
            if m != -1:
                if graph[m] == 0:
                    queue.append((m, c))
                    graph[m] = graph[i] + 1
                    continue
                if graph[m] == 1 and c == 0 and m != 0:
                    queue.append((m, 1))
                    graph[m] = graph[i] + 1

    if graph[-1] == 0:
        return -1
    return graph[-1]

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    size = N * M
    graph = [0] * size
    for idx in range(0, size, M):
        graph[idx: idx + M] = [*map(int, sys.stdin.readline().rstrip())]

    answer = bfs()
    print(answer)
