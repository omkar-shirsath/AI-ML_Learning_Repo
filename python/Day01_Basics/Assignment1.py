"""

Q1. Write a program that asks the user for their name and age, then prints a
sentence like:

Hello Shradha, you are 21 years old!

"""

name = input("Enter your name : ")
age = int(input("Enter your Age : "))

print(f"Hello {name} , you are {age} years old !")

"""
Q2 . Take two numbers as input from the user and print their sum, difference,
product, and quotient.

"""
num_1 = float(input("Enter 1st number  : "))
num_2 = float(input("Enter 2nd number : "))
print(f"sum : {num_1+num_2} \ndifference : {num_1-num_2} \nproduct : {num_1 * num_2}\nquotient : {num_1/num_2}")

"""
Q3 . Ask the user to enter two integers and one float. Convert them all to floats
and print their average.

"""

num_1 = float(input("Enter first integer : "))
num_2 = float(input("Enter Second integer : "))
num_3 = float(input("Enter the Float value: "))

print(f"Average of all three numbers : {(num_1+num_2+num_3)/3}")

"""
Q4. The user enters a string containing a number (e.g., "45" ).
 Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.
"""

string = "45"
string = int(string)
print(string,type(string))
string = float(string)
print(string,type(string))
string = str(string)
print(string,type(string))

"""
Q5. Evaluate and print the result of the following expression:
x = 10 + 3 * 2 ** 2
Based on what you learnt in the lecture explain why the output is what it is. 

myanswer before runing the condition : 22  ( it uses operatior precedence to solve this )
output: 22 
"""
x = 10 + 3 * 2 ** 2
print(x)

"""
Q6. Write a program to swap values of two numbers entered by the user.

"""

num_1 = int(input("Enter 1st number : "))
num_2 = int(input("Enter 2nd number : "))

print(f"orignal order : {num_1 , num_2}")
temp = num_1
num_1 = num_2
num_2 = temp
print(f"swap order of numbers : {num_1 , num_2}")

"""
Q7 Ask the user for a temperature in Celsius (string input). Convert it to float,
then calculate and print temperature in Fahrenheit.
 
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +32

"""

temp_celsius = input("Enter the temp in Celsius : ")
temp_float = float(temp_celsius)
FahrenheitTemp = (temp_float * (9/5)) +32
print(FahrenheitTemp)

"""
Q8. Take the radius (r) as user input and print the area.
Use the formula: Area = π * r (value of π = 3.14)

"""

r = float(input("radius : "))
Area = 3.14 * r *r
print(f"Area of radius {r} is  : {Area}")

"""
 Q9 Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
compute simple interest:

SI = (P ∗ R ∗ T)/100
"""

p = float(input("Enter Pricipal value : "))
R = float(input("Enter Rate value : "))
T = float(input("Enter Time value : "))

print(f"simple intrest SI = { (p*R*T)/100}")

"""
Q10. Take a decimal number as input (like 45.78 ) and output its:
• integer part - 45
• fractional part - .78

"""

num =float(input("Enter decimal number (eg. 45.78 ) : "))
int_part = int(num)
frac_part = float(num%int_part)
print(f"integer part - {int_part} ")
print(f"fractional part - ", round(frac_part,2))


