def problem14():
	num = None
	longest = 0
	for i in range(999999, 1, -1):
		n = i
		counter = 1
		while True:
			if n==1:
				break
			elif n%2 == 0:
				n=n/2
			else:
				n=3*n+1
			counter+=1
		if counter>longest:
			longest = counter
			num = i
	print(num)
			
if __name__=='__main__':
	problem14()
