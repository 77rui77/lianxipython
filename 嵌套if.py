s=input('你是会员吗？是/否')
money=float(input('请输入金额：'))
if s=='是':
    if money>=200:
        print('打八折，应付金额为：',money*0.8)
    elif 100<=money<200:
        print('打九折，应付金额为：',money*0.9)
    else:
        print('不打折，应付金额为：',money)
else:
    if money>=200:
        print('打九五折，应付金额为：',money*0.95)
    else:
        print('不打折，应付金额为：',money)