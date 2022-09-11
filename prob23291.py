N, K = map(int, input().split())
# 가장 많은 것과 적은 것이 K 차이가 되어야함.
board = list(map(int, input().split()))
# Ex) arr = [5, 2, 3, 14, 9, 2, 11, 8]
# 1 단계 : 물고기 집어넣기
def put_fish(arr):
    minValue = min(arr)
    for i in range(len(arr)):
        if arr[i] == minValue :
            arr[i] += 1
    return arr

# 2 단계 : 어항 쌓기
def pile(arr):
    temp = [[arr[0]]]
    del arr[0]
    temp.append(arr)
    return temp

# 3 단계 : 2개 이상 쌓여있는 어항을 모두 떼어서 시계 방향으로 90도 회전
def rotate(arr):
    while True :
        temp = []
        minValue = len(arr) + 1
        for i in range(len(arr)):
            minValue = min(minValue, len(arr[i])) # Column
        if len(arr) > len(arr[-1]) - minValue : break
        for j in range(minValue): # Column
            sample = []
            for i in range(len(arr)-1, -1, -1): # Row
                sample.append(arr[i][j])
            temp.append(sample)
        temp.append(arr[-1][minValue : ])
        arr = temp.copy()
    return arr

# 4단계 물고기 수 조절하기
def arrangement(arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = []
    for i in range(len(arr)):
        for j in range(len(arr[i])) :
            x, y = i, j
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < len(arr) and 0 <= ny < len(arr[i]) :
                    try :
                        diff = abs(arr[x][y] - arr[nx][ny]) // 5
                        if arr[nx][ny] > arr[x][y] :
                            temp.append([x, y, diff])
                            temp.append([nx, ny, -diff])
                    except : continue
    for x, y, diff in temp :
        arr[x][y] += diff
    return arr

# 5단계 : 다시 눕히자
def rescale(arr):
    temp = []
    for j in range(len(arr[-1])) :
        for i in range(len(arr) -1, -1, -1):
            try :
                temp.append(arr[i][j])
            except : continue
    return temp

def rotate2(arr):
    size = int(len(arr)/2)
    temp = [[arr[i] for i in range(size-1, -1, -1)], arr[size : ]]
    size //= 2
    new_array = []
    for j in range(len(temp)-1, -1, -1):
        sample = []
        for i in range(size -1, -1, -1):
            sample.append(temp[j][i])
        new_array.append(sample)
    new_temp = []
    for i in range(len(temp)):
        new_temp.append(temp[i][size : ])
    new_array += new_temp
    return new_array

def solve():
    it = 0
    array = board.copy()
    while True :
        if max(array) - min(array) <= K : break
        array = put_fish(array)
        array = pile(array)
        array = rotate(array)
        array = arrangement(array)
        array = rescale(array)
        array = rotate2(array)
        array = arrangement(array)
        array = rescale(array)
        it += 1
    return it

print(solve())