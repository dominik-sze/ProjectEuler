import math

def problem20():
	num = math.factorial(100)
	sum = 0
	for c in str(num):
		sum+=int(c)
	print(sum)

if __name__=='__main__':
	problem20()
