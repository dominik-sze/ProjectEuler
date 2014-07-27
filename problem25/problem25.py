import profile

def problem25():
	first = 1
	second = 1
	sum = 0
	count = 3
	while True:
		sum = first+second
		first = second
		second = sum
		if len(str(sum))==1000:
			break
		count+=1
	print(count)

if __name__=='__main__':
	profile.run("problem25()")
		
