d={'na':98,'tang':100,'long':90}
print(d.items())

for x in d.keys():
	print(x)

d1=sorted(d.items(),key=lambda x:x[1])
print(dict(d1))
item=d.items()
print(list(item))
print(list(d.values()))
print(list(d.keys()))

print(list(range(10)))