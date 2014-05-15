# prime numbers
def isPrime(x):
	c = 1
	prime = True
	while 1:
		c+=1
		if c>=x:	break
		if x%c == 0: prime = False
	
	return prime
	
def primeFactors(x):
	q = x
	while 1:
		q -= 1
		#if q>=x : break
		if isPrime(q) and x%q == 0:
			print q; break

#primeFactors(123131313)
print isPrime(121212121121)