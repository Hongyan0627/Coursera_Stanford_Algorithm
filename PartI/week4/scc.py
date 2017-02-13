
# read file, create graphs
f = open("./SCC.txt")
N = 875714
graph = {}
graph_reverse = {}

for i in range(N):
    graph[i] = []
    graph_reverse[i] = []

for row in f:
    temp = row.strip().split(' ')
    num1 = int(temp[0]) - 1;
    num2 = int(temp[1]) - 1;
    graph[num1].append(num2)
    graph_reverse[num2].append(num1)

# first DFS, using stack
visited = [0 for dummy in range(N)]
order = [-1 for dummy in range(N)]
t = 0
my_stack = []
for node in range(N-1,-1,-1):
    if(visited[node] != 0):
        continue
    my_stack.append(node)
    while(len(my_stack) > 0):
        temp_node = my_stack.pop()
        if(visited[temp_node] == 1):
            order[t] = temp_node
            #order[temp_node] = t
            visited[temp_node] = 2
            t += 1
        elif(visited[temp_node] == 0):
            visited[temp_node] = 1
            my_stack.append(temp_node)
            for item in graph_reverse[temp_node]:
                my_stack.append(item)
        else:
            pass

#second DFS, using stack
leaders = {}
visited2 = [0 for dummy in range(N)]
s = 0
my_stack2 = []
for k in range(N):
    node = order[N - k - 1]
    if(visited2[node] != 0):
        continue

    s = node
    my_stack2.append(node)
    while(len(my_stack2) > 0):
        temp_node = my_stack2.pop()
        if(visited2[temp_node] == 0):
            visited2[temp_node] = 1
            leaders[s] = leaders.get(s,0) + 1
            for item in graph[temp_node]:
                my_stack2.append(item)
        else:
            pass

#print the result
print sorted(leaders.values(),reverse=True)[0:5]

###################################################
# recursive version, not good for python
###################################################
# def DFS_first(i):
#     global t,visited,graph_reverse,order
#     visited[i] = 1
#     if (len(graph_reverse[i]) > 0):
#         for item in graph_reverse[i]:
#             if (visited[item] == 0):
#                 DFS_first(item)
#     order[t] = i
#     t += 1
    
# for node in range(N-1,-1,-1):
#     if (visited[node] == 0):
#         DFS_first(node)



# leaders = [-1 for dummy in range(N)]
# visited = [0 for dummy in range(N)]
# s = 0

# def DFS_second(i):
#     global s,graph,visited
#     visited[i] = 1
#     leaders[i] = s
#     for item in graph[i]:
#         if (visited[item] == 0):
#             DFS_second(item)

# for k in range(N):
#     node = order[N - 1 - k]
#     if (visited[node] == 0):
#         s = node
#         DFS_second(node)

# scc = {}
# for leader in leaders:
#     scc[leader] = scc.get(leader,0) + 1


# print sorted(scc.values())
    


            
    
    
    