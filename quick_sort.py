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



def quicksort(li,left,right):
	# print(li)
	if left >= right:
		return
	else:
		A = onesort(li,left,right)
		quicksort(li,left,A)
		quicksort(li,A+1,right)
		

a = [5,1,2,4,6,10,7,3,8,9]

quicksort(a,0,9)
print(a)