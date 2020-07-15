def Bubblesort(li):
	'''冒泡法排序'''
	Length = len(li)
	for i in range(Length - 1):
		print(i)
		for j in range(Length - i - 1):
			if li[j] > li[j + 1]:
				temp = li[j + 1]
				li[j + 1] = li[j]
				li[j] = temp



a = [9,7,6,2,5,1,8,10,3,4]

Bubblesort(a)

print(a)