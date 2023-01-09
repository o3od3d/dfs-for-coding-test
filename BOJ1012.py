"""
배추흰지렁이는 인접한 배추로 이동가능
서로 인접한 배추 몇 군데 퍼져있는지 조사하여 필요한 지렁이 갯수구하기

1. 아이디어
 - 2 중 for문 => 값 1 && 방문x
 - 각 테스트 케이스마다 구하기

2. 시간복잡도
 - O(V+E)
 - V : 50 * 50
 - E : 4V

3. 자료구조
 - 그래프 : INT[][]
 - 방문 : BOOL[][]

"""
test = int(input())
direction = [[0,1],[0,-1],[1,0],[-1,0]]
import sys
sys.setrecursionlimit(10**7)
def dfs(x,y):
    visited[x][y] = True
    for dir in direction:
        nx = x + dir[0]
        ny = y + dir[1]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny)

for _ in range(test):
    M,N,K = map(int,input().split())
    board = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for k in range(K):
        i,j = map(int,input().split())
        board[j][i] = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)

