import random
import copy

f = open("./KargerMinCut.txt")
ad_list = []
V_list = []
count = 0
for row in f:
	V_list.append(count)
	count += 1
	temp = row.strip().split('\t')
	temp_ls = []
	for i in range(1,len(temp)):
		temp_ls.append(int(temp[i].strip()) - 1)
	ad_list.append(temp_ls)


def KargerMinCut(ad_list,V_list):
	ad_l = copy.deepcopy(ad_list)
	V = copy.deepcopy(V_list)
	n_nodes = len(V)
	for i in range(n_nodes - 2):
		random_start = random.choice(V)
		random_end = random.choice(ad_l[random_start])

		V.remove(random_end)
	
		temp_ad = copy.deepcopy(ad_l[random_end])
	
		for item in temp_ad:
			ad_l[item].remove(random_end)
			if (item != random_start):
				ad_l[item].append(random_start)
				ad_l[random_start].append(item)
		ad_l[random_end] = []
	return len(ad_l[V[0]])


def random_trial(ad_l,V_l,times):
	min_cut = -1
	for i in range(times):
		temp_min = KargerMinCut(ad_l,V_l)
		if((min_cut < 0) or (temp_min < min_cut)):
			min_cut = temp_min
	return min_cut



print random_trial(ad_list,V_list,100)




