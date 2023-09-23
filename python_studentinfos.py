studentinfos = []
print("=" * 30)
print("欢迎进入学生信息系统")
print("=" * 30)

while True:

    # 学生信息查询系统
    # print("=" * 30)
    # print("欢迎进入学生信息系统")
    # print("=" * 30)
    print("1.录入学生信息")
    print("2.修改学生信息")
    print("3.删除学生信息")
    print("4.查询学生信息")
    print("5.退出系统")
    #  1. 系统功能选择
    num = str(input("请输入您要进入的功能对应的数字: "))
    
    #  2. 录入学生信息
    if num == "1":
        stu_name = input("请输入学生的姓名:")
        stu_sex = input("请输入学生的性别:")
        stu_phonenum = input("请输入学生的电话号码:")
        newinfo = {}
        newinfo["name"] = stu_name
        newinfo["sex"] = stu_sex
        newinfo["phonenum"] = stu_phonenum
        studentinfos.append(newinfo)

        print("已录入%s的信息!!!"%(stu_name))


    #  3. 修改学生信息
    elif num == "2":
        stuId = int(input("请输入要修改的学生的序号: "))

        
        stu_name = input("请输入学生的姓名: ")
        stu_sex = input("请输入学生的性别: ")
        stu_phonenum = input("请输入学生的电话号码:")


        studentinfos[stuId-1]["name"] = stu_name
        studentinfos[stuId-1]["sex"] = stu_sex
        studentinfos[stuId-1]["phonenum"] = stu_phonenum

        print("已修改%s的信息!!!" %(stu_name))



    #  4. 删除学生信息
    elif num == "3":
        pass





    #  5. 查询学生信息
    elif num == '4':
        #print(studentinfos)
        print("学生信息如下:")
        print("序号      姓名       性别        电话")
        i = 1
        for tempInfo in studentinfos:
        
            print("%d         %s       %s        %s"%(i, tempInfo["name"], tempInfo["sex"], tempInfo["phonenum"]))
        
            i += 1


    # 6.退出查询系统
    elif num == '5':
        print("您已退出系统！！")
        exit()








    





