# 終極密碼
# 猜錯顯示比答案大還是小
# 猜對顯示答案並說恭喜猜對了

import random
start = input('請決定範圍數字起始值:')
start = int(start)
end = input('請決定範圍數字結束值:')
end = int(end)
r = random.randint(start,end)
count = 1
while True:
	print() 
	print('第',count,'次猜測')
	num = input('請猜目標數字：')
	num = int(num)
	if num == r:
		print('恭喜你猜對了，答案為:',num)
		break
	elif num  > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	count += 1 # 等同於count = count + 1


