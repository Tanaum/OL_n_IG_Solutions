Evening  =[[False, True]*20]*10 #Right now all of the seats are available

#Coutns booked seats
Booked = 0
for i in range(10):
    for j in range(20):
        if Evening[i][j] == True:
            Booked = Booked + 1
print('Booked:', Booked)

#Loop for validation
#REPEAT...UNTIL could have been used but that is not a feature in Python
print("Enter number of seats.")
print("Four seats can be booked at a time")
NumberSeats = float(input())
while NumberSeats<= 0 or NumberSeats>4 or NumberSeats != round(NumberSeats):
    print("Please re-enter number of seats.")
    print("Four seats can be booked at a time")
    NumberSeats = float(input())

#Checks if enough seats are available
Available = 200 - Booked
if Available<NumberSeats: #If user wants more seats than available
    if Available == 0:
        print("Houseful")
    else:
        print(Available,"seats available")
else:
    for Seat in range(int(NumberSeats)):
        Evening[(Booked+Seat)%20][(Booked+Seat)//20] = True
        print('Row:',(Booked+Seat)%20)
        print("Seat:",(Booked+Seat)//20)