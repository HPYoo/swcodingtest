m, n = map(int, input().split())
num_of_bus = int(input())
bus_info = {}
for _ in range(num_of_bus):
    temp = list(map(int, input().split()))
    bus_info[temp[0]] = [[temp[1], temp[2]], [temp[3], temp[4]]]
sx, sy, dx, dy = map(int, input().split())
graph = [[]]
bus_line = []
for i in range(num_of_bus):
    temp = []
    x1, y1 = bus_info[i+1][0]
    x2, y2 = bus_info[i+1][1]
    if abs(x1 - x2) >= 1 and y1 == y2 :
        for k in range(min(x1, x2), max(x1, x2) + 1):
            temp.append([k, y1])
    else :
        for k in range(min(y1, y2), max(y1, y2), +1):
            temp.append([x1, k])
    bus_line.append(temp)

# Make Graph
for i in range(num_of_bus):
    temp = bus_line[i]
    bus_list = []
    for j in range(num_of_bus):
        if i != j :
            for k in range(len(temp)):
                if temp[k] in bus_line[j] and j + 1 not in bus_list :
                    # print(i+1, 'Connected With', j+1)
                    bus_list.append(j + 1)
    bus_list.sort()
    graph.append(bus_list)

def bfs():
    q = []
    a = []
    for i in range(num_of_bus):
        for j in range(len(bus_line[i])):
            if [sx, sy] == bus_line[i][j] :
                q.append([i+1, 1])
            if [dx, dy] == bus_line[i][j] :
                a.append(i+1)
    minValue = 1e9
    while q :
        visited = [False for _ in range(num_of_bus + 1)]
        qq = [q[0]]
        del q[0]
        visited[qq[0][0]] = True
        while qq :
            x, cnt = qq[0]
            del qq[0]
            if x in a :
                minValue = min(minValue, cnt)
            for i in graph[x]:
                if not visited[i] :
                    visited[i] = True
                    qq.append([i, cnt + 1])
    return minValue

print(bfs())
