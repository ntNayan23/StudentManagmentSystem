print("=========================================\n")
print("  Wainganga College Of engineering  \n")
print("=========================================\n")

print("Choose your Action\n")
print("1.	Add new Student")
print("2.	Delete Student")
print("3. 	Search Student")

choice = int(input("Your input please :"))
print("User have selected: userChoice={}".format(choice))
if(choice == 1):
    print("=========================================\n")
    print("  Wainganga College Of engineering - Add New Student \n")
    print("=========================================\n")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    phoneNumber = int(input("Enter Phone Number :-"))
    print("New Student is added")
elif(choice == 2):
    print("=========================================\n")
    print("  Wainganga College Of engineering - Delete Student \n")
    print("=========================================\n")
    name = input("Enter Name of Student:- ")
    print("Deleted Student")
elif(choice == 3):
    print("=========================================\n")
    print("  Wainganga College Of engineering - search Student \n")
    print("=========================================\n")
    name = input("Enter Name of Student:- ")
    age = input("Enter age of Student:- ")
    phoneNumber = input("Enter phone Number:- ")
    print("Name="+name, "age="+age, "phoneNumber="+phoneNumber)

else:
    print("Invalid Choice")