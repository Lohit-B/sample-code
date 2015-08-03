numOfDigits = 2
diff = 8
count = 0

def calculateSuffixes(n, diff):
	return [num for num in range(10) if abs(n-num) >= diff]

def calNumbers(arr, digitsInNum, count, diff):
	for num in arr:
		if (digitsInNum == 1):
			count = count + len(arr)
			break
		count = calNumbers(calculateSuffixes(num, diff), digitsInNum-1, count, diff)
	return count

print calNumbers(range(1,10), numOfDigits, 0, diff)


