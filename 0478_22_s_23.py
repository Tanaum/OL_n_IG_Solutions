#0478/22/M/J/2023
#arrays/lists that are in the question

Account = [
    ['Adam Kent', 'k3ntgobrr'],
    ['Juliette', 'd0ntt0chm3'],
    ['Pip', 't@lkn3rdy70m3']
]

AccDetails = [
    [-500.00, 100.00, 200.00],
    [100.00, 100.00, 200.00],
    [50000.00, 100.00, 200.00]
]

Size = len(Account)

########################################
#validation of account ID
def AccExists(name, password):
    for i in range(len(Account)):
        if Account[i][0]== name and Account[i][1]== password:
            return i
        '''else:
            return -1'''
        
#will reapeat until the existence of the account has been confirmed
name = input('Enter name: ')
password = input('Enter password: ')
valid = AccExists(name, password)
while valid == None:
    print('The name or password is incorrect. Please enter correct name and password')
    name = input('Enter name: ')
    password = input('Enter password: ')
    valid = AccExists(name, password)
#'procedures' for all four actions
def DisplayBalance(AccID):
    print(f'\nThe balance is{ AccDetails[AccID][0]}\n')
def WithDrawMoney(AccID):
    if AccDetails[AccID][0] >= -(AccDetails[AccID][1]):
        withdraw_amount = float(input('\nHow much would you like to withdraw? '))
        while withdraw_amount>AccDetails[AccID][2]:
            print('\nYou can only withdraw',AccDetails[AccID][2])
            withdraw_amount = float(input(''))
        AccDetails[AccID][0] -= withdraw_amount
        print(f'\n{withdraw_amount} has been successfully withdrawn from your account\n')
    else:
        print('\nYou have reached the overdraft limit. To deposit money, press 3.')
def DepositMoney(AccID):
    deposit_money = float(input('\nHow much would you like to deposit? '))
    AccDetails[AccID][0] += deposit_money
    print(f'\n{deposit_money} have been successfully deposited\n')
#display menu
option = 0
while option != 4:
    option = int(input('''Enter 1 to display balance
Enter 2 to withdraw money
Enter 3 to deposit money
Enter 4 to exit
'''))
    if option == 1:
        DisplayBalance(valid)
    elif option == 2:
        WithDrawMoney(valid)
    elif option == 3:
        DepositMoney(valid)