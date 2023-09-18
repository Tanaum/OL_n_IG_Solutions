#Tanaum Masooma, O3-B

StudentName = ['Kate', 'Catherine', 'Aliha', 'Umaima', 'Anaya', 'Momin']
StudentMark = [
    [71,73,80],
    [60,90,15],
    [50,50,20],
    [40,30,47],
    [58,85,90],
    [10,20,10]
]

TotalMarks = []
Average = []

SubNo = 3

distinctionNo = 0
meritNo= 0
passNo = 0
failNo=0

#calculating total
for student in range(len(StudentName)):
    total =0
    for subject in range(SubNo):
        total+=StudentMark[student][subject]
    TotalMarks.append(total)

#calculating average
for total in range(len(TotalMarks)):
    average = round((TotalMarks[total]/SubNo))
    Average.append(average)

#outputting grades, names, etc of each student
for student in range(len(StudentName)):
    print('Name:', StudentName[student])
    print('Combined total marks:', TotalMarks[student])
    print('Average marks:',Average[student])
    if Average[student] >=70:
        distinctionNo+=1
        print('Grade awarded: Distinction\n')
    elif Average[student] >=55:
        meritNo+=1
        print('Grade awarded: Merit\n')
    elif Average[student] >=40:
        passNo+=1
        print('Grade awarded: Pass\n')
    else:
        failNo+=1
        print('Grade awarded: Fail\n')

print('Distinctions:',distinctionNo)
print('Merits:',meritNo)
print('Passes',passNo)
print('Fails:',failNo)

#Tanaum Masooma, O3-B