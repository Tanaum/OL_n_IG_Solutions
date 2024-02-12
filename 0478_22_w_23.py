WoodType = ['']*3
Price = ['']*3
Customers = ['']*100
Quotations = [['']*100]*5

#Populating the arrays
WoodType[0] = "Laminate"
WoodType[1] = "Pine"
WoodType[2] = "Oak"
Price[0] = 29.99
Price[1] = 39.99
Price[2] = 24.99

#Loop to get information from customers
for Customer in range(100):
    Customers[Customer] = input("Enter your name: ")

    #Validations
    print('The floor must be a rectangle')
    Width = float(input("Enter the wisth in meters. It should be between 1.5 and 10.0 inclusive"))
    Length = float(input("Enter the wisth in meters. It should be between 1.5 and 10.0 inclusive"))
    while (Width<1.5 or Width>10.0) or (Length<1.5 or Length>10.0) or Length == Width:
            print("Re-enter dimensions")
            print('The floor must be a rectangle')
            Width = float(input("Enter the wisth in meters. It should be between 1.5 and 10.0 inclusive. "))
            Length = float(input("Enter the wisth in meters. It should be between 1.5 and 10.0 inclusive. "))

    #Choice of wood
    WoodChoice = input('What type of would you like? Laminate, Pine, or Oak? ')

    #Find wood's price
    for Wood in range(3):
        WoodPrice = Price[Wood]
        Index = Wood

    #Total cost
    Total = WoodPrice * Width*Length
    
    #Storing data in array
    Quotations[Customer][0] = round(Length,1)
    Quotations[Customer][1] = round(Width,1)
    Quotations[Customer][2] = round((Length*Width))
    Quotations[Customer][3] = Index
    Quotations[Customer][4] = round(Total,2)

    #Final outputs
    print("Name:",Customers[Customer])
    print("Choice of wood:",WoodType[Index])
    print("Total price:",round(Total,2))