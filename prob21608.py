N = int(input())
info_dict = {}
order_list = []
board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N**2):
    tmp = list(map(int, input().split()))
    info_dict[tmp[0]] = tmp[1:]
    order_list.append(tmp[0])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(ns):
    # 0 : like_cnt, 1 : empty_cnt
    like_info = {0 : [], 1: [], 2:[], 3:[], 4:[]}
    empty_info = {0 : [], 1: [], 2:[], 3:[], 4:[]}
    for i in range(N):
        for j in range(N):
            x, y = i, j
            if board[x][y] != 0 : continue
            like_cnt, empty_cnt = 0, 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N :
                    if board[nx][ny] in info_dict[ns] : like_cnt += 1
            like_info[like_cnt].append([x, y])
    for k in range(4, -1, -1):
        if len(like_info[k]) == 1 :
            x, y = like_info[k][0]
            board[x][y] = ns
            break
        elif len(like_info[k]) > 1 :
            like_info[k].sort()
            for it in range(len(like_info[k])):
                x, y = like_info[k][it]
                empty_cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N :
                        if board[nx][ny] == 0 : empty_cnt += 1
                empty_info[empty_cnt].append([x, y])
            for empty in range(4, -1, -1):
                if empty_info[empty] :
                    empty_info[empty].sort()
                    x, y = empty_info[empty][0]
                    board[x][y] = ns
                    break
            break
def scoring():
    global score
    s_list = [0, 1, 10, 100, 1000]
    for i in range(N):
        for j in range(N):
            x, y = i, j
            student = board[x][y]
            cnt = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N :
                    if board[nx][ny] in info_dict[student] : cnt += 1
            score += s_list[cnt]

def solve():
    for st in range(N**2):
        search(order_list[st])
    scoring()

score = 0
solve()
print(score)