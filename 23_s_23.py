#IG Paper 23/May/June/2023

Contacts = []
    
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
                add(Contacts)
                bubble_sort(Contacts)
            elif choice==2:
                display(Contacts)
            elif choice==3:
                delete(Contacts)
            elif choice == 4:
                print('Bye!')
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
    
#validates choice
def valid(choice):
    if choice in ['1','2','3','4']:
        return True 
    else:
        return False 

#validates the number of contacts 
def validation(n):
    if n<=5 and n>=1: 
        return True
    else:
        return False

#adds new contacts
def add(list):
    global CurrentSize
    num_of_contacts = int(input('Enter contacts (1-5): '))
    if validation(num_of_contacts):
        if CurrentSize + num_of_contacts <=max_contacts:
            for contact in range(num_of_contacts):
                name = input('Enter full name (last name, first name): ')
                number = input('Enter telephone number: ')
                Contacts.append([name,number])
                CurrentSize+=1
        else:
            print(f'Too many contacts. You can only enter {max_contacts-CurrentSize} more contacts.')
    else:
        print('Please enter a valid option')

#sorts the contacts using bubble sort
def bubble_sort(list):
    global CurrentSize

    if CurrentSize>=2:
        upper = len(list)
        lower = 0
        swap = True
        while swap == True and upper>lower:
            swap=False
            for row in range(upper-1):
                if list[row][0]>list[row+1][0]:
                    temporary = list[row][0]
                    list[row][0]=list[row+1][0]
                    list[row+1][0]=temporary
                    temporary2 = list[row][1]
                    list[row][1]=list[row+1][1]
                    list[row+1][1]=temporary2
                    swap=True
        return list

#displays all of the contacts
def display(list):
    global CurrentSize

    if CurrentSize>=2:
        for row in range(CurrentSize):
            print(f'Name: {list[row][0]}\nTelephone Number: {list[row][1]}')
    else:
        print('Too few contacts.')

#deletes all of the contacts       
def delete(list):
    global CurrentSize
    list.clear()
    CurrentSize = 0

if __name__ == '__main__':
    main()