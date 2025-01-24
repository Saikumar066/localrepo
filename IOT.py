#Program1
# name = input("Enter a name:")
# time = int(input("How many times a name should print:"))
# # while (time>0):
# #     print(name)
# #     time = time-1

# for val in range(time):
#     print(name)


#Program2
# num1 = int(input("Enter a numaerator for division:"))
# num2 = int(input("Enter a denominator for division:"))


# try:
#     div = num1/num2
#     print("the result is",div)

# except ZeroDivisionError:
#     print("Denominator cannot be zero")

# finally:
#     print("Yes program completed")

#Program3
# from datetime import datetime
# import time
# for val in range(10):
   
#     timeonly = datetime.now().strftime("%H:%M:%S")
#     time.sleep(10)
#     print(timeonly)
#     print("hello!")


#Program4

# Filename = input("Enter a file name:")
# with open (Filename,"r") as file:
#     for line in file:
#         print("wordcount:",len(line.split())) 