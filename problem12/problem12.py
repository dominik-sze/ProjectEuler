def problem12():
	num = 1
	while True:
		triangle = (num*(num+1))/2
		num += 1
		counter = 0
		for i in range(1, int(triangle**0.5)):
			if triangle%i == 0:
				counter+=2

		if counter>500:
			print(int(triangle))
			break

if __name__=='__main__':
	problem12()

