g=(x*x for x in range(1,11))
for n in g:
	print(n)

print(abs(-10))

print(abs)
f=abs
print(f(-10))

def f1(x,y,f):
	return f(x)+f(y)

print(f1(1,-2,abs))

def is_odd(n):
	if n%2==1:
		return True
	else:
		return False

f=filter(is_odd, [1,2,3,4,5,6,7,8,9])
print(f)
print(list(f))