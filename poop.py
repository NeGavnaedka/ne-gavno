import math  #подключение библиотеки мат функций
a = int(input("введите сторону a:"))
b = int(input("введите сторону b:"))
c = int(input("введите сторону c:"))
p = ((a+b+c)/2)
print("полупериметр треугольника:", p)
s = math.sqrt(p*(p-a)*(p-b)*(p-c))
s= print("площадь треугольника:", s)