"""
12
1 2 3
1 3 2
2 4 5
3 5 11
3 6 9
4 7 1
4 8 7
5 9 15
5 10 4
6 11 6
6 12 10
"""
from collections import deque


n = int(input())
tree = [[] for _ in range(n + 1)]

graph = [list(map(int, input().split())) for _ in range(n - 1)]



