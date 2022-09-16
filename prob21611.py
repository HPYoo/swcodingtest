N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
b_info = [list(map(int, input().split())) for _ in range(M)]
# None, 상, 하, 좌, 우
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# blizzard
def blizzard(di, si, arr):
    x, y = int(N/2), int(N/2)
    for i in range(si):
        nx = x + dx[di]
        ny = y + dy[di]
        arr[nx][ny] = 0
        x, y = nx, ny
    return arr
# Make 1D Array
def twotoone(arr):
    temp_vec = []
    sx, sy = int(N/2), int(N/2)
    sdx = [0, 1, 0, -1]
    sdy = [-1, 0, 1, 0]
    q = [[sx, sy]]
    cnt = 0
    d = 0
    k = 1
    while q :
        x, y = q[0]
        del q[0]
        for _ in range(k):
            nx = x + sdx[d]
            ny = y + sdy[d]
            if 0 <= nx < N and 0 <= ny < N :
                temp_vec.append(arr[nx][ny])
                x, y = nx, ny
        if k == N : break
        q.append([x, y])
        cnt += 1
        d = (d + 1) % 4
        if cnt == 2 :
            k += 1
            cnt = 0
    return temp_vec

def onetotwo(arr):
    temp_arr = [[0 for _ in range(N)] for _ in range(N)]
    sx, sy = int(N/2), int(N/2)
    sdx = [0, 1, 0, -1]
    sdy = [-1, 0, 1, 0]
    q = [[sx, sy]]
    cnt = 0
    d = 0
    k = 1
    it = 0
    while q :
        x, y = q[0]
        del q[0]
        for _ in range(k):
            nx = x + sdx[d]
            ny = y + sdy[d]
            if 0 <= nx < N and 0 <= ny < N :
                temp_arr[nx][ny] = arr[it]
                it += 1
                x, y = nx, ny
        if k == N : break
        q.append([x, y])
        cnt += 1
        d = (d + 1) % 4
        if cnt == 2 :
            k += 1
            cnt = 0
    return temp_arr

# Pull Marble
def pulling(arr):
    temp = []
    for i in range(len(arr)):
        if arr[i] != 0 :
            temp.append(arr[i])
    if len(arr) != len(temp):
        for i in range(len(arr) - len(temp)) :
            temp.append(0)
    return temp

# Explosion # 반복
def explosion(arr):
    info = []
    x = arr[0]
    cnt = 1
    num_list = [0, 0, 0]
    while True :
        for i in range(1, len(arr)):
            if x == arr[i] and x != 0 :
                cnt += 1
            elif x != arr[i] :
                if cnt >= 4 :
                    for j in range(i - 1, i - cnt -1, -1):
                        arr[j] = 0
                    info.append([i - cnt - 1, i - 1])
                    num_list[x-1] += cnt
                    cnt = 1
                    x = arr[i]
                else :
                    cnt = 1
                    x = arr[i]
        if info :
            info = []
            arr = pulling(arr)
            x = arr[0]
        else :
            break
    return arr, num_list

def rearrange(arr):
    cnt = 1
    x = arr[0]
    temp = []
    for i in range(1, len(arr)):
        if x == arr[i] and x != 0 :
            cnt += 1
        if x != arr[i] :
            temp.append(cnt)
            temp.append(x)
            x = arr[i]
            cnt = 1
    if len(arr) != len(temp):
        for i in range(len(arr) - len(temp)):
            temp.append(0)
    return temp

def solve():
    m_it = 0
    num1, num2, num3 = 0, 0, 0
    temp_arr = [[x for x in y] for y in board]
    while m_it < M :
        temp_arr = blizzard(b_info[m_it][0], b_info[m_it][1], temp_arr)
        temp_arr = twotoone(temp_arr)
        temp_arr = pulling(temp_arr)
        temp_arr, num_list = explosion(temp_arr)
        num1 += num_list[0]
        num2 += num_list[1]
        num3 += num_list[2]
        temp_arr = rearrange(temp_arr)
        temp_arr = onetotwo(temp_arr)
        m_it += 1
    return [num1, num2, num3]

result = solve()
print(1 * result[0] + 2 * result[1] + 3 * result[2])


