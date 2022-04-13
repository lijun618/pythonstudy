# 随意输入整数 从大到小排序

lst1=[]
for i in range(1,8):
    x=int(input("请输入一个数字:"))
    lst1.append(x)
#lst1.sort(reverse=True)
#print(lst1)
n=len(lst1)
#print(n)
#冒泡排序
for i in range(n-1):            #i为排序的轮次
   for k in range (n-i-1):      #k为数据的下标
       if lst1[k]>lst1[k+1]:    # 相邻的两个数比较
           lst1[k],lst1[k+1]=lst1[k+1],lst1[k] #  更换位置
           print(lst1)
           