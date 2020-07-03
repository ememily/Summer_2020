'''Programmer: Emily Morales
Description: PayCheck
Write a program to collect the following data from the user.
1)    User last name
2)    User First Name
3)    Number of Hours worked.
4)    Hourly-wage
 
Calculate the gross wage based on the formula:
Gross wage is number of hours worked multiplied by hourly-wage.
Hint: You use the symbol * for multiplication.
 
Output: Display the user name and gross wage.

Date:06/27/20'''

userlastname = input("What is your lastname?")
userfirstname = input("What is your firstname?")
HoursWorked = float(input("How many hours do you work?"))
HourlyWage = float(input("What is your hourly wage?"))

GrossWage = round(HourlyWage * HoursWorked)


print("Hello," ' '+str(userfirstname)+' '+str(userlastname)+' '+str("your total gross wage is")+' '+str(GrossWage))
print("Thank you")
