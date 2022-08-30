words = []
for i in range(6) :
    temp = input()
    words.append(temp)

def permutation(arr, t):
    result = []
    if t == 0 :
        return [[]]
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[:i] + arr[i + 1:]
        for P in permutation(rest_arr, t - 1) :
            result += [[elem] + P]
    return result

permut = permutation(words, 3)

# 3개를 배치 해본다.
# 단어가 있는지 써치
# 안되면 탈락
def solve():
    answer_board = []
    while permut :
        x, y, z = permut[0]
        del permut[0]
        board = [x, y, z]
        # 행 기준으로 words 제거
        temp = words.copy()
        cnt = 6
        check = True
        for i in range(3):
            if board[i] in temp :
                temp[temp.index(board[i])] = True
                cnt -= 1
            else :
                check = False
        if check :
            for i in range(3):
                char = board[0][i] + board[1][i] + board[2][i]
                if char in temp :
                    temp[temp.index(char)] = True
                    cnt -= 1
                else :
                    check = False
        if check and cnt == 0 and temp.count(True) == 6:
            answer_board.append([board[0] + board[1] + board[2]])
    return answer_board

result = solve()
result.sort()

if not result :
    print(0)
else :
    for i in range(0, 9, 3):
        print(result[0][0][i] + result[0][0][i+1] + result[0][0][i+2])

