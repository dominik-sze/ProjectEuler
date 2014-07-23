def problem16():
	num = 2**1000
	digitSum = 0
	for i in str(num):
		digitSum+=int(i)
	print(digitSum)

if __name__=='__main__':
	problem16()

