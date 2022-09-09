from collections import deque
board = [list(map(str, input())) for _ in range(5)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def combination(arr, t):
    result = []
    if t == 0 : return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1 : ]
        for C in combination(rest_arr, t - 1):
            temp = [elem] + C
            if len(temp) >= 4 :
                cnt = 0
                for k in range(len(temp)):
                    if board[temp[k][0]][temp[k][1]] == 'Y' : cnt += 1
                if cnt >= 4 : continue
            result.append([elem] + C)
    return result
info = []
for i in range(5):
    for j in range(5):
        info.append([i, j])

comb = deque(combination(info, 7))

def bfs():
    result = 0
    while comb :
        temp = comb.popleft()
        visited = [False for _ in range(7)]
        q = deque([temp[0]])
        visited[0] = True
        while q :
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 5 and 0 <= nx < 5 :
                    if [nx, ny] in temp :
                        idx = temp.index([nx, ny])
                        if not visited[idx] :
                            visited[idx] = True
                            q.append([nx, ny])
        if False not in visited :
            result += 1
    return result

print(bfs())