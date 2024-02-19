password = 'a123456'

x = 0
y = input("password:")
if y != 'a123456' :
	while x <= 2 and y != 'a123456' :
		print('密碼錯誤,還有',2-x,'次機會')
		y = input("password:")
		x = x + 1
	if  y != 'a123456':
		print('登入失敗次數過多，請15分鐘後再試')

if y == 'a123456':
	print('登入成功，請稍後!')
		