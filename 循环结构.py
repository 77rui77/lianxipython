a=0
sum=0
while a<5:
    sum+=a
    a+=1
    print(sum)

a=1
sum=0
while a<=100:
    if not bool(a%2):
        sum+=a
    a+=1
print('1-100之间的偶数和',sum)