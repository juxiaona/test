'''
对于list的排序，python提供了两种方式
list.sort(key,reverse)
sorted(list,key,reverse)
sorted 返回一个对象，可以用作表达式，改变了原来的list生成一个新的list
list.sort()不会返回对象，改变的是原来的list
reverse 默认值是False默认正序排列，如果设为True，为倒序排列
'''
L1=[4,3,1,2]
L1.sort()
print(L1)

L2=['abc','423','we2','123']
L2.sort()
print(L2)

#根据第二个关键字排序
L3=[('a',3),('b',1),('c',2)]
L3.sort(key=lambda x:x[1])
print(L3)
#根据第一个关键字排序
L3.sort(key=lambda x:x[0])
print(L3)


#根据字典的value 排序
L4=[{'name':100},{'name':97},{'name':98}]
L4.sort(key=lambda x:x['name'])
print(L4)

#先根据第二个关键字排序，再根据第一个关键字排序
L5=[('c',1),('b',2),('a',2),('d',0)]
L5.sort(key=lambda x:(x[1],x[0]))
print(L5)

L6=['123','45','678','23']
L6.sort(key=lambda x:x[1])
print(L6)

'''list切片'''
L=[0,1,2,3,4,5,6,7,8,9]

print(L[1:3])
print(L[:3])
print(L[3:])
print(L[3::2])
print(L[::-1])


'''字符串排序'''
str='string'
l=list(str)
print(l)
l.sort(reverse=True)
str1=''.join(l)
print(str1)


'''dict相关知识，dict 本身是无序的，可以根据keys、values、items排序'''
list1=['nana','tang','long']
list2=[98,100,96]
dict1=dict(zip(list1, list2))
print(dict1)
print(list(dict1.keys()))
print(list(dict1.values()))
items=list(dict1.items())
print(items)
items.sort(key=lambda x:x[0])
print(items)
items.sort(key=lambda x:x[1])
print(items)
dict2=dict(items)
print(dict2)

D={}
for i in range(len(items)):
	D[items[i][0]]=items[i][1]
print(D)