f = open("./dijkstraData.txt")
N = 200
inf = 1000000

graph = [[] for dummy in range(N)]

for row in f:
    temp = row.strip().split('\t')
    temp_node = int(temp[0]) - 1
    for i in range(1,len(temp)):
        temp_str = temp[i].strip().split(',')
        graph[temp_node].append((int(temp_str[0].strip()) - 1, int(temp_str[1].strip())))


X = []
X.append(0)
A = {}
A[0] = 0

while(len(X) < len(graph)):
    temp_min = -1
    v_star = -1
    w_star = -1
    len_star = -1
    for item in X:
        for r in graph[item]:
            temp_node = r[0]
            temp_len = r[1]
            if(temp_node not in X):
                if((temp_min < 0) or ((A.get(item,inf) + temp_len) < temp_min)):
                    temp_min = (A.get(item,inf) + temp_len)
                    v_star = item
                    len_star = temp_len
                    w_star = temp_node
    X.append(w_star)
    A[w_star] = A[v_star] + len_star

test_cases = [7,37,59,82,99,115,133,165,188,197]
for i in test_cases:
    print A.get(i-1,1000000)
