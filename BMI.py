# BMI值計算公式:    BMI = 體重(公斤) / 身高(公尺)^2

print('BMI數值換算及體質判定:')
print('體重正常範圍為BMI:18..5 ~ 24')
print('過重：24≦BMI＜27 / 輕度肥胖：27≦BMI＜30 / 中度肥胖：30≦BMI＜35 / 重度肥胖：BMI≧35')
data_h = input('你的身高(公尺)為:')
data_h = float(data_h)
data_w = input('你的體重(公斤)為:')
data_w = float(data_w)
data_bmi = data_w / data_h ** 2
print('你的BMI指數為:',data_bmi)
if data_bmi < 18.5:
	print('判定結果:體質過輕')
elif data_bmi >= 18.5 and data_bmi<24:
	print('判定結果:體質正常')
elif data_bmi >= 24 and data_bmi<27:
	print('判定結果:體質過重')
elif data_bmi >= 27 and data_bmi<30:
	print('判定結果:輕度肥胖')
elif data_bmi >= 30 and data_bmi<35:
	print('判定結果:中度肥胖')
elif data_bmi >= 35:
	print('判定結果:重度肥胖')
else:
	print('輸入錯誤')