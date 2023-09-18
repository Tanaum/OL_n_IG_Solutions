#IA someday i'll use oop for it

Contacts = {}
    
CurrentSize = 0 

max_contacts = 100
max_contacts_add = 5   

def main():
    while True:
        menu()

        choice = input('Enter a number: ')

        if valid(choice):
            choice = int(choice)
            if choice==1:
                print(add())
            elif choice==2:
                print(display())
            elif choice==3:
                delete()
            elif choice == 4:
                'Bye!'
                exit()
        else:
            print('Invalid option. Choose a valid option')

def menu():
    print('''Menu:
1: Add new contacts.
2: Display all saved contacts.
3: Delete all saved contacts
4: Exit
''')
    
def valid(choice):
    if choice in ['1','2','3','4']:
        return True 
    else:
        return False 
        
def validation(n):
    if n<=5 and n>=1: 
        return True
    else:
        return False
    
def add():
    global CurrentSize
    num_of_contacts = int(input('Enter contacts (1-5): '))
    if validation(num_of_contacts):
        if CurrentSize + num_of_contacts <=max_contacts:
            for contact in range(num_of_contacts):
                name = input('Enter full name (last name, first name): ')
                number = input('Enter telephone number: ')
                Contacts[name]=number
                CurrentSize+=1
        else:
            print(f'Too many contacts. You can only enter {max_contacts-CurrentSize} more contacts.')
    else:
        print('Please enter a valid option')

def display():
    return dict(sorted(Contacts.items()))

def delete():
    Contacts.clear()

if __name__ == '__main__':
    main()