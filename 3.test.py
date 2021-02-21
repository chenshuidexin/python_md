'''
value=float(input("请输入长度为:"))
unit=input("请选择单位:")

if unit == "in" or unit == "英寸":
    print('%f英寸 = %f厘米' % (value,value*2.54))
elif unit == "cm" or unit == "厘米":
    print('%f厘米 = %f英寸'% (value,value/2.45))
else:
    print("请输入有效的单位或数字")
'''
'''
a=float(input("请输入a="))
b=float(input("请输入b="))
c=float(input("请输入c="))
if a+b>c and a+c>b and b+c>a :
    print("周长:%f" % (a+b+c))
    p=(a+b+c)/2
    area=(p*(p-a)*(p-b)*(p-c))**0.5
    print('面积:%f'%(area))
else:
    print("不能构成三角形")
'''

