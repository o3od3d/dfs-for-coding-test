"""
1. 아이디어
 - 2 중 for문 => 값 1 && 방문 x
 - dfs통해 찾은 값 저장 후 정렬해서 출력

2. 시간복잡도
 - O (V+E) < 2억 가능
 - V: 25 * 25
 - E : 4V

3. 자료구조
 - 그래프 : int[][]
 - 방문여부 : int[][]

"""

n = int(input())
board = [list(map(int,input().strip())) for _ in range(n)]
direction = [[0,1],[0,-1],[1,0],[-1,0]]
result = []
visited = [[False] * n for _ in range(n)]
# 총 단지수 출력, 각 단지내 집 수 오름 순 정렬한줄에 하나씩

def dfs(x,y):
    global cnt
    cnt += 1
    for dir in direction:
        nx = x + dir[0]
        ny = y + dir[1]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            cnt = 0
            visited[i][j] = True
            # dfs로 크기 구하기
            dfs(i,j)
            # 크기 결과 리스트에 넣기
            result.append(cnt)

result.sort()
print(len(result))
for r in result:
    print(r)