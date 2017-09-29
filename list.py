
L = [['b',6,3],['a',1,3],['c',4,3],('c',3,3)]  
L.sort(key=lambda x:(x[0],x[1]))
print(L)

s='string'
l=list(s)
l.sort(reverse=True)
s=''.join(l)
print(s)

x=['aaa','ccccc','bb']
x.sort(key=lambda x:len(x))
print(x)

d={'na':98,'tang':100,'long':90}
print(d['na'])
print(d.get('tang'))
print(set([4,3,2,2]))
l1=L[1:2]
print(l1)
s1='0123456789'
print(s1[::-2])
for key in d:
	print(key)

for value in d.values():
	print(value)

S="ABC"
print(S[1])
for s in S:
	print(s)

for k,v in d.items():
	print(k,':=',v)
print(d.items())
d1=sorted(d.items(),key=lambda x:x[0])
print(d1)