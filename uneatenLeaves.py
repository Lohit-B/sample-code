caterpilars = [2,3, 5, 7]

def isPrime(n):
	if (n ==1 or n % 2 == 0 or n%3 == 0): return False
	k = 1
	while 6*k+1 < n**(1/2):
		if(n%6*k-1==0 or  6*k+1 == 0): return False
	return True

def getDivisor(cp, prime, primeFactors):
	if cp ==1: return primeFactors, cp
	count = 0
	while (cp % prime == 0):
		cp = cp/prime
		count += 1
	if count >=1:
		primeFactors.append(prime)
	return primeFactors, cp

def getPrimeFactors(n):
	primeFactors = []
	if isPrime(n):
		primeFactors.append(n)
		return primeFactors;

	primes = [2, 3]
	for prime in primes:
		primeFactors, n = getDivisor(n, prime, primeFactors)

	if (isPrime(n)):
		primeFactors.append(n)
		return primeFactors
	
	k = 1
	while(n > 6*k+1):
		if (isPrime(6*k-1)):
			primeFactors, n = getDivisor(n, 6*k-1, primeFactors)
		if (isprime(6*k+1)):
			primeFactors, n = getDivisor(n, 6*k+1, primeFactors)
		k += 1
	
	return primeFactors

def getCPFactors(arrCP):
	factors = []
	for cp in arrCP:
		factors = factors + getPrimeFactors(cp)
	return list(set(factors))

def errorCor(initNum, primes, n): # sorted list of primes
	count = 0
	for p in primes:
		if initNum*p > n:
			return count
		count += (errorCor(initNum*p, primes[primes.index(p)+1:], n)+n/(initNum*p))
	return count
	
def getEatenLeaves(primes, n):
	countEaten = 0 
	for prime in primes:
		numOfLeavesEatenByPrime = n/prime
		countEaten += numOfLeavesEatenByPrime
		for p in primes:
			if p <= prime:
				continue
			countEaten -= (numOfLeavesEatenByPrime/p -  errorCor(p, primes[primes.index(p)+1:], numOfLeavesEatenByPrime))
	return countEaten

print getEatenLeaves(getCPFactors(caterpilars), 50)
