import sys


def graph_loader(input):
    graph = dict()

    for e in input:
        if e[0] not in graph:
            graph[e[0]] = [e[1]]
        else:
            graph[e[0]].append(e[1])

        if e[1] not in graph:
            graph[e[1]] = [e[0]]
        else:
            graph[e[1]].append(e[0])

    return graph


def DFS(graph, start):
    visited = list()
    stack = list()

    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                stack.extend(sorted(graph[node], reverse=True))
    return visited


def BFS(graph, start):
    visited = list()
    queue = list()

    queue.append(start)
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node in graph:
                queue.extend(sorted(graph[node], reverse=False))
    return visited


if __name__ == '__main__':
    N, M, start = map(int, sys.stdin.readline().split())
    input = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    graph = graph_loader(input)
    dfs = DFS(graph, start)
    bfs = BFS(graph, start)

    print(' '.join(map(str, dfs)))
    print(' '.join(map(str, bfs)))
