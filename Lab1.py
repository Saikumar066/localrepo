#addtion of two numbers:
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))
# sum = num1 + num2
# pass
# print("The addition of two numbers is:",sum)

#substraction of two numbers:
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))
# if(num1>num2):
#  substract = num1 - num2
# else:
#  print("Enter Greater number at first.")

# print("The substraction of two numbers is:",substract)

#Multiplication of two numbers:
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))
# multi = num1*num2
# print("The Multiplication of two numbers is:",multi)

#Division of two numbers:
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number('Don't take zero'):"))
# if(num2!=0):
#  divi = num1/num2
#  print("The Division of two numbers is:",divi)
# else:
#     print("The divisor cannot be zero.")
    


#Area of Cricle:
# import math
# r = float(input("Enter a radius:"))
# pi = 3.142
# area = 3.142*r*r
# print(area)

#Area of Rectangle:
# l = float(input("Enter the length of the rectangle:"))
# h = float(input("Enter the height of the rectangle:"))
# area = l*h
# print(area)

#Area of Triangle:
# b = float(input("Enter the breadth of the triangle:"))
# h = float(input("Enter the height of the triangle:"))
# area = 0.5*b*h
# print(area)

#Surface Area of a Cyclinder:
# import math 
# r = int(input("Enter the radius of the cyclinder:"))
# h = int(input("Enter the height of the cyclinder:"))
# pi = 3.142
# area = 2*pi*r*(r+h)
# print(area)

#Area of a Cone:
# import math
# r = int(input("Enter the radius of the cone:"))
# h = int(input("Enter the height of the cone:"))
# pi = 3.142
# area = pi*r*r+h
# print(area)

#SimpleIntrest:
# p = int(input("Enter the Princple amount:"))
# r = int(input("Enter the rate of intrest:"))
# t = int(input("Enter the time period:"))
# Simple = (p*t*r)/100
# print(Simple)

#Compound Interst:
# p = int(input("Enter the Princple amount:"))
# r = float(input("Enter the rate of intrest:"))
# t = int(input("Enter the time period:"))
# n = int(input("Enter the number of times intrest is compounded per year:"))
# Compound = (p*(1+(r/n)))*n*t
# print(Compound)

#area of Square:
# a = int(input("Enter the side of the square:"))
# area = a*a
# print(area)

#area of Cyclinder:
# r = float(input("Enter the radius of the cyclinder:"))
# h = int(input("Enter the height of the cyclinder:"))
# pi = 3.142
# area = pi*r*r*h
# print(area)

#Greatest of two numbers:
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))
# if(num1>num2):
#     print("First number is greater than second number.")
# else:
#     print("Second number is greater than first number.")

#Greatest of three numbers:
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))
# num3 = int(input("Enter a third number:"))
# if(num1>num2):
#     print("First number is greater than second number.")
# elif(num2>num3):
#     print("Second number is greater than third number.")
# elif(num3>num1):
#     print("Third number is greater than first number.")
# else:
#     print("Second number is greater than first number.")

#odd or even:
# num1 = int(input("Enter a number:"))
# if(num1%2==0):
#     print("It is an even number.")
# else:
#     print("Its is an odd number.")

#Prime Number:
# num1 = int(input("Enter a number to check it's a Prime Number or not:"))
# def is_prime(num1):
#     if num1 <= 1:
#         return False
#     for i in range(2, int(num1**0.5) + 1):
#         if num1 % i == 0:  
#             return False

#     return True
# if is_prime(num1):
#     print(f"{num1} is a prime number.")
# else:
#     print(f"{num1} is not a prime number.")


# Positive or negative Number
# num1 = int(input("Enter a Number:"))
# if(num1>0):
#     print("It is a Positive Number.")
# elif(num1==0):
#     print("Null Number.")
# else:
#     print("It is a Negitive number.")


#voiting Eligibility
# age = int(input("Enter a age:"))
# if(age>=18):
#     print("Yes he can vote")
# else:
#     print("Not yet he can't vote.")

#Printing hello with your name
# name = (input("Enter your name:"))
# print("Hello",name)

#Counting no of characters in a string without space
# string = input("Enter a String or a character:")
# nospace = string.replace(" ","")
# char = len(nospace)
# ch = len(string.split())
# print("The no of characters is:",char,ch)


# shape = input("Enter 1.rectangle  2.triangle  3.circle:")
# if(shape == "1"):
#         l = float(input("Enter the length of the rectangle:"))
#         h = float(input("Enter the height of the rectangle:"))
#         area = l*h
#         print("The area of the Rectangle is:",area)
# elif(shape =="2"):
#     b = float(input("Enter the breadth of the triangle:"))
#     h = float(input("Enter the height of the triangle:"))
#     area = 0.5*b*h
#     print("The area of the Triangle is:",area)
# elif(shape == "3"):
#     r = float(input("Enter a radius:"))
#     pi = 3.142
#     area = 3.142*r*r
#     print("The area of the Circle is:",area)
# else:
#     print("Enter a vaid input")

# name = input("Enter a name:")
# time = int(input("How many times a name should print:"))
# print((name + " ")*time)

#This code is for beginners in python."Be Good ALWAYS"

#OOPS Concepts 
#N natural number
# n = int(input("Enter the Number to print the sum of it:"))
# i = 1
# while(i<=n):
#     print(i)
#     i =i+1

#Patterns
# n = int(input("Enter the number:"))
# i = 1
# while(i<=n):
#     print("A" * i)
#     i = i+1


#SuperMethod
# class Car:
#     def __init__(self,type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("Car is Started.")
#     @staticmethod
#     def stop():
#         print("Car is stoped")

# class Bmw(Car):
#     def __init__(self,name,type):
#         self.name= name
#         super().__init__(type)
    
# c1 = Bmw("audi","electric")
# print(c1.type)

#Matrix Addition
# rows = int(input("Enter a number of rows:"))
# col = int(input("Enter a number of column:"))
# print("Enter first matrix row vise:")
# num1 = [[int (x) for x in input().split()] for _ in range(rows)]
# print("Enter second matrix row vise:")
# num2 = [[int (x) for x in input().split()] for _ in range(rows)]

# result = [[num1[i][j] + num2[i][j] for j in range(col)] for i in range(rows)]
# print("Resultant Matrix:")
# for row in result:
#     print(row)


# Matrix Multiplication
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# print("Enter first matrix row-wise:")
# num1 = [[int(x) for x in input().split()] for _ in range(rows)]
# print("Enter second matrix row-wise:")
# num2 = [[int(x) for x in input().split()] for _ in range(cols)] 
# result = [[0 for _ in range(len(num2[0]))] for _ in range(rows)]
# for i in range(rows):  
#     for j in range(len(num2[0])):  
#         for k in range(cols):  
#             result[i][j] += num1[i][k] * num2[k][j]
# print("Resultant Matrix:")
# for row in result:
#     print(row)



# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == "__main__":
#     num = int(input("Enter a number: "))
#     if is_prime(num):
#         print(f"{num} is a prime number.")
#     else:
#         print(f"{num} is not a prime number.")

# def swap_numbers(a, b):
#     return b, a

# if __name__ == "__main__":
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))
    
#     x, y = swap_numbers(x, y)
#     print(f"After swapping: First number = {x}, Second number = {y}")


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# if __name__ == "__main__":
#     arr = list(map(int, input("Enter list elements separated by space: ").split()))
#     target = int(input("Enter the target element: "))
    
#     index = linear_search(arr, target)
#     if index != -1:
#         print(f"Element found at index {index}")
#     else:
#         print("Element not found in the list")

# def fibonacci(n):
#     fib_series = [0, 1]
#     for i in range(2, n):
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series[:n]

# if __name__ == "__main__":
#     n = int(input("Enter the number of Fibonacci terms: "))
#     print("Fibonacci Series:", fibonacci(n))


# def count_words_and_chars(text):
#     num_words = len(text.split())  # Splitting by spaces to count words
#     num_chars = len(text)  # Counting all characters including spaces
#     return num_words, num_chars

# # Input from user
# input_text = input("Enter a string: ")

# # Count words and characters
# words, chars = count_words_and_chars(input_text)

# # Display results
# print(f"Number of words: {words}")
# print(f"Number of characters: {chars}")
