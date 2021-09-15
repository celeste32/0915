"""r = float(input("請輸入數字："))
print(r)
x = int(input("請輸入數字："))
print(x)"""

y = eval(input('請輸入數字：'))
print(y*10)

import math
#cmd命令
#eval()>>此函數可將輸入的str轉成各種公式並加以計算
r = 10.6
cmd = 'pow(r,2)*math.pi'
print(cmd)
print(eval(cmd))