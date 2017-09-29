#递归的方式
def fib(n):
	if n<=2:
		return 1
	else:
		return fib(n-1)+fib(n-2)

print(fib(1))
print(fib(2))
print(fib(4))

def fib_tail(n,temp=1,total=1):
	if n<=2:
		return total
	else:
		return fib_tail(n-1,total,total+temp)

print(fib_tail(3))

def fib_circle(n):

	a=1
	b=1
	if n<=2:
		return 1
	else:
		for i in range(2,n):
			c=a+b
			a=b
			b=c
		return c
