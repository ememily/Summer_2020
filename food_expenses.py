'''Programmer : Emily Morales
Description : Write a program to accept the food expenses of 3 Guests (one at a time). Using Accumulation concept, calculate and display the total expenses from all  3 guests combined. 
Date : 06/27/20'''

GuestOne = "Emily"
GuestTwo = "Seiry"
GuestThree = "Connor"

ExpensesOne = int
ExpensesOne = int(input("Enter food expenses for "+str(GuestOne)))
ExpensesTwo = int
ExpensesTwo = int(input("Enter food expenses for "+str(GuestTwo)))
ExpensesThree = int
ExpensesThree =int(input("Enter food expenses for "+str(GuestThree)))

Total = ExpensesOne + ExpensesTwo + ExpensesThree



print("The expense of all guests is "+str(ExpensesOne) + "+" +str(ExpensesTwo) + "+"+ str(ExpensesThree)+ "=" +str(Total))
