import sys

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    S = list(map(int, sys.stdin.readline().split()))
    interval = list()

    for _ in range(K):
        a,b = list(map(int, sys.stdin.readline().split()))
        denom = b-a+1
        ave = sum(S[a-1:b])/denom
        print("%0.2f" % ave)