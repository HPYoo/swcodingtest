N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
L_info = list(map(int, input().split()))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate(arr):
    temp = [[] for _ in range(len(arr))]
    for row in range(len(arr)-1, -1, -1):
        for col in range(len(arr[row])-1, -1, -1) :
            temp[col].append(arr[row][col])
    return temp

def diminish():
    temp = []
    for i in range(2**N):
        for j in range(2**N):
            x, y = i, j
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and board[nx][ny] > 0 :
                    cnt += 1
            if cnt < 3 :
                temp.append([x, y])
    while temp :
        x, y = temp[0]
        del temp[0]
        if board[x][y] > 0 :
            board[x][y] -= 1

def bfs():
    # 가장 큰 덩어리 찾기
    visited = [[False for _ in range(2**N)] for _ in range(2**N)]
    maxValue = 0
    for i in range(2**N):
        for j in range(2**N):
            if board[i][j] > 0 and not visited[i][j] :
                q = [[i, j]]
                visited[i][j] = True
                cnt = 1
                while q :
                    x, y = q[0]
                    del q[0]
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and not visited[nx][ny] :
                            if board[nx][ny] > 0 :
                                cnt += 1
                                visited[nx][ny] = True
                                q.append([nx, ny])
                maxValue = max(maxValue, cnt)
    return maxValue

def solve():
    it = 0
    while it < Q :
        L = L_info[it]
        rot_arr = []
        for i in range(0, 2**N, 2**L):
            temp_arr = board[i : i + 2**L]
            for j in range(0, 2**N, 2**L) :
                for k in temp_arr :
                    rot_arr.append(k[j : j + 2**L])
                x0, x1, y0, y1 = int(i), int(i + 2**L), int(j), int(j + 2**L)
                rot_arr = rotate(rot_arr)
                ix, iy = 0, 0
                for xxx in range(x0, x1):
                    iy = 0
                    for yyy in range(y0, y1):
                        board[xxx][yyy] = rot_arr[ix][iy]
                        iy += 1
                    ix += 1
                    if ix >= abs(x1 - x0) : ix = 0
                rot_arr = []
        diminish()
        it += 1
    total = 0
    for i in range(2**N):
        total += sum(board[i])
    result = bfs()
    print(total)
    print(result)
solve()