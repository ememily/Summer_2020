'''Programmer: Emily Morales
Description : 2-  Write a program that allows the user to enter values for a salesperson’s base salary, total sales, and commission rate. The program computes and outputs the salesperson’s pay by adding the base salary to the product of the total sales and commission rate. 
Date:06-24-20'''

BaseSalary = int(input("Please Enter Base Salary"))
TotalSales = int(input("Please Enter Total Sales"))
CommissionSales = int(input("Please Enter Commissions Sales"))
SalespersonPay = int

SalespersonPay = BaseSalary + TotalSales + CommissionSales
print("The base salary of salesperson equals " +str(BaseSalary)+ " +" +str(TotalSales)+ " +" +str(CommissionSales)+ " =" +str(SalespersonPay))
