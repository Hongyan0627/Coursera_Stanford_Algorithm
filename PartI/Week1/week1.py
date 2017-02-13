# save all the integers
f = open("./IntegerArray.txt")
nums = []
for row in f:
    nums.append(float(row.strip()))
    
# merge sort to count the inversions
def merge_sort_and_count(ls):
    ls_length = len(ls)
    if (ls_length <= 1):
        return (0,ls)
    else:
        mid = ls_length / 2
        first_ls = ls[0:mid]
        second_ls = ls[mid:]
        (n1,sorted_ls1) = merge_sort_and_count(first_ls)
        (n2,sorted_ls2) = merge_sort_and_count(second_ls)
        temp_ls = []
        l1_length = len(sorted_ls1)
        l2_length = len(sorted_ls2)
        temp_n = 0
        i = 0
        j = 0
        while( (i < l1_length) and (j < l2_length)):
            if (sorted_ls1[i] <= sorted_ls2[j]):
                temp_ls.append(sorted_ls1[i])
                i += 1
            else:
                temp_ls.append(sorted_ls2[j])
                temp_n += (l1_length - i)
                j += 1
        if (i == l1_length):
            temp_ls += sorted_ls2[j:]
        else:
            temp_ls += sorted_ls1[i:]
        
        return ((temp_n + n1 + n2),temp_ls)

n,ls = merge_sort_and_count(nums)
print n
        
    
