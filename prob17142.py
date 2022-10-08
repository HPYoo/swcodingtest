N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
info = []
empty_cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(N):
        if board[i][j] == 2 :
            info.append([i, j])
        if board[i][j] == 0 :
            empty_cnt += 1

def combination(arr, t):
    result = []
    if t == 0 : return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1 : ]
        for C in combination(rest_arr, t-1):
            result.append([elem] + C)
    return result

def bfs():
    res = 1e9
    comb = combination(info, M)
    for temp in comb :
        q = temp
        visited = [[False for _ in range(N)] for _ in range(N)]
        for x, y in temp :
            visited[x][y] = True
        time = 0
        num_zero = empty_cnt
        while True :
            size = len(q)
            if size == 0 or num_zero == 0 :
                if num_zero == 0 :
                    break
                else :
                    time = 1e9
                    break
            time += 1
            for _ in range(size):
                x, y = q[0]
                del q[0]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N :
                        if not visited[nx][ny] :
                            if board[nx][ny] == 2 : # 감염은 동시다발적
                                q.append([nx, ny])
                                visited[nx][ny] = True
                            elif board[nx][ny] == 0 :
                                visited[nx][ny] = True
                                q.append([nx, ny])
                                num_zero -= 1
        res = min(res, time)

    if res == 1e9 : print(-1)
    else : print(res)

bfs()