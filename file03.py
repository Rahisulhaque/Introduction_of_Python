def     write_input(filename):
	outFile = open(str(filename), 'w')
	number_of_input = int(input(" Please, enter how many numbers you are going to enter: "))
	count = 0
	while(count < number_of_input):
		user_input= int(input("Enter you number: "))
		count += 1
		outFile.write(str(user_input) + '\s')
	outFile.close()


write_input("TESTFILE")