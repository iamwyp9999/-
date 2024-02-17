#因input會轉為字串，不同類別變數無法比較

age = input('請輸入您的年齡:') 
#此時age為字串函數
age = int(age) 
#此時型態轉換,age已從字串函數換為整數函數
if age >= 20 : 
	print('您已成年，可以投票')
if age <= 20 :
	print('您還未成年')