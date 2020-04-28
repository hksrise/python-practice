## this is the python code ....
#for i in range(4):
#    for j in range(4-i):
#        print('#', end="")
#              
#    print()          
#    
#    num1 = 2
#    num2 = 4
#    sum = num1 + num2
#    print("Sum of {0} and {1} is {2}". format(num1,num2,sum))
#    
#    number1 = input("First Number :")
#    number2 = input("\n Second Number:")
#    
#    sum = float(number1) + float(number2)
#    
#    print(sum)
#    
#    
#    def fact(n):
#        
#    x = input("facorial of :")
#    result = fact(x)
#    
#    print(result)
#    
#    a = 2
#    a = 4
#    a = 6
#    print(a + a + a)
#    
#    for n in range(20):
#        print(2 ** n, end = "")
#        
#        
# for x in range(20):
#     if x%2 == 0:
#         print(x, end = " ")
#         
#     else:
#         print('Odd', end = " ")
#         
#
# x = range(1,23)
#   x* = 10
# print(list(x))
# 
# x = range(1,21)
# print(list(map(str, x)))
# 
# d = {"a":1, "b":2, "c":3}
# dict = ((key,value) for key, values in d.items() if values <=1)
# print(d)
# 
# from pprint import pprint
# d = {"a" : list(range(1,11)), "b" : list(range(11,21)), "c" : list(range(21,31))}
# pprint(d)
# 
# from pprint import pprint
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# pprint(['b'][2])
# 
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# for key, values in d.items():
#     print(key, "Has Values", value)
#     
#     
# d = {"a" : list(range(1,11)), "b" : list(range(11, 21)), "c" : list(range(21, 31))}
# for key, values in d.items():
#     print(key, "Has Values", value)

#for i in range(100,0,-4):
#    print(i, end = ' ')

#word = 'python'
#for n in word:
#    print (n,end = ' ')

#Sum of the List
#data = [0,1,2,3,4,10,22]
#total = 0
#print(data[5])
#data_1 =[]
#for num in data:
#    total = total + num
#    print("The sum of data is:",total,end=' ')
#total_2 = sum(data)
#print("The sum is:",total_2)

#find_max = 0
#for num in data:
#    if num>find_max:
#        find_max = num
#print("Maximum value is:",find_max)
#print("The maximum value using max fundtion is:", max(data))

#
#my_list=[11,21,31,41,51,61]
#for i in range(5):
#    print(my_list[i])
#    print(my_list[i+1])
#    print()
    

#Bubble Sort
#data = [23,87,34,65,76,54]
#data_copy= data[:]
#for i in range(len(data_copy)):
#    for j in range(0, len(data_copy)-i-1):
#        if data_copy[j]>data_copy[j+1]:
#            data_copy[j],data_copy[j+1] = data_copy[j+1],data_copy[j]
#print(data_copy)   
#print(sorted(data))        

#List Methods
#my_list = [21,45,78,3,56]
#my_list.reverse()
#print(my_list)

#While Loop
#n = 10
#while n>0:
#    print(n)
#    n=n-1

#Ages for people in your class
#user_input = int(input("Please enter ages of people. From -1 to end:"))
#ages = []
#while user_input > 0:
#    ages.append(user_input)
#    user_input = int(input("The next age is :"))
#print("The ages are:", ages)    
 

#F Stirng & Counter in a While loop
#count = 0
#class_names =[]
#names = str(input("Please enter name and stop:"))
#while names != "n":
#    count += 1
#    class_names.append(names)
#    print(f"{names} has been added")
#    names = str(input("Next name: "))
#print(f" There are {count} in the class and their names are {class_names[0]} and {class_names[1]}" ) 

# Modulous FizzBuzz
#n = 100
#for i in range(1, n+1):
#    if i % 3 == 0 and i % 5 == 0:
#        print(i,"FizzBuzz")
#    elif i % 5 == 0:
#        print(i,"Fizz")
#    elif i % 3 == 0:
#        print(i,"Buzz")
#    else :
#        print(i)        
   
#Odd or Even
#
#number = int(input("Please enter the number:"))
#if number % 2 == 0:
#    print("Even")
#else:
#    print ("Odd")    

#Numbers between 1 and 100 and count the numbers from lower to higher number

#num_1 = int(input("Please enter the 1st number:"))
#num_2 = int(input("Please enter the 2nd number:"))
#
#while num_1<1 or num_2<1 or num_1>100 or num_2>100 or num_1 == num_2:
#    print("Numbers must be between 1 and 100, please try again:")
#    num_1 = int(input("Please enter the 1st number again:"))
#    num_2 = int(input("Please enter the 2nd number again:"))
#    
#if num_1<num_2:
#    for i in range (num_1, num_2+1):
#        print(i,end=" ")
#        
#if num_2<num_1:
#    for i in range (num_2, num_1+1):
#        print(i, end=" ")        
    
#Ask the use to enter a string and print eh recerse of that string
#
#word = input("Please enter a word:")
#reverse_string = " "
#
#for char in word:
#    reverse_string = char + reverse_string # The orders of the variables is crucial
#    
#print(reverse_string)   
#print(word[::-1]) #Easier way to reverse the string


#Ask a user to input number between 1 and 12 and then display time table for that number using .isdigit()

#user_input = input("Please enter the number between 1 and 12:")
#
#while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) > 12):
#    print("Please enter a number between 1 and 12")
#    user_input = input("Please make selection:")
#    
#user_input = int(user_input) 
#
#print(f"This is the {user_input} times table: ")
#
#for i in range(1,13):
#    print(f"{i} x {user_input} = {i*user_input}")
    

#Ammed the previous problem such that you don't ask for user input an dprint times table between 1 and 12

#for i in range(1,13):
#    print(f"This is the {i} times table")
#    
#    for j in range(1,13):
#        print(f"{j} x {i} = {j*i}")

#Ask the user to put a sequence of numbers and find their mean

#user_input = input("Please enter the number and type exit to stop:")
#
#numbers= []
#while user_input.lower() != "exit" :
#    while not user_input.isdigit():
#        print("That is not a number, numbers only pls :")
#        user_input = input("Please try again")
#        
#    numbers.append(int(user_input))
#    user_input = input("Please enter next number:")
#print("The mean is :",sum(numbers)/len(numbers))    


#Write a code to print the user input factorial of a number
#
#n = int(input("Please enter the number:"))
#
#fact = 1
#
#for i in range(1,n+1):
#    fact = fact * i
#print(fact)    


#Write a code to calucalte Fibonacci numbers. Create a list of the 1st 20 Fibonacci numbers

#n= 20
#a= 0
#b=1
#fib_nums = []
#for i in range(n):
#    fib_nums.append(a)
#    a,b = b,a+b
#    
#print(f"The first {n} Fibonacci numbers are {fib_nums}")    

#Print an "F" using a '*"

#star = '*'
#
#for i in range (1,7):
#    for j in range(1,6):
#        if i == 1 and j < 6:
#            print(star,end="")
#        elif i == 2 and j == 1:
#            print()
#            print(star)
#        elif i == 3 and j < 5:
#            print(star,end="")
#        elif i == 4 and j == 1:
#            print()
#            print(star)
#        elif i == 5 and j == 1:
#            print(star)
#        elif i == 6 and j == 1:
#            print(star)

    