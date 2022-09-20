import sys
from collections import deque
import copy


def bfs():
    tmp_graph = copy.deepcopy(graph)
    queue = deque()

    # Initial state of a laboratory where the virus has been leaked.
    for i in range(N):
        for j in range(M):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))

    # The state of the laboratory where the virus is being spread.
    while queue:
        cor_x, cor_y = queue.popleft()
        for k in range(4):
            new_x = cor_x + moveX[k]
            new_y = cor_y + moveY[k]

            if 0 <= new_x < N and 0 <= new_y < M and tmp_graph[new_x][new_y] == 0:
                tmp_graph[new_x][new_y] = 2
                queue.append((new_x, new_y))

    safe_area = 0
    global answer

    for n in range(N):
        safe_area += tmp_graph[n].count(0)
    answer = max(answer, safe_area)

def building_walls(wall_num):
    if wall_num == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                building_walls(wall_num+1)
                graph[i][j] = 0


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    moveX = [-1, 1, 0, 0]
    moveY = [0, 0, -1, 1]

    answer = 0
    building_walls(0)
    print(answer)
