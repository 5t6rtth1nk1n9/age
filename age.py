driving = input('請問你有沒有開過車?')
if driving == '有':
	age = int(input('請問你的年齡?'))
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == '沒有':
	age = int(input('請問你的年齡?'))
	if age >= 18:
		print('你可以考駕照了阿，怎麼還不去考')
	else:
		print('很好， 再過幾年你就可以去考駕照了')
else:
	print('87題目答案好好填拉(只能填有/沒有)XD')