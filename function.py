# msg="Welcome to itp"
# print(msg.upper())
# print(msg.lower())
# print(msg.find("to"))
# print(msg.count("o"))#to check the character in given string
# print(msg.endswith("itp"))

# Decision control structure
#
# 1.selection control structure- if,if/else,nested if /else
# 2.branching control structure -switch case
# 3.looping control structure-for loop,while loop
# if condition:
#     statement
# ---------------------------------------------------------------------------------------------------------------------
# accept any number from user and check given number is even or odd

# n=int(input("Enter a number"))
# if n%2==0:
#     print("The number is even")
# else:
#     print("The number is odd")
# ---------------------------------------------------------------------------------------------------------------------
# #accept basic salary from user if basic salary>=10000 the hr -10% of basic salary ta -5% of basic salary
# #bonus-15000 otherwise hra -1500,ta-2000,bonus-1000
# #then find out nest-sal =bs+hra+bonus
#
# bs=int(input("Enter a basic salary"))
#
# if bs>=10000:
#     Hr=0.1*bs
#     Ta=0.5*bs
#     Bonus=15000
#     NS=bs+Hr+Ta+Bonus
# else :
#     Hr = 1.5 * bs
#     Ta = 2 * bs
#     Bonus = 1000
#     NS = bs + Hr + Ta + Bonus
# print("Hr\t     Ta\t    Bonus\t   NS")
# print(f"{Hr}\t {Ta}\t {Bonus}\t {NS}\t")
# ---------------------------------------------------------------------------------------------------------------------
# accept any char from user and print corresponding colour name
# col=input("Enter any a character")
#
# if col=='p' or col=='P':
#     print("The colour is pink")
# elif col=='r' or col=='R':
#     print("The colour is Red")
# elif col=='y' or col=='Y':
#     print("The colour is yellow")
# else:
#     print("Wrong character")
# ----------------------------------------------------------------------------------------------------------------------
# To check given year is leap or not

# year=int(input("Enter a year"))
# if year%4==0 and year%100!=0 or year%400==0:
#     print("leap year")
# else:
#     print("year is not leap")
# -----------------------------------------------------------------------------------------------------------------------
# name=input("Enter a name of student:")
# rollno=int(input("Enter a rollno of student:"))
# sub1=int(input("Enter a mark of 1 subject:"))
# sub2=int(input("Enter a mark of 2 subject:"))
# sub3=int(input("Enter a mark of 3  subject:"))
#
# total=sub1+sub2+sub3
# per=total/3
# print(f"The total mark of student:{total}")
# print(f"The total per of student:{per}")
#
# if per>=70:
#     print("distiction")
# elif per>=60:
#     print("first class")
# elif per >=50:
#     print("second class")
# elif per>=40:
#     print("pass class")
# else:
#     print("Fail")
# ------------------------------------------------------------------------------------------------------------------------
# 1 Design Half Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4  ex  - 56/6
# Your program should take operator  and the two numbers as input from the user
# and then return the result

# a,b = [int (x) for x in input("enter 2 nos").split()]
# opr = input("enter any character")
# if a==45 and b==3 and opr=='*':
# print("555")
# elif a==56 and b==9 and opr=='+':
# print("77")
# elif a==56 and b==6 and opr=='/':
# print("4")
# elif opr=='+':
# print(a+b)
# elif opr=='-':
# print(a-b)
# elif opr=='*':
# print(a*b)
# elif opr=='/':
# print(a/b)
# else:
# print("wrong operator")
# ---------------------------------------------------------------------------------------------------------------------
# Write a Python program to find the eligibility of admission for a professional course based on the following criteria:
# Marks in Maths >=65 Marks in Phy >=55 Marks in Chem>=50 Total in all three subject >=180

# m,p,c=[int (x) for x in input("enter 3 values").split()]
# total =m+p+c
# if m>=65 and p>=55 and c>=50 and total>=180:
#     print("Eligible for admission")
# else:
#     print("Not Eligible for admission")
# ---------------------------------------------------------------------------------------------------------------------
# 3.print greatest of 3 nos = a=30,b=40,c=50
# a,b,c=[int (x) for x in input("Enter values of a,b,c").split()]
#
# if a>b and a>c:
#      print("A is greater")
# elif b>c:
#     print("B is greater")
# else:
#     print("C is greater")
# ---------------------------------------------------------------------------------------------------------------------
# 4. If the three sides of a triangle are entered through the keyboard,
# write a program to check whether thr triangle is valid or not.
# The triangle is valid if the sum of two sides is greater than the largest of the three sides.
#
# a,b,c=[int (x) for x in input("enter 3 values").split()]
#
# if a>b and a>c and b+c>a:
#     print("Triangle is valid")
# elif b>c and b>a and a+c>b:
#     print("Triangle is valid")
# elif c>a and c>b and b+a>c:
#     print("Triangle is valid")
# else:
#     print("Triangle is invalid")
# ----------------------------------------------------------------------------------------------------------------------
# 5. Write a program to input any alphabet and check whether it is vowel or consonant.

# ch = input("enter any character")
# if ch=='a' or ch=='e' or ch=='i' or ch=='o' and ch=='u':
#     print("character is vowel")
# else:
#     print("character is consonants")
# ---------------------------------------------------------------------------------------------------------------------
# 6.Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.
# Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

# p,c,b,m,com=[int (x)for x in input("Enter a five subject marks").split()]
# total=p+c+b+m+com
# per=total/5
# if per>=90:
#    print("Grade A")
# elif per>=80:
#     print("Grade B")
# elif per>=70:
#     print("Grade C")
# elif per>=60:
#     print("Grade D")
# elif per>=40:
#     print("Grade E")
# else:
#     print("Grade F")
# ---------------------------------------------------------------------------------------------------------------------
# 4. To ask user that how many days in a leap year.

# a. if user will get correct ans -then
# print "You have cleared the first level" and
# ask again another que "What month has an extra day in leap year?"
# if user will get correct answer then display message
# "Congratulations !!You have cleared the test" otherwise
# "You have failed the test".

# b.otherwise print following
# msg- "Your input is wrong, please try again."

# user = int(input("How many days in a leap year? "))
#
# if user == 366:
#     print("You have cleared the first level")
#     user = input("What month has an extra day in a leap year? ")
#
#     if user == "february":
#         print("Congratulations!! You have cleared the test.")
#     else:
#         print("You have failed the test.")
# else:
#     print("Your input is wrong, please try again.")


# Watch War movie -
# Ask user's name and age
# if user's name start with ('a' or 'A') and age is above 20 then
# print 'You can watch war movie'
# Else print  'sorry, you cannot watch war movie'

# name=input("Enter name")
# age=int(input('Enter age'))
# if name[0]=='a' or name[0]=='A' and age>20:
#      print('You can watch war movie')
# else:
#     print('sorry, you cannot watch war movie')










