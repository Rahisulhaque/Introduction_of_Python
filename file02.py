def writeNames():
	NameFile = open('myschool.txt', 'w')

	NameFile.write('42\n')
	NameFile.write('Santa Monica College\n')
	NameFile.write('Jahangirnagar University\n')
	NameFile.write('Rajshahi Cadet College\n')


	NameFile.close()

def readNames():
	
	Namefile = open('myschool.txt', 'r')

	myshool0 = Namefile.readline()
	myshool1 = Namefile.readline()
	myshool2 = Namefile.readline()
	myshool3 = Namefile.readline()

	print myshool0, myshool1, myshool2, myshool3

	Namefile.close()

def main():
	writeNames()
	readNames()
	


main()