r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
r, c, k = r - 1, c - 1, k
def check(arr):
    num_row = len(arr)
    num_col = len(arr[0])
    if num_row >= num_col : return 'R'
    else : return 'C'

def calc_R(arr):
    new_arr = []
    max_row = 0
    for i in range(len(arr)):
        temp = arr[i]
        max_num = max(arr[i])
        info = {}
        for j in range(1, max_num+1):
            if temp.count(j) != 0 :
                info[j] = temp.count(j)
        # info [1] 기준으로 정렬하자
        size = len(info)
        temp_list = []
        num = 1
        while size:
            for j in info :
                if info[j] == num :
                    temp_list.append(j)
                    temp_list.append(num)
                    size -= 1
            num += 1
        max_row = max(max_row, len(temp_list))
        new_arr.append(temp_list)
    for i in range(len(new_arr)):
        if len(new_arr[i]) < max_row :
            while True :
                new_arr[i].append(0)
                if len(new_arr[i]) == max_row : break
    return new_arr

def calc_C(arr):
    temp_arr = []
    # 90도 회전시키자
    temp = []
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            temp.append(arr[i][j])
        temp_arr.append(temp)
        temp = []
    temp_arr = calc_R(temp_arr)
    # 다시 뒤집어주자
    num_r = len(temp_arr[0])
    num_c = len(temp_arr)
    new_arr = [[] for _ in range(num_r)]
    for i in range(num_c):
        temp = temp_arr[i]
        for j in range(num_r):
            new_arr[j].append(temp[j])
    return new_arr

def solve(arr):
    time = 0
    while True :
        if 0 <= r < len(arr) and 0 <= c < len(arr[0]) :
            if arr[r][c] == k:
                break
        calc = check(arr)
        if calc == 'R' : arr = calc_R(arr)
        else : arr = calc_C(arr)
        # size check
        size_row = len(arr)
        size_col = len(arr[0])
        if size_row > 100 :
            arr = arr[:100]
        if size_col > 100 :
            temp = []
            for b in range(100):
                temp.append(arr[b][:100])
            arr = temp.copy()
        time += 1
        if time > 100 : break
    if time > 100 :
        print(-1)
    else :
        print(time)
solve(board)