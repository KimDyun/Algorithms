import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    weights = [0]
    weights.extend(list(map(int, sys.stdin.readline().split())))
    checks = [0]
    checks.extend([1 for _ in range(N)])

    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        if weights[A] <= weights[B]:
            checks[A] = 0
        if weights[B] <= weights[A]:
            checks[B] = 0
    print(sum(checks))