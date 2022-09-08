board = [list(map(int, input().split())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    arr = []
    for i in range(5):
        for j in range(5):
            q = [[i, j, 1, str(board[i][j])]]
            while q :
                x, y, cnt, string = q[0]
                del q[0]
                if cnt == 6 :
                    if string in arr :
                        continue
                    else :
                        arr.append(string)
                        continue
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < 5 and 0 <= ny < 5 :
                        q.append([nx, ny, cnt + 1, string + str(board[nx][ny])])
    return arr

result = bfs()
print(len(result))
