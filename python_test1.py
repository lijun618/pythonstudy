#test1:4个数字1/2/3/4数字，组成无重复数字的3位数，并输出总个数
#遍历for循环+判断无重复数字（a!=b and b!=c and c!=a ）
sum=0
for i in range(1,5):
    for k in range(1,5):
        for v in range(1,5):

            if ((i!=k) and(k!=v) and (v!=i)):
                print(i,k,v)
                sum+=1
print(sum)
