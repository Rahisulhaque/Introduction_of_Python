##############################################################################################
#                                                                                            #
#                          CS 87 A, Python Programming                                       #
#                      This code is written by Rahisul Haque                                 #
#                           e-mail: rahisul@icloud.com                                       #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################

def get_int():
	try:
		myInt = int(input("Please enter your an integer: "))
		return myInt
	except(ValueError):
		print ">>>>>You have enter a wrong input<<<<<<"


def write_input(filename):
	 
	myInput = int(input("Please tell me how many nunmber you want to put: "))
	outfile = open(filename + ".txt", 'w')
	count = 1
	while( count <= myInput):
		
		outfile.write(str(get_int()) + '\n')

		count += 1

	outfile.close()

def read_output(filename):
	
	infile = open(filename + ".txt", 'r')
	retrived_str = infile.read()
	print retrived_str
    

def main():
	inputfile_name = str(raw_input("PLease name your file you wanna create: : "))
	write_input(inputfile_name)
	outputfile_name = str(raw_input("PLease name your file , you wanna open: "))
	read_output(outputfile_name)
main()
