# Placing a hash tag in front of a line will make the 
# line not execute 
#This is reffered to as a "comment"

'''
Line 1 of block comment 
Line 2 of block comment 
Line 3 of block comment 
'''

"""
Line 1 of block comment 
Line 2 of block comment 
Line 3 of block comment 
"""

"""
A condition is a comparison. 
conditions evaluate a boolean value to e true of false. 
If a condition is true, the following block of code will run. 
A block of code will be indented 

COMPARISONS: 
>    Greater than 
<    Less than 
>=   Greater than or equal to 
<=   Less than or equal to 
==   Equal to 
!=   Not equal to 
 
""" 

mark = int(input("Please enter your test mark"))

if mark >= 90: 
    print("You aced it")
    
elif mark >= 70:
    print("YOu got a B! Good job!")
    
elif mark >= 60: 
    print("Thats a C!")

elif mark >=50:
    Print("You barely made it!")    
    
else: 
    print("You failed!")
    
if (mark >= 0 and mark <= 100):
    print("You have a volid mark")
    
if (mark > 100 or mark < 0):
        print("This is and invalid mark")