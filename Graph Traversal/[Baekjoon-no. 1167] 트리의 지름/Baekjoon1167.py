import sys

def dfs(start, result):
    for n, d in graph[start]:  # n : node, d : distance
        if result[n] == 0:
            result[n] = result[start] + d
            dfs(n, result)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N)]
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        j = 1
        last_idx = len(line) - 1
        while j != last_idx:
            graph[line[0]-1].append((line[j] - 1, line[j + 1]))
            j += 2

    result1 = [0] * N
    dfs(0, result1)
    result1[0] = 0
    max_idx = max(range(len(result1)), key=lambda iter: result1[iter])  # argmax for list

    result2 = [0] * N
    dfs(max_idx, result2)
    result2[max_idx] = 0
    print(max(result2))
