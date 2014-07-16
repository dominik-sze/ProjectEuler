def problem2():
	first = 1
	second = 2
	sum = 2
	while second<4000001:
		tmp = first+second
		first = second
		second = tmp
		if(tmp%2==0):
			sum+=tmp
	print(sum)

if __name__=='__main__':
	problem2()
