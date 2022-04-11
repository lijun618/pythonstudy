#test1: 有4个数字1/2/3/4，能组成多少个互不相同且没有重复数字的三位数，并打印出来各是多少
# Tips：遍历for循环 + 判断非重复(a!=b and b!=c and c!=a) 
'''list1=[1,2,3,4]
for i in list1:
    print(i)
'''
sum= 0
for i in range(1,5):
    for k in range(1,5):
        for v in range(1,5):
            if ((i!=k) and (k!=v)and (v!=i)):
                print(i,k,v)
                sum=sum+1
print(sum)
