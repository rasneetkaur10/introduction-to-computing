#average of three numbers
number1=int(input("first number:"))
number2=int(input("second number:"))
number3=int(input("third number:"))
result=(number1+number2+number3)/3
print(result , end='\n''\n''\n')

print('xxxxxxxxxxxxxxx' , end='\n''\n''\n')

#calculation of income tax
taxrate=0.2
standarddeduction=int(10000)
grossincome=int(input("enter gross income:"))
numberofdependents=int(input("enter nuber of dependents:"))
dependentdeduction=int(3000)
taxableincome = grossincome - standarddeduction - (dependentdeduction
* numberofdependents)
tax=taxableincome*taxrate
print(taxableincome)
print(tax , end='\n''\n''\n')

print('xxxxxxxxxxxxxxx' , end='\n''\n''\n')

#list of details of students
SID=input("enter student SID:")
Name=input("enter student name:")
Gender=input("enter student gender:")
Coursename=input("enter course name:")
CGPA=input("enter CGPA:")
list=[SID , Name , Gender , Coursename , CGPA]
print("\nList containing multiple values: ")
print(list[0])  
print(list[1])
print(list[2])
print(list[3])
print(list[4] , end='\n''\n''\n')

print('xxxxxxxxxxxxxxx' , end='\n''\n''\n')

#marks list in sorted manner
m1 = int(input("Marks of 1st student : "))
m2 = int(input("Marks of 2nd student : "))
m3 = int(input("Marks of 3rd student : "))
m4 = int(input("Marks of 4th student : "))
m5 = int(input("Marks of 5th student : "))
SortedMarks = [m1, m2, m3, m4, m5]
SortedMarks.sort()
print(SortedMarks , end='\n''\n''\n')

print('xxxxxxxxxxxxxxx' , end='\n''\n''\n')

#list of colours
colour=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(colour)
colour1=colour.copy()
colour.remove(colour[3])
# Removing‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
colour1[3]="Purple"
colour1[4]="Purple"
print(colour)
print(colour1)
