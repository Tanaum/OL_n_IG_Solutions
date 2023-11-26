#Arrays used in the question

Days = ['Monday','Tuesday','Wednseday','Thursday','Friday','Saturday','Sunday']
Readings =[['']*24]*7
AverageTemp = ['']*7
###############################################################################
Farenheit_Readings = ['']*7
MAX_TEMP = 50.0
MIN_TEMP = -20.0

for day in range(len(Days)):
    total = 0
    for hour in range(24):
        temp = float(input(f'Enter temperature for hour {hour} of day {Days[day]}: ')) 
        while temp<MIN_TEMP or temp>MAX_TEMP:
            print(f'Temperature can on be between {MIN_TEMP}C and {MAX_TEMP}C inclusive')
            temp = float(input('Please enter correct reading: '))
        Readings[day][hour] = temp
    for reading in range(len(Readings[day])):
        total+= Readings[day][reading]
    AverageTemp[day] = round((total/24),1)

for celcius_reading in range(len(AverageTemp)):
    Farenheit = (AverageTemp[celcius_reading]*(9/5))+32
    Farenheit_Readings[celcius_reading] = round(Farenheit,1)

for i in range(len(Days)):
    print(f'Average temperature on {Days[i]}: {AverageTemp[i]}C or {Farenheit_Readings[i]}F')

faren_total = 0
celcius_total = 0
for i in range(len(AverageTemp)):
    celcius_total+=AverageTemp[i]
    faren_total+=Farenheit_Readings[i]
faren_ave, cel_ave = round((faren_total/7),1), round((celcius_total/7),1)

print(f'Overall average: {cel_ave}C or {faren_ave}F')