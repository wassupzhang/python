print(4&8) #二进制，按位与&，同为1时结果为1
print(4|8) #按位或|，同为0时结果为0
print(4<<1)#向左移动一位，相当于乘以2
print(4>>1)#向右移动一位，相当于除以2

#顺序结构
print('------程序开始-----')
print('1.把冰箱门打开')
print('2.把大象放冰箱里')
print('3.把冰箱门关上')
print('-----程序结束------')

#测试对象的布尔值(都为false)
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool([]))  #空列表
print(bool(dict()))
print(bool(set()))

#单分支结构
money=1000
s=int(input('请输入取款金额'))
if money>=s:
    money=money-s
    print('取款成功，余额为：',money)

#双分支结构（if   else）
num=int(input('请输入一个整数'))
if num%2==0:
    print(num,'是偶数')
else:
    print(num,'是奇数')