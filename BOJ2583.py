"""
1. 아이디어
 - 주어진 직사각형 나타내기 =>1 로표현
 - 2 중 FOR문 => 값 0 && 방문 X
 - DFS통해 찾은 값 저장 후 정렬하여 출력

2. 시간복잡도
 - O(V+E)
 - V : 100 * 100
 - E : 4V

3. 자료구조
 - 그래프 : INT[][]
 - 방문여부 : BOOL[][]
 - 결과 : INT[][]
"""
M,N,K = map(int,input().split())
square = [list(map(int,input().split())) for _ in range(K)]
board = [[0] * N for _ in range(N)]
for s in range(K):
    for i in range(4-square[s][1],5-square[s][3],-1):
        for j in range(square[s][0],square[s][2]):
            board[i][j] = 1
direction = [[0,1],[0,-1],[1,0],[-1,0]]
visited = [[False] * N for _ in range(M)]
result = []

def dfs(x,y):
    global cnt
    cnt += 1
    for dir in direction:
        nx = x + dir[0]
        ny = y + dir[1]
        if 0 <= nx < M and 0 <= ny < N:
            if board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny)
print(board)
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and not visited[i][j]:
            cnt = 0
            visited[i][j] = True
            dfs(i,j)
            result.append(cnt)

print(len(result))
print(result,end="")
