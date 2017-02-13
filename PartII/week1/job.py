flag = True
num_jobs = 0
jobs = []
f = open("./jobs.txt")
for row in f:
	if(flag):
		num_jobs = int(row.strip())
		flag = False
	else:
		temp_job = row.strip().split(' ')
		temp_weight = int(temp_job[0].strip())
		temp_len = int(temp_job[1].strip())
		temp_diff = temp_weight - temp_len
		#temp_diff = temp_weight * 1.0 / temp_len
		jobs.append((temp_weight,temp_len,temp_diff))

def my_compare(job1,job2):
	if(job1[2] > job2[2]):
		return -1
	elif(job1[2] < job2[2]):
		return 1
	else:
		if (job1[0] > job2[0]):
			return -1
		elif (job1[0] < job2[0]):
			return 1
		else:
			return 0

sorted_jobs = sorted(jobs,cmp=my_compare)

complete_time = 0
weighted_time = 0
for item in sorted_jobs:
	complete_time += item[1]
	weighted_time += item[0] * complete_time
print weighted_time


