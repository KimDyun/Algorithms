import sys
from collections import deque
from itertools import combinations


def bfs():
    safety = []  # safe area
    infection = []  # infected area

    # Initial state of a laboratory where the virus has been leaked.
    for i in range(size):
        if graph[i] == 0:
            safety.append(i)
        if graph[i] == 2:
            infection.append(i)

    init_area = len(safety) + len(infection) - 3  # wall-less area
    ans = 0

    num_cases_make_wall = combinations(safety, 3)  # the number of cases that you can make wall

    for case in num_cases_make_wall:
        new_graph = graph.copy()
        queue = infection.copy()

        infection_cnt = 0

        for c in case:
            new_graph[c] = 1  # build a wall

        # The state of the laboratory where the virus is being spread.
        while queue:
            idx = queue.pop()  # infected area
            infection_cnt += 1
            cor_x, cor_y = idx // M, idx % M  # column index and row index on a 2-dim grid.

            move = [
                idx - M if 0 < cor_x else -1,
                idx + M if cor_x < N - 1 else -1,
                idx - 1 if 0 < cor_y else -1,
                idx + 1 if cor_y < M - 1 else -1
            ]  # get indices of graph (1-dim list) after checking if the index is exceeded
                # when moving up, down, left, and right on a 2-dim grid.

            for m in move:
                if m != -1 and new_graph[m] == 0: # if virus can be spread
                    new_graph[m] = 2 # infection
                    queue.append(m) # store a infected area

        global answer

        answer = max(answer, init_area - infection_cnt)


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    size = N * M
    graph = [0] * size
    for i in range(0, size, M):
        graph[i: i + M] = [*map(int, sys.stdin.readline().split())]

    answer = 0
    bfs()
    print(answer)
