import sys
from collections import deque
from itertools import combinations
import copy


def bfs():
    safety = []
    infection = []

    # Initial state of a laboratory where the virus has been leaked.
    for i in range(size):
        if graph[i] == 0:
            safety.append(i)
        if graph[i] == 2:
            infection.append(i)

    init_area = len(safety) + len(infection) - 3
    ans = 0

    num_cases_make_wall = combinations(safety, 3)

    for nc in num_cases_make_wall:
        new_graph = graph.copy()
        queue = safety.copy()
        infection_cnt = 0

        for n in nc:
            new_graph[n] = 1

        # The state of the laboratory where the virus is being spread.
        while queue:
            idx = queue.pop()
            infection_cnt += 1
            cor_x, cor_y = idx // M, idx % M

            move =[
                idx - M if 0 < cor_x else -1,
                idx + M if cor_x < N - 1 else -1,
                idx - 1 if 0 < cor_y else -1,
                idx + 1 if cor_y < M - 1 else -1
            ]
            for m in move:
                if m != -1 and new_graph[m] == 0:
                    new_graph[m] = 2
                    queue.append(m)

        ans = max(ans, init_area - infection_cnt)

    return ans


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    size = N * M
    graph = [0] * size
    for i in range(0, size, M):
        graph[i : i+M] = [*map(int, sys.stdin.readline().split())]

    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, -1, 1]

    answer = bfs()
    print(answer)
