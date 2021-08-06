s=int(input('请输入成绩:'))
if 90<=s<=100:
    print('A')
elif 80<=s<90:
    print('B')
elif 70<=s<80:
    print('C')
elif 60<=s<70:
    print('D')
elif 0<=s<60:
    print('不及格')
else:
    print('请输入有效成绩')