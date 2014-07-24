def problem17():
	ntol = {'one':3,'two':3,'three':5,'four':4,'five':4,'six':3,'seven':5,'eight':5,'nine':4,'ten':3,
		'eleven':6,'twelve':6,'thirteen':8,'fourteen':8,'fifteen':7,'sixteen':7,'seventeen':9,'eighteen':8,'nineteen':8,
		'twenty':6,'thirty':6,'forty':5,'fifty':5,'sixty':5,'seventy':7,'eighty':6,'ninety':6,'hundred':7,'thousand':8, 'and':3}

	letters = 0

	oneTo9 = ntol['one']+ntol['two']+ntol['three']+ntol['four']+ntol['five']+ntol['six']+ntol['seven']+ntol['eight']+ntol['nine']
	tenTo19 = ntol['ten']+ntol['eleven']+ntol['twelve']+ntol['thirteen']+ntol['fourteen']+ntol['fifteen']+ntol['sixteen']+ntol['seventeen']+ntol['eighteen']+ntol['nineteen']
	twentyTo99 = 10*(ntol['twenty']+ntol['thirty']+ntol['forty']+ntol['fifty']+ntol['sixty']+ntol['seventy']+ntol['eighty']+ntol['ninety']) + 8*oneTo9
	hundredTo999 = 9*(ntol['hundred'])+9*99*(ntol['hundred']+ntol['and'])+9*(oneTo9+tenTo19+twentyTo99)+100*oneTo9 

	letters = oneTo9+tenTo19+twentyTo99+hundredTo999+ntol['one']+ntol['thousand']

	print(letters)


if __name__=='__main__':
	problem17()
