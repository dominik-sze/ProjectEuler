import math

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

def problem3():
	number = 600851475143
	#number = 13195
	for i in range((int)(math.sqrt(number)), 1, -1):
		if number%i==0 and is_prime(i):
			print(i)
			return


if __name__=='__main__':
	problem3()
