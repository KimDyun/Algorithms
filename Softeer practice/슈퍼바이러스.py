import sys

"""
    단순히 K * P^(N*10)을 하면 O(N)의 시간 복잡도를 가지지만
    2배씩 나누어 연산을 수행하는 재귀함수를 응용하면 O(logN)의 시간복잡도를 가진다.
"""

def f(p, n):
    if n == 1:
        return p
    elif n % 2 == 0:
        r = f(p, n/2)
        return r*r % 1000000007
    else:
        r = f(p, (n-1)/2)
        return r*r*p % 1000000007
if __name__ == "__main__":
    K, P, N = map(int, sys.stdin.readline().split())
    N = N*10
    result = f(P, N)
    print(K * result % 1000000007)