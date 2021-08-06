a=20
a+=30
print(a)
a-=10
print(a)
a*=2
print(a)

money=1000
s=int(input('请输入金额'))
if s<=money:
    money=money-s
    print('取款成功，余额为：',money)
else:
    print('余额不足，余额为：',money)







