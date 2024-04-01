import regex as re


"""

Todo 1
write a function called phonebook
this function should ask which action you want to perform
i  add a contact
ii delete a contact
iii search a contact
iv exit

Todo 2 add a contact
create a function which accept an input
i enter name
ii enter phone_no
iii enter address
save the output in a txt file

To do 3 search a contact
i read through a txt file
ii input: which contact do you want to see?: 
iii output the contact search for only


"""

path = "C:\\Users\\Adams\\Desktop\\Software Dev\\my_phonebook.txt"
print("Welcome to Bee quick contact ")
print("To add a contact press 1")
print("To view all contact press 2")
print("To search a contact press 3")
print("To delete a contact press 4")
print("To exit press 5")

def add_contact ():
    while True:
        name = input("Enter name: ")
        phone_no = input("phone_no: ")
        address = input("address: ")
        details  = {name: {"address": address, "phone_no": phone_no}}

        with open("my_phonebook.txt", mode="a") as file:
                    for name, info in details.items():
                        file.write(f"{name}: [{info['phone_no']}, {info['address']}]\n")

        choice = input("Do you want to save another contact? : (y/n): ")
        if choice.lower() == "n" :
            break
        elif choice == "y":
            add_contact()
           
                
        # break

def view_all_contact():
     with open("my_phonebook.txt", mode="r") as file:
        contents = file.read()
        print(contents)

def search():
   with open("my_phonebook.txt", mode="r") as file:
        search = input("which contact are you searching for? ")
        for contents in file:
            if search in contents:
                print(contents)


def delete(path, search_by_name):
    with open(path, 'r') as file:
        lines = file.readlines()
        for i in lines:
            word_chars = re.findall(f'{search_by_name}', i, re.IGNORECASE)
            if len(word_chars) > 0:
                lines.remove(i)
        print(lines)
        new_content = "\n".join(lines)
        with open(path, "w") as file:
            file.write(new_content)

def exit():
    print("exit")


def phone_book():
    while True:
        choice = input("what do you want to do 1,2,3,4,5:  ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_all_contact()
        elif choice == "3":
            search()
        elif choice == "4":
            search_by_name = input('What do you want to delete? ')
            delete(path, search_by_name)    
        else:
            choice == "5"
        break

phone_book()        
