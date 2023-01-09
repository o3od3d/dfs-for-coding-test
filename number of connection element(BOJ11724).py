"""
방향 없는 그래프가 주어졌을 때, 연결 요소 개수 구하기

1. 아이디어
 - 방문하지 않은 요소 방문

2. 시간복잡도
 - O(V+E)
 - V : 1000
 - E : 499500

3. 자료구조
 - 그래프 : INT[]
 - 방문 : INT[]
"""
import sys
sys.setrecursionlimit(10**7)
N,M = map(int,input().split())
board = [[] for _ in range(N+1)]
for _ in range(M):
    i,j = map(int,input().split())
    board[i].append(j)
    board[j].append(i)
visited = [False] * (N+1)

def dfs(vertex):
    visited[vertex] = True
    for v in board[vertex]:
        if not visited[v]:
            dfs(v)
ans = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans)