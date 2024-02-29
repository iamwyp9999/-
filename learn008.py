# import (載入) 
# randint = random int , 唯一函數

import random
import time

i = 0
while True:
	if i < 5:
		r = random.randint(1, 100)
		i = i + 1
		print(r)
		time.sleep(0.5)
	else:
	 break
print('數值產生結束')

