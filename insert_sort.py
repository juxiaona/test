def insert_sort(lists):

	for i in range(len(lists)):
		position=i

		while position>0:
			if lists[position-1]>lists[position]:
				temp=lists[position-1]
				lists[position-1]=lists[position]
				lists[position]=temp
			position-=1
		print(lists)

	return lists

L=[8,4,5,7,2,5,1]

insert_sort(L)