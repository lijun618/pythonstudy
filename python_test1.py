# 用1/2/3/4 这4个数字组成无重复数字的三位数，并输出三位数的总个数
sum=0
for a in range(1,5):
    for b in range(1,5):
        for c in range (1,5):
            if ((a!=b)and (b!=c)and (c!=a )):
                print(a,b,c)
                sum+=1
print(sum)
