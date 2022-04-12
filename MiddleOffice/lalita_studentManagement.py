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
    print("Add New Student")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    phone_number = int(input("Enter Phone Number :-"))
    print("New Student is added")
elif(choice == 2):
    name = input("Enter Name of Student:- ")
    print("Delete Student")
elif(choice == 3):
    name = input("Enter Name of Student:- ")
    print("It should display student Name",name)

else:
    print("Invalid Choice")