"""
R,G,B = 빨,초,파
같은 색상이 상하좌우로 인접해 있는 경우 두 글자는 같은 구역에 속함
적록색약 아닌 사람과 적록색약인 사람이 보는 구역의 개수 공백 출력

1. 아이디어
 - 2 중 FOR문 => 같은 색 (적록색약과 아닌 경우 2가지)

2. 시간복잡도
 - O (V+e)
 - V : 100 * 100
 - E : 4V

3. 자료구조
 - 그래프 : STR[][]
 - 방문 : BOOL[][]
 - 방문 : BOOL[][]

"""
import sys
sys.setrecursionlimit(10**7)
n = int(input())
board = [list(map(str,input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]

result = [0,0]

def dfs(x,y,color,color2,visit):
    visit[x][y] = True
    for dir in direction:
        ni = x + dir[0]
        nj = y + dir[1]
        if 0 <= ni < n and 0 <= nj < n:
            if (board[ni][nj] == color or board[ni][nj] == color2) and not visit[ni][nj]:
                dfs(ni,nj,color,color2,visit)


for i in range(n):
    for j in range(n):
        if (board[i][j] == 'R' or board[i][j] == 'G') and not visited[i][j]:
            result[0] += 1
            dfs(i,j,'R','G',visited)
        elif board[i][j] == 'B' and not visited[i][j]:
            result[0] += 1
            dfs(i,j,'B','B',visited)
        if board[i][j] == 'R' and not visited2[i][j]:
            result[1] += 1
            dfs(i,j,'R','R',visited2)
        elif board[i][j] == 'B' and not visited2[i][j]:
            result[1] += 1
            dfs(i,j,'B','B',visited2)
        elif board[i][j] == 'G' and not visited2[i][j]:
            result[1] += 1
            dfs(i,j,'G','G',visited2)

print(result[1],result[0])


