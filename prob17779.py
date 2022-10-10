N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
nboard = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 1e9

def make5(x, y, d1, d2):
    s_point = [[x, y], [x, y], [x + d1, y - d1], [x+d2, y +d2]]
    e_point = [[x + d1, y - d1], [x + d2, y + d2], [x+d1+d2, y-d1+d2], [x+d2+d1, y+d2-d1]]
    nd = [[1, 1, 1, 1], [-1, 1, 1, -1]]
    for i, (x, y) in enumerate(s_point) :
        board[x][y] = 5
        while True :
            x += nd[0][i]
            y += nd[1][i]
            board[x][y] = 5
            if [x, y] == e_point[i] : break
    for i in range(N):
        temp = board[i]
        cnt = temp.count(5)
        if cnt == 2 :
            first = temp.index(5)
            second = temp[first + 1 : ].index(5) + first
            for j in range(first + 1, second+1) :
                board[i][j] = 5

def divide(x, y, d1, d2):
    for i in range(N):
        for j in range(N):
            if 0 <= i < x + d1 and 0 <= j <= y  and board[i][j] != 5:
                board[i][j] = 1
            elif 0 <= i <= x + d2 and y < j <= N - 1 and board[i][j] != 5:
                board[i][j] = 2
            elif x + d1 <= i <= N - 1 and 0 <= j < y - d1 + d2 and board[i][j] != 5:
                board[i][j] = 3
            elif x + d2 < i <= N - 1 and y - d1 + d2 <= j <= N - 1 and board[i][j] != 5:
                board[i][j] = 4

def bfs(): # Derive Population of each area
    global result
    visited = [[False for _ in range(N)] for _ in range(N)]
    area_list = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] :
                area = board[i][j]
                x, y = i, j
                cnt = nboard[i][j]
                q = [[x, y]]
                visited[x][y] = True
                while q :
                    x, y = q[0]
                    del q[0]
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == area:
                            visited[nx][ny] = True
                            q.append([nx, ny])
                            cnt += nboard[nx][ny]
                area_list.append(cnt)
    result = min(max(area_list) - min(area_list), result)

def solve():
    for ii in range(N):
        for jj in range(N):
            x, y = ii , jj
            for dd1 in range(1, N):
                for dd2 in range(1, N - dd1):
                    if 0 <= x < x + dd1 + dd2 < N and 0 <= y - dd1 < y < y + dd2 < N :
                        make5(x, y, dd1, dd2)
                        divide(x, y, dd1, dd2)
                        bfs()
                    for iii in range(N):
                        for jjj in range(N):
                            board[iii][jjj] = 0

solve()
print(result)