def bubble_sort(lists):
	len_list=len(lists)
	for i in range(len_list):
		for j in range(len_list-i-1):
			if lists[j]>lists[j+1]:
				temp=lists[j]
				lists[j]=lists[j+1]
				lists[j+1]=temp
		print(lists)
	return lists


lists1=[1,4,6,3,7,5,2]
bubble_sort(lists1)
