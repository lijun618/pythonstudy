#  冒泡排序： 随机random生成8个整数，按照从小到大的顺序排序后输出

import random
list1= []
for i in range(1,11):

    a = random.randint(0,100)
    #print(a)
    list1.append(a)
    #print(list1[i-1])
    #list1.sort() sort()是列表的方法,可以快速修改原列表使得它按照大小排序。

    i += 1    
#print(list1)

# 冒泡排序
for i in range(len(list1)-1):
    for k in range(len(list1)-i-1):
        if list1[k] > list1[k+1]:
            list1[k],list1[k+1] = list1[k+1],list1[k]
            print(list1)





