def onesort(li,left,right):
	i = left
	j = right
	A = left
	Base = li[A]
	while j > i:
		while j > i and li[j] > Base:
			j = j - 1
		if j > i:
			li[A] = li[j]# 往原来的坑里填数
			A = j# 挖新的坑
		while j > i and li[i] < Base:
			i = i + 1
		if j > i:
			li[A] = li[i]# 往原来的坑里填数
			A = i# 挖新的坑
	li[A] = Base
	return A


def quick_noR(li,left,right):
	'''快速排序的非递归实现'''
	'''不考虑区间排序的先后，只要把指定区间排好就行'''
	'''利用栈保存要排序的区间起止位置'''
	Rli = []
	Rli.append(left)
	Rli.append(right)

	while len(Rli) > 0:
		j = Rli.pop()# right
		i = Rli.pop()# left
		A = onesort(li,i,j)
		if A - 1 > i:
			Rli.append(i)
			Rli.append(A)
		if A + 1 < j:
			Rli.append(A + 1)
			Rli.append(j)


a = [5,1,2,4,6,10,7,3,8,9]

quick_noR(a,0,9)
print(a)
