import math

def problem21():
	sum = 0
	for i in range(1,10000):
		b = 0
		for j in range(1, int(i/2+1)):
			if i%j==0:
				b+=j
		if(i==b):
			continue
		a = 0
		for j in range(1, int(b/2+1)):
			if b%j==0:
				a+=j
		if i==a:
			sum+=i
	print(sum)

if __name__=='__main__':
	problem21()

