#O LEVELS SPECIMEN PAPER 2B

#DATA IN THE QUESTION:
Patient = ['Luke','Veronica', 'Marinette', 'Adrien', 'Gabriel', 'Alya']
Readings = [
	[32.5, 60],
	[31.6, 55],
	[37.2, 100],
	[32.0, 101],
	[37.3, 70],
	[40.5, 500]	
]

#question states that we should write *a* procedure so i'm only gonna write one procedure
def hospital(id):
	if id in range(1000):
		print(f'Name: {Patient[id]}')
		if (Readings[id][0] >= 31.6 and Readings[id][0]<= 37.2) and Readings[id][1] in range(55, 101):
			print('Normal readings')
		elif (Readings[id][0] >= 31.6 and Readings[id][0]<= 37.2) and Readings[id][1] not in range(55, 101):
			print('Warning. Pulse.')
		elif not(Readings[id][0] >= 31.6 and Readings[id][0]<= 37.2) and Readings[id][1] in range(55, 101):
			print('Warning. Temperature.')
		else:
			print('Severe Warning.')
		exit()
	else:
		print('Invalid hospital number.')
		exit()

#test
hospital_number = int(input('Enter hospital number: ').strip())
hospital(hospital_number)