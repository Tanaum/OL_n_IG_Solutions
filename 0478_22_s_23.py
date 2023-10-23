Account = [
    ['A', 'abc'],
    ['person', '123'],
    ['human', 'xyz789']
]

AccDetails = [
    [-500.00, 100.00, 200.00],
    [100.00, 100.00, 200.00],
    [50000.00, 100.00, 200.00]
]

Size = len(Account)-1

#validation of account ID
def AccExists(AccID):
    if AccID < 0 or AccID > Size:
        return False
    else:
        return True

def Login(name, password, AccID):
    if Account[AccID][0] != name or Account[AccID][1] != password:
        return False
    else:
        return True
#'procedures' for all four actions
def DisplayBalance(AccID):
    print(f'\nThe balance is { AccDetails[AccID][0]}\n')
def WithDrawMoney(AccID):
    if AccDetails[AccID][0] >= -(AccDetails[AccID][1]):
        withdraw_amount = float(input('\nHow much would you like to withdraw? '))
        while withdraw_amount>AccDetails[AccID][2]:
            print('\nYou can only withdraw',AccDetails[AccID][2])
            withdraw_amount = float(input(''))
        AccDetails[AccID][0] -= withdraw_amount
        print(f'\n{withdraw_amount} has been successfully withdrawn from your account\n')
    else:
        print('\nYou have reached the overdraft limit. To deposit money, press 3.\n')
def DepositMoney(AccID):
    deposit_money = float(input('\nHow much would you like to deposit? '))
    AccDetails[AccID][0] += deposit_money
    print(f'\n{deposit_money} have been successfully deposited\n')
#test
cusID = int(input('Enter account ID: '))
if AccExists(cusID):
    name  = input('Enter name: ')
    password = input('Enter password: ')
    if Login(name, password, cusID):
        #display menu
        option = 0
        while option != 4:
            option = int(input('''Enter 1 to display balance
Enter 2 to withdraw money
Enter 3 to deposit money
Enter 4 to exit
'''))
            if option == 1:
                DisplayBalance(cusID)
            elif option == 2:
                WithDrawMoney(cusID)
            elif option == 3:
                DepositMoney(cusID)
            else:
                print('You can only enter 1, 2, 3, or 4.')
    else:
        print('Incorrect name or password.')
else:
    print('Incorrect accout ID/Account with this ID does not exist')