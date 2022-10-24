print("working...")
print("The firsr 9 Prime Fibonacci numbers:")

num = 0

def isprime(m):
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True

def fib(nr):
	if (nr == 0):
		return 0
	if (nr == 1):
		return 1
	if (nr > 1):
		return fib(nr-1) + fib(nr-2)

for n in range(2,520000):
	x = fib(n)
	if isprime(x):
		num = num + 1
		if (x > 1):
			if (num < 11):
				print(str(x),end=" ")
			else:
				break

print()
print("done...")