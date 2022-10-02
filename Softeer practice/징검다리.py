import sys

"""
    높은 돌을 최대한 많이 밟는 경우의 수를 구할 때 1차원 리스트에 돌의 높이가 저장된다.
    이 때 중간에 높은 돌을 밟았다가 낮은 돌이 나왔을 경우, 그 이후에 다시 높은 돌이 나올 수 있다.
    예를 들어, N = 9, 돌의 높이 리스트 rocks = [7, 6, 1, 2, 3, 2, 3, 4, 5]가 있을 때
    결과 값은 5, 밟은 돌들의 인덱스는 [2, 3, 4, 7, 8], 이에 상응하는 돌의 높이는 [1,2,3,4,5]가 된다.
    따라서 K번째 돌을 밟으려 할 때 K-1번째 돌까지 다시 탐색 해주어야 하며, O(N^2)의 시간복잡도를 갖는 이중 반복문으로 문제를 풀 수 있다.
"""

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
