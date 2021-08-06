#判断两个整数大小
a=int(input('输入一个整数'))
b=int(input('输入一个整数'))
'''if a>=b:
    print(a,'>=',b)
else:
    print(a,'<',b)
'''
print(str(a)+'>='+str(b)   if a>=b  else   str(a)+'<'+str(b))
