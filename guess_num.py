import random
start = input('請輸入隨機數字範圍開始值: ')
end = input('請輸入隨機數字範圍結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count = count + 1 #可以寫成count += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次') #避免break讓最後一行沒有被讀到
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次') #寫在最底下避免重複寫多次
