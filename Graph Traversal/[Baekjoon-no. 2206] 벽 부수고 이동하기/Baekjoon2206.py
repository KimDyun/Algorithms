if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    size = N * M
    graph = [0] * size
    for i in range(0, size, M):
        graph[i: i + M] = [*map(int, sys.stdin.readline().split())]

    answer = 0
    bfs()
    print(answer)
