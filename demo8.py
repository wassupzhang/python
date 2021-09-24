answer=input('您是会员吗y/n')     #嵌套if的表达
money=float(input('请输入您的购物金额'))
if answer=='y':
    if money>=200:
        print('打八折，付款金额为:',money*0.8)
    elif money>=100:
        print('打九折，付款金额为：',money*0.9)
    else:
        print('不打折，付款金额为：',money)
else:
    if money>=200:
        print('打9.5折，付款金额为：',money*0.95)
    else:
        print('不打折，付款金额为：',money)

