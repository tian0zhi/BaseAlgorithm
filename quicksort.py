def QuickSort(li,left,right):
	'''快排'''
	Length = len(li)
	if left >= right or Length <= 1:
		return
	else:
		i = left
		j = right
		A = left
		Base = li[A]
		while j > i:
			while j > i and li[j] >= Base:
				j = j - 1
				print('j=',j)
			if j > i:
				li[A] = li[j]
				A = j
			while j > i and li[i] < Base:
				i = i + 1
				print('i=',i)
			if j > i:
				li[A] = li[i]
				A = i
			# print(li)
		
		li[A] = Base
		print(li)
		QuickSort(li,left,A-1)
		QuickSort(li,A+1,right)
		# print(li)
		

a = [5,1,2,4,6,10,7,3,8,9]

QuickSort(a,0,9)
print(a)