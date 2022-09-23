import sys
from collections import deque

def bfs():
    q1 = deque()
    q2 = deque()

    not_zero = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0:
                not_zero += 1
                if graph[i][j] == 1:
                    q1.append((i, j))

    queue = q1
    candidate_queue = q2
    answer = 0
    while 1:
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                cx, cy = x + mx[i], y + my[i]
                if 0 <= cx < N and 0 <= cy < M and graph[cx][cy] == 0:
                    candidate_queue.append((cx, cy))
                    graph[cx][cy] = 1
                    not_zero += 1
        if candidate_queue:
            tmp = queue
            queue = candidate_queue
            candidate_queue = tmp
            answer += 1
        else:
            if not_zero == N*M:
                print(answer)
            else:
                print(-1)
            break

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]

    bfs()
