def is_prime(num):
	if num<=3:
		if num<=1:
			return False
		return True
	if num%2==0 or num%3==0:
		return False
	for i in range(5, int(num**0.5) +1, 6):
		if num%i==0 or (num%(i+2))==0:
			return False
	return True

def problem10():
	sum = 0
	for i in range(1, 2000000):
		if(is_prime(i)):
			sum+=i
	print(sum)

if __name__=='__main__':
	problem10()
