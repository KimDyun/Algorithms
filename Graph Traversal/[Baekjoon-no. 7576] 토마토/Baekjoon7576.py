import sys
from collections import deque

def bfs():
    q1 = deque()
    q2 = deque()

    not_zero = 0

    for i in range(size):
        if graph[i] != 0:
            not_zero += 1
            if graph[i] == 1:
                q1.append(i)

    queue = q1
    candidate_queue = q2
    answer = 0
    while 1:
        while queue:
            idx = queue.popleft()
            x, y = idx // M, idx % M
            move = [
                idx - M if 0 < x else -1,
                idx + M if x < N - 1 else -1,
                idx - 1 if 0 < y else -1,
                idx + 1 if y < M - 1 else -1
            ]
            for m in move:
                if m != -1 and graph[m] == 0:
                    candidate_queue.append(m)
                    graph[m] = 1
                    not_zero += 1

        if candidate_queue:
            tmp = queue
            queue = candidate_queue
            candidate_queue = tmp
            answer += 1
        else:
            if not_zero == N * M:
                print(answer)
            else:
                print(-1)
            break

if __name__ == '__main__':
    M, N = map(int, sys.stdin.readline().split())
    size = M*N
    graph = list()
    for i in range(0, size, M):
        graph[i:i+M] = [*map(int, sys.stdin.readline().split())]
    bfs()
