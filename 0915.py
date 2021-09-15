#Python是弱型語言
#格式化列印一
price = 10.6
qty = 20
print("單價:%.2f,數量:%d,總價:%f" % (price,qty,price*qty))
#                                   參數(tuple)
#格式化列印二
price = 10.6
qty = 20
print('單價:{0:2},數量:{1},總價:{2}'.format(price,qty,price*qty))
print(f"單價:{price},數量:{qty},總價:{price*qty}")
print('單價:{0},數量:{1},總價:{2}'.format(price,qty,price*qty))
print('單價:{0:.2f},數量:{1},總價:{2}'.format(price,qty,price*qty))

#變數Variable－－可變動的數
x = 10  #產生一個空間，並將10放入
y = 20
print(f'x={x},y={y}')
x=100 #直接更改x的值
print(f'x={x},y={y}')
x = "student"
print("x=%s,y=%d" % (x,y))
# %d：整數 %f：小數 %s：字串
"""
C/C++
int x; //宣告x為4byte
x=10; //初始化
lung z=10;
x="abc";<-錯誤

Java
int x; //宣告並初始化為0
System.out.printIn("x="+x);
lung z=10;
-21億~21億
"""
