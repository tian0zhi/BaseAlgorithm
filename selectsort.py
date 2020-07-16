def selectsort(li):
	'''选择排序'''
	length  = len(li)
	for i in range(0,length - 1):# 每一趟排好一个数
		minindex = i
		for j in range(i + 1,length):# 选出从i - length的最小数
			if li[j] < li[minindex]:
				minindex = j
		temp = li[minindex]# 交换最小数
		li[minindex] = li[i]
		li[i] = temp # 排序第i个


a = [10,9,8,7,6,5,4,3,2,1]

selectsort(a)

print(a)