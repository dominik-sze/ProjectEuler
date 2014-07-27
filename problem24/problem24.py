import itertools
import profile
import math

def problem24():
	all_permutations = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
	miliionth_perm = all_permutations[999999]
	print(''.join([str(x) for x in miliionth_perm]))

def problem24a():
	elements = [0,1,2,3,4,5,6,7,8,9]
	remain = 999999
	perm = ""
	
	for i in range(1,10):
		j = remain//math.factorial(10-i)
		remain = remain%math.factorial(10-i)
		perm += str(elements[j])
		del elements[j]
		if remain==0:
			break
	print(perm+''.join([str(x) for x in elements]))

if __name__=='__main__':
	profile.run("problem24()")
	profile.run("problem24a()")
