'''Programmer : Emily Morales
Description   : Have a user to enter a number. Write some conditional statement to check whether the number entered by the user is even or odd.
Date         : 6/26/20'''


OddNumber = int(input("Enter a number:"))

EvenNumber = OddNumber % 2


if EvenNumber >0 :
    print("Odd Number")
else:
    print("Even Number")
