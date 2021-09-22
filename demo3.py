a=3.1415
print(a,type(a))
n1=1.1
n2=2.2
print(n1+n2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
print(f1+1)
print(f2+1)

name='张三'
age=20
print(type(name),type(age))
print('我叫'+name+'，今年'+str(age)+'岁')     #'int str类型相同才能相加'可将int转成str()类型

a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

#字符串中的数据如果是非数字串，则不允许转换，如float（’hello‘）