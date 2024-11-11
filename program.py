#write a progam to print hello world in python
"""print("hello")

# write a program to print single variable and multiple variable in python
#single variable
a = 5
print(a)

#multiple variable
x = 8
y = 7
print(x,y)

#wap to print multiplication,division,addition,subtraction of tow numbers

num1 = 8
num2 = 5
print(num1+num2)
print(num1 - num2)
print(num1*num2)
print(num1/num2)

# wap to perform all the datatypes

name = "avirbhav"
num3 = 45.8941257
age = 20
num5 = 4.74
ch = 'a'
s = True
print(name)
print(num3)
print(age)
print(num5)
print(ch)
print(s)

#wap to print all valid and invalid idetifier rules 
# valid
sum = 8
print(sum)
NAME = "A"
print(NAME)
__name__ = 't'
print(__name__)

# invalid
1variable = 5
my-variable = 4
if = 3
    $ amount = 4

#wap to assigning and reassigning the variable

t = 5
print(t)

t+=5
print(t)

#wap to impliment variable design method with single value to multiple variable and multiple value to multiple variable

dig1 =dig2 = 4

print(dig1)
print(dig2)

dig3 , dig4,dig5 = 5,2,6
print(dig3,dig4,dig5)

#wap to perform logical and membership operator
#logical operator and
x = True
y = False
print(x and y)
# logical operator or
a = True
b= False
print(a or b)

# logical operator not
p = True

print(not p)
# membership operator in
vegetable = ['peas','spinich','cauliflower']
print('peas'in vegetable)
print('ladyfinger'in vegetable)

# membership operator not in

number = [1,8,7,9]
print(4 not in number)
print(8 not in number)

#wap to impliment calculator on behalf of user input and perform all airthmetic operations

userinput = int(input ("Enter your number"))
userinput2 =int( input("Enter next number"))
print('sum', userinput + userinput2)
print('sub', userinput - userinput2)
print('mul' , userinput *userinput2)
print('div' , userinput /userinput2)

# area of square
side = 4
print(side*side)

# area of rectangle

length , breadth = 5,6
print(length*breadth)

# area of cube
a = 6
print(6*a*a)

# area of cuboid
l ,b,h= 4,6,5
print(2*(l*b + b*h + h*l))

# area of circle
radius = 6
print(3.14*radius*radius)

# area of triangle 
base,height = 4,1
print(0.5*base*height)

# wap using if else which number is greter without user input

num1 = 4
num2 = 2
num3 = 8
if num1>num2 and num1>num3 :
    print("num1 is greater")

elif num2>num1 and num2>num3 :
    print("num2 is greater")

elif num3>num1 and num3 >num2 :
    print(" num3 is greater")

else :
    print("invalid")


    # with user input
num1 = int(input("enter your num1: "))
num2 = int(input("enter your num2: "))
num3 = int(input("enter your num3: "))

    
if num1>num2 and num1>num3 :
    print("num1 is greater")

elif num2>num1 and num2>num3 :
    print("num2 is greater")

elif num3>num1 and num3 >num2 :
    print(" num3 is greater")

else :
    print("invalid")

# wap to take input from user ram,shyam, mohan which one is greater

name = input("enter name ")
name2 = input("enter next name ")
name3 = input("enter your next name ")

if name>name2 and name >name  :
    print("name is greater")

elif name2>name and name2 > name3 :
    print("name2is greater")

elif name3>name and name3>name2 :
    print("name3 is greter")

else :
    print("invalid")"""




#printing half pyramid pattern

n= 5
for i in range (n+1,1,-1) :
    for j in range (1,i,1) :
        print("*",end=" ")
    print()
