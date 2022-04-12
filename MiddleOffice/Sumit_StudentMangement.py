print('''------------------------ \nGovernment Polytechnic \n------------------------''' )
print(''' 1.Add New Student\n 2.Delete Student\n 3.Search Student''')
choice =  int(input("Enter You choice :- "))
if(choice == 1):
    print("Add New Student")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    mob_number = int(input("Enter mob_number :-"))
    print("New Student is added")
elif(choice == 2):
    name = input("Enter Name of Student:- ")
    print("Delete Student")
elif(choice == 3):
    name = input("Enter Name of Student:- ")
    print("It should display student Name",name)

else:
    print("Invalid Choice")