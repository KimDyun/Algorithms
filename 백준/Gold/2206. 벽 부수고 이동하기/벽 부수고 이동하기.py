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
        i, c = queue.popleft()
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
                    #if wall == 1 and graph[a][b] == 1:
                #                     visited[a][b][0] = visited[i][j][1] + 1
                #                     q.append([a, b, 0])
                #                 elif graph[a][b] == 0 and visited[a][b][wall] == 0:
                #                     visited[a][b][wall] = visited[i][j][wall] + 1
                #                     q.append([a, b, wall])
# def bfs():
#     graph[0][0] = 1
#     visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
#     visited[0][0][1] = 1

#     q = deque()
#     q.append([0, 0, 1])
#
#     while q:
#         i, j, wall = q.popleft()
#         if i == N - 1 and j == M - 1:
#             return visited[i][j][wall]
#         for k in range(4):
#             a = i + dx[k]
#             b = j + dy[k]
#             if 0 <= a < N and 0 <= b < M:
#                 if wall == 1 and graph[a][b] == 1:
#                     visited[a][b][0] = visited[i][j][1] + 1
#                     q.append([a, b, 0])
#                 elif graph[a][b] == 0 and visited[a][b][wall] == 0:
#                     visited[a][b][wall] = visited[i][j][wall] + 1
#                     q.append([a, b, wall])
#     return -1
#
#     #
#     # print(-1)

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())

    size = N * M
    graph = [[0] * size]
    for idx in range(0, size, M):
        graph[idx: idx + M] = [*map(int, sys.stdin.readline().rstrip())]

    # graph = [[*map(int, sys.stdin.readline().rstrip())] for _ in range(N)]
    # dx = [1,-1,0,0]
    # dy = [0,0,1,-1]

    bfs()
