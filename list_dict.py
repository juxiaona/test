str1 = "k:1|k1:2|k2:3|k3:4"
list1=str1.split('|')
D={}
for i in list1:
	key=i.split(':')[0]
	value=i.split(':')[1]
	D[key]=value
print(D)
t=(1,2,3)
for i in t:
	print(i)