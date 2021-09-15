print("請輸入半徑：")
#狀況一
r = input() #自鍵盤key in一串字串
fr = float(r) #字串轉成小數
print('半徑為：%s' % (r))
a = fr * fr * 3.14159
print(f'面積為：{a}')

#狀況二
r = float(r)
a = r * r * 3.14159
print(f'面積為：{a}')

#狀況三
a = float(r) * float(r) * 3.14159
print(f'面積為：{a}')

#狀況四
r = float(input())
a = r * r * 3.14159
print(f'面積為：{a}')

#精簡
"""
eval()>>此函數可將輸入的str轉成各種公式並加以計算
r = eval(input("請輸入半徑："))
a = pow(r,2) * math.pi
pow(x,y)=x的y次方  Alt+import math
print(f"面積為：{a}")
short salary = 40000
int salary = -21億~-21億
pow(2,5)=32
pow(2,8)=256
pow(2,10)=1024
pow(2,16)=65536>>-32768~-1；0~32767
pow(2,24)=1677萬
pow(2,32)=42億
"""