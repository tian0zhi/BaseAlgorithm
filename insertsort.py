def insertsort(li):
	'''插入排序'''
	Length = len(li)# 列表长度
	for i in range(1,Length):# 只需排序1 - len(li)
		for j in range(0,i):# 比较待排序数与已经排好序(有序区)各元素大小
			if li[j] > li[i]:# 升序排序，如果待排序数li[i]<有序区li[j]，交换他们
				temp = li[j]
				li[j] = li[i]
				li[i] = temp
			else:# 如果待排序数li[i]!<有序区li[j],结束这次 待排序数li[i] 排序
				break


a = [10,9,8,7,6,5,4,3,2,1]

insertsort(a)
print(a)