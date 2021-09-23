print(2*4)
print(11//2)#取整运算
print(11%2)#取余运算
print(2**3)#2的3次方
print(-9//4)#一正一负向下取整
print(9%-4)#余数=被除数-除数*商

#运算符
a=20
a+=30
print(a)
a,b,c,=20,30,40
print(a,b,c)

#交换两个值
a,b=10,20
print('交换之前:',a,b)
a,b=b,a
print('交换之后:',a,b)

a,b=10,20   #比较运算符
print('a>b吗?',a>b)
print('a!=b吗?',a!=b)
lst1=(11,22,33,44)
lst2=(11,22,33,44)
print(lst1==lst2)
print(lst1 is lst2)#is比较的是id的值
print(id(lst1))
print(id(lst2))

#布尔运算
a,b=1,2
print(a==1 and b==2)
print(a==1 and b<2)#false ang true == false
#or 或者
print(a==1 or b<1)
#not
f=True
f2=False
print(not f)
print(not f2)
#in ----not in
s='helloworld'
print('e'not in s)
