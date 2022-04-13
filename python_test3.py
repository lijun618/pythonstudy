# 随意输入三个数 从大到小排序
lst1=[]
for i in range(1,4):
    x=int(input("请输入一个数字:"))
    lst1.append(x)
lst1.sort(reverse=True)
print(lst1)
