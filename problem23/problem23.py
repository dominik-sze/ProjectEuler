import profile

def eratosthenes_sieve2(upper_limit):
	"""
	Returns a list of primes < n
	"""
	sieve = [True]*upper_limit
	for i in range(3, int(upper_limit**0.5)+1, 2):
		if sieve[i]:
			sieve[i*i::2*i] = [False]*int(((upper_limit-i*i-1)/(2*i)+1))
	return [2] + [i for i in range(3, upper_limit, 2) if sieve[i]]

def sum_factors_prime(number, primes, plen):
	n = number
	sum = 1
	p = primes[0]
	i = 0
	l = plen
	while p*p<=n and n>1 and i<l:
		p = primes[i]
		i+=1
		if n%p==0:
			j=p*p
			n=n/p
			while n%p==0:
				j = j*p
				n = n/p
			sum = sum*(j-1)/(p-1)
	if n>1:
		sum*=n+1
	return sum-number

def problem23():
	maxa = 28123
	abundant = []
	primes = eratosthenes_sieve2(int(maxa**0.5)+1)
	l = len(primes)
	for i in range(2, maxa):
		sum = sum_factors_prime(i, primes, l)
		if sum>i:
			abundant.append(i)
	asum = 0
	can = [True]*(maxa)
	counter = 0
	sum = 0
	for i in abundant:
		for j in abundant[counter::]:
			if (i+j) < maxa:
				can[i+j]=False
		counter+=1
	allsum = 0
	for i, v in enumerate(can):
		if v==True:
			allsum+=i

	print(allsum)

if __name__=='__main__':
	profile.run("problem23()")
