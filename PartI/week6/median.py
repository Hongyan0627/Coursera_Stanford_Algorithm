import Queue as Q
import math
q_low = Q.PriorityQueue()
q_high = Q.PriorityQueue()


f = open("./Median.txt")
numbers = []
for row in f:
	numbers.append(int(row.strip()))
f.close()

medians = []
for i in range(len(numbers)):
	if(q_low.qsize() < 1):
		q_low.put((-numbers[i],numbers[i]))
		medians.append(numbers[i])
		continue
	else:
		temp_min = q_low.get()[1]
		if (temp_min < numbers[i]):
			q_high.put(numbers[i])
		else:
			q_low.put((-numbers[i],numbers[i]))
		q_low.put((-temp_min,temp_min))

		while((q_low.qsize() - q_high.qsize()) > 1):
			temp = q_low.get()[1]
			q_high.put(temp)

		while(q_low.qsize() < q_high.qsize()):
			temp = q_high.get()
			q_low.put((-temp,temp))
		temp_median = q_low.get()[1]
		medians.append(temp_median)
		q_low.put((-temp_median,temp_median))
	# if(i == 6):
	# 	while(q_low.qsize() > 0):
	# 		print q_low.get()[1]
	# 	print "*************************"
	# 	while(q_high.qsize()>0):
	# 		print q_high.get()
	# 	break
print sum(medians)