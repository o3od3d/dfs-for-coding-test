"""
바이러스에 걸리면 연결된 모든 컴퓨터는 바이러스에 걸린다.
바이러스에 걸리는 컴퓨터의 수는?

1. 아이디어
 - for문 => 바이러스와 연결된 컴퓨터의 수 출력

2. 시간복잡도
 - O(V+E)
 - V : 100
 - E : 2V

3. 자료구조
 - 그래프 : INT[]
 - 방문 : bool[]
"""
num = int(input())
pair = int(input())
board = [[] for _ in range(num+1)]
for _ in range(pair):
    i,j = map(int,input().split())
    board[i].append(j)
    board[j].append(i)
visited = [False] * (num+1)

def dfs(virus):
    global cnt
    visited[virus] = True
    for v in board[virus]:
        if not visited[v]:
            dfs(v)
            cnt += 1
cnt = 0
dfs(1)
print(cnt)