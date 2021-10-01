#计算BMI
weight = input('输入你的体重')
high = input('输入你的身高')

weight = float(weight)
high = float(high)/100

bmi = weight/high/high

print('你的BMI是',bmi)