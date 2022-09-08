n, m = map(int, input().split())
queen = list(map(int, input().split())) # 2
knight = list(map(int, input().split())) # 3
pawn = list(map(int, input().split())) # 4

board = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

# 상, 상우, 우, 우하, 하, 하좌, 좌, 좌상
# 0,  1,    2,  3,   4,  5,    6,  7
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
q_path = [[0, 2, 4, 6], [1, 3, 5, 7]]
# [상, 상우], [우, 상우], [우, 우하], [하, 우하], [하, 하좌], [좌, 하좌], [좌, 좌상], [상, 좌상]
k_path = [[0, 1], [2, 1], [2, 3], [4, 3], [4, 5], [6, 5], [6, 7], [0, 7]]

def bfs():
    # Setting
    q = []
    if queen[0] != 0 :
        for i in range(1, len(queen) - 1, 2):
            x, y = queen[i] -1, queen[i + 1] -1
            q.append([x, y, 2])
            board[x][y] = 2
            visited[x][y] = True
    if knight[0] != 0 :
        for i in range(1, len(knight) - 1, 2):
            x, y = knight[i] - 1, knight[i + 1] - 1
            q.append([x, y, 3])
            board[x][y] = 3
            visited[x][y] = True
    if pawn[0] != 0 :
        for i in range(1, len(pawn) - 1, 2) :
            x, y = pawn[i] - 1, pawn[i + 1] - 1
            board[x][y] = 4
            visited[x][y] = True

    while q :
        x, y, piece = q[0]
        del q[0]
        if piece == 2 :
            for i in q_path :
                for d in i :
                    k = 1
                    check = True
                    while True :
                        nx = x + k * dx[d]
                        ny = y + k * dy[d]
                        if 0 <= nx < n and 0 <= ny < m :
                            if board[nx][ny] == 0 and not visited[nx][ny]:
                                board[nx][ny] = 1
                                k += 1
                                check = True
                            elif board[nx][ny] == 1 :
                                k += 1
                                check = True
                            else :
                                check = False
                        else : check = False
                        if not check : break
        if piece == 3 :
            for i in k_path :
                nx = x + dx[i[0]] + dx[i[1]]
                ny = y + dy[i[0]] + dy[i[1]]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                    if board[nx][ny] == 0 :
                        visited[nx][ny] = True
                        board[nx][ny] = 1
    result = 0
    for i in range(n):
        result += board[i].count(0)
    return result

print(bfs())