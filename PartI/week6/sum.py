f = open("./2sum.txt")
dic = {}

for row in f:
	temp_num = int(row.strip())
	dic[temp_num] = dic.get(temp_num,0) + 1


array = dic.keys()
array = sorted(array)
array_len = len(array)


stat = {}

q = array_len-1
p = array_len-1

i = 0
j = array_len-1

while(i <= q):
	if(array[i] + array[p] >= - 10000):
		while(array[i] + array[p] > 10000):
			p -= 1
		j = p
		while(array[i] + array[j] >= -10000):
			stat[array[i] + array[j]] = 1
			j -= 1
		q = j
	i += 1

print len(stat.keys())

f.close()