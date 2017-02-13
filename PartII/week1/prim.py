flag = True
num_nodes = 0
num_edges = 0

f = open("./edges.txt")

graph = {}

for row in f:
	if(flag):
		temp = row.strip().split(' ')
		num_nodes = int(temp[0].strip())
		num_edges = int(temp[1].strip())
		flag = False
	else:
		temp = row.strip().split(' ')
		node1 = int(temp[0].strip())-1
		node2 = int(temp[1].strip())-1
		cost = int(temp[2].strip())

		if(graph.get(node1) == None):
			graph[node1] = [(node2,cost)]
		else:
			graph[node1].append((node2,cost))

		if(graph.get(node2) == None):
			graph[node2] = [(node1,cost)]
		else:
			graph[node2].append((node1,cost))		


X = [0]
visited = [0 for dummy in range(num_nodes)]
visited[0] = 1

min_cost = 0.0
while(len(X) < num_nodes):
	temp_min = None
	temp_v = -1
	temp_w = -1
	for node in X:

		nb = graph[node]
		for edge in nb:
			if(visited[edge[0]] > 0):
				continue
			else:
				if((temp_min == None) or (edge[1] < temp_min)):
					temp_min = edge[1]
					temp_v = node
					temp_w = edge[0]
	X.append(temp_w)
	visited[temp_w] = 1
	min_cost += temp_min
print min_cost

