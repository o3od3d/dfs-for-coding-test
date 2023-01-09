"""
섬의 개수 세기
가로세로대각선
1. 아이디어
 - 2중 FOR문 => 방문 X && 값 1
 - 섬의 개수 구하기

2. 시간복잡도
 - O(V+e) = 7V ~= 2500 < 2억
 - V : 50 * 50
 - E : 6V

3. 자료구조
 - 그래프 : INT[][]
 - 방문 : BOOL[][]
"""
direction = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[-1,-1],[1,-1]]
def dfs(x,y):
    visited[x][y] = True
    for dir in direction:
        nx = x + dir[0]
        ny = y + dir[1]
        if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx,ny)
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    board = [list(map(int,input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                cnt += 1
                dfs(i,j)
    print(cnt)
