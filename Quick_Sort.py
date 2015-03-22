def quicksort(num, start, end):
	if start >= end:
		return
	pivot = num[start]
	i = start
	j = end
	while i < j:
		while i < j and num[j] >= pivot:
			j -= 1
		num[i] = num[j]
		while i < j and num[i] < pivot:
			i += 1
		num[j] = num[i]
	num[i] = pivot
	quicksort(num, start, i-1)
	quicksort(num, i+1, end)

# Test
a = [1,4,2,8,5,7]
quicksort(a,0,5)
print a

