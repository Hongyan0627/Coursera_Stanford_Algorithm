f = open("./QuickSort.txt")
nums = []
for row in f:
    nums.append(float(row.strip()))

# swap function
def swap(lst,index1,index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp
    
def select_pivot(ls,left,right,pivot_flag):
    if (pivot_flag == 2):
        return right
    elif (pivot_flag == 3):
        middle = (right + left) / 2
        return sorted([(ls[left],left),(ls[middle],middle),(ls[right],right)])[1][1]
    else:
        return left
    
def quick_sort(ls,left,right,pivot_flag):
    if (right <= left):
        return 0
    else:
        len_ls = right - left + 1
        pivot_index = select_pivot(ls,left,right,pivot_flag)
        swap(ls,left,pivot_index)
        i = left + 1
        j = i
        while (j <= right):
            if (ls[j] < ls[left]):
                swap(ls,i,j)
                i += 1
            j += 1
        if ((i-1) > left):
            swap(ls,left,i-1)
            
        n1 = quick_sort(ls,left,i-2,pivot_flag)
        n2 = quick_sort(ls,i,right,pivot_flag)
        return (n1 + n2 + (len_ls - 1))

pivot_method = 3
n = quick_sort(nums,0,len(nums)-1,pivot_method)
print n