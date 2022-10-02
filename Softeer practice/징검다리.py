import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())

    rocks = list(map(int, sys.stdin.readline().split()))
    cnt_list = [1] * N
    for i in range(1, N):
        max_idx = 0
        for j in range(i):
            if rocks[j] < rocks[i] and cnt_list[max_idx] <= cnt_list[j]:
                max_idx = j
                cnt_list[i] = cnt_list[max_idx] + 1
    print(max(cnt_list))
