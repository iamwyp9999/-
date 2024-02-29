# 讀取檔案
# .strip() 刪除換行符號

import time
data = []
count = 0
with open ('reviews.txt') as f:
	for line in f:
		data.append(line.strip())
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('檔案讀取完成，總共有',len(data),'筆資料')
print('-----------------------')
sum_len = 0
for d in data:
	sum_len += len(d)
print('留言平均長度為,',sum_len / len(data))
print('-----------------------')
n = 0
while True:
	print(data[n])
	print('-----------------------')
	n += 1
	time.sleep(0.5)
