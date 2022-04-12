# 当月奖金bonus根据当月利润profit按比例发放。输入利润I计算应发奖金金额并输出。
profit=float(input("请输入本月利润(万元):"))
print("当月利润额为",profit,"万元")
if 0<profit<=10:
    bonus=profit*10000*0.1
    print("当月应发奖金为:",bonus,"元！")
elif 10<profit<20:
    bonus=(round(0.075*profit+0.25,2))*10000    #10*10000*0.1+(profit-10)*10000*0.075
    print("当月应发奖金为:",bonus,"元！")
elif 20<profit <40:
    bonus =(round(0.125*profit-0.75,2))*10000   #(0.25+profit*0.075)*10000+(profit-20)*10000*0.05
    print("当月应发奖金为:",bonus,"元！")
elif 40<profit <60:
    bonus = (round(0.155*profit-1.95,2))*10000  #(0.125*profit -0.75)*10000+(profit-40)*0.03*10000
    print("当月应发奖金为:",bonus ,"元！")
elif 60<profit <100:
    bonus =(round(0.170*profit-2.85,2))*10000   #(0.155*profit -1.95)*10000+(profit-60)*0.015*10000
    print("当月应发奖金为:",bonus,"元！")
elif profit >100:
    bonus =(round(0.18*profit-3.85,2))*10000    #(0.17*profit-2.85)*10000+(profit-100)0.01*10000
    print("当月应发奖金为:",bonus ,"元！")
else:
    print("输入有误，请再次输入当月利润！")
