def Home():
    name = input("enter your name")
    age = input("enter your age")
    phone_no = input("enter your phone_no")
    print(name, age, phone_no)


def Header():
    print('''* \nStudent Management System\n***''')


def Add():
    print("Add New Student")
    name = input("Enter Name :- ")
    age = int(input("Enter Age :- "))
    phone_number = int(input("Enter Phone Number :-"))
    print("New Student is added")


def Delete():
    name = input("Enter Name of Student:- ")
    print("Delete Student")


def Display():
    name = input("Enter Name of Student:- ")
    print("It should display student Name", name)
def choice():
    print(''' 1.Add New Student\n 2.Delete Student\n 3.Search Student''')
    choice = int(input("Enter You choice :- "))
    return choice


if __name__ == "__main__":
    Header()
    ch = choice()
    if (ch== 1):
        Header()
        Add()
    elif (ch== 2):
        Header()
        Delete()
    elif (ch== 3):
        Header()
        Display()
    else:
        print("Invalid Choice")