m, n = map(int, input().split())
num_of_bus = int(input())
bus_info = {}
for _ in range(num_of_bus):
    temp = list(map(int, input().split()))
    bus_info[temp[0]] = [[min(temp[1], temp[3]), min(temp[2], temp[4])], [max(temp[1], temp[3]), max(temp[2], temp[4])]]
sx, sy, dx, dy = map(int, input().split())
graph = [[] for _ in range(num_of_bus + 1)]
check = [False] * (num_of_bus + 1)
# Find Bigger Bus Line
def find():
    for i in range(1, num_of_bus+1):
        temp = False
        x1, y1 = bus_info[i][0]
        x2, y2 = bus_info[i][1]
        for j in range(1, num_of_bus+1):
            if i != j :
                x3, y3 = bus_info[j][0]
                x4, y4 = bus_info[j][1]
                if x1 == x2 == x3 == x4 :
                    if y3 <= y1 <= y2 <= y4 :
                        temp = True
                if y1 == y2 == y3 == y4 :
                    if x3 <= x1 <= x2 <= x4 :
                        temp = True
        check[i] = temp
    for i in range(1, num_of_bus+1):
        if check[i] :
            continue
        x1, y1 = bus_info[i][0]
        x2, y2 = bus_info[i][1]
        for j in range(1, num_of_bus + 1):
            if check[j] : continue
            if i == j : continue
            x3, y3 = bus_info[j][0]
            x4, y4 = bus_info[j][1]
            if x1 <= x3 <= x2 and x1 <= x3 <= x2:
                if y3 <= y1 <= y4 and y3 <= y2 <= y4:
                    graph[i].append(j)
                    graph[j].append(i)
            # 한 점 혹은 겹치는 경우 (수평 방향)
            if y1 == y2 == y3 == y4:
                if not (x1 > x4 or x2 < x3):
                    graph[i].append(j)
                    graph[j].append(i)
            # 한 점 혹은 겹치는 경우 (수직 방향)
            if x1 == x2 == x3 == x4:
                if not (y1 > y4 or y2 < y3):
                    graph[i].append(j)
                    graph[j].append(i)
    return

def bfs():
    q = []
    a = []
    find()
    for i in range(1, num_of_bus+1):
        if check[i] :
            continue
        x1, y1 = bus_info[i][0]
        x2, y2 = bus_info[i][1]
        if x1 <= sx <= x2 and y1 <= sy <= y2 :
            q.append(i)
        if x1 <= dx <= x2 and y1 <= dy <= y2 :
            a.append(i)
    minValue = 1e9
    visited = [-1 for _ in range(num_of_bus + 1)]
    real_q = []
    for i in q :
        real_q.append(i)
        visited[i] = 0
    while real_q :
        x = real_q[0]
        del real_q[0]
        for i in graph[x]:
            if visited[i] == -1:
                visited[i] = visited[x] + 1
                real_q.append(i)
    for i in a :
        minValue = min(visited[i], minValue)
    return minValue+1

print(bfs())