def onesort(li,now,high):
	'''li为待排序堆，now为当前节点索引，high为最大索引下标 O(nlogn)'''
	i = now
	j = now *2 + 1
	base = li[now]
	while j <= high:
		if j + 1 <= high:
			if li[j + 1] > li[j]:
				j = j + 1
		if base < li[j]:
			li[i] = li[j]
		else:#如果父节点都比孩子节点大就退出循环
			break
		i = j# 这里有问题
		j = 2*i + 1
		
	li[i] = base
	# print(li)


def heapsort(li,low,high):
	end = (high - 1)//2
	for i in range(end,low-1,-1):
		# print(i)
		onesort(li,i,high)

def chage(li,a,b):
	temp = li[a]
	li[a] = li[b]
	li[b] = temp

a = [5,1,2,4,6,10,7,3,8,9]
b = [1, 9, 7, 8, 6, 2, 5, 3, 4]#,10]
for i in range(0,9):
	# print(9 - i)
	heapsort(a,0,9 - i)
	# print(a)
	chage(a,0,9 - i)
	# print(a)

print(a)
# heapsort(a,0,9)
# print(a)
# chage(a,0,9)
# print(a)
# heapsort(b,0,8)
# print(b)
# chage(a,0,8)
# print(a)
# for i in range(0,9):
	# heapsort(a,0,9 - i)
	# chage(a,0,9 - i)
	# print(a)