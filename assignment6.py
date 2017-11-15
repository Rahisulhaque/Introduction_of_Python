##############################################################################################
#                                                                                            #
#                          CS 87 A, Python Programming                                       #
#                      This code is written by Rahisul Haque                                 #
#                           e-mail: rahisul@icloud.com                                       #
#                                                                                            #
#                                                                                            #
#                                                                                            #
##############################################################################################



#get_int
def get_int(msg):
	try:
		return int(input(msg))

	except (NameError, TypeError, SyntaxError):
		print " \n \n >>>>>> Seems like you have entered a wrong input! <<<<<<<\n \n"


# temperatue funtion
def    Celsius_to_Fahrenheit( _Celsius ):
	Fahrenheit = (_Celsius * (9/5)) + 32
	print   "%.2f   degree will be  %.2f degree (approx) Fahrenheit." %(_Celsius,Fahrenheit)



# weight function
def    Pounds_to_Kilograms( _Pounds ):
	Kilogram = ( _Pounds / 2.2046)
	print "%.2f  will be  %.2f (approx) Kilograms." %(_Pounds, Kilogram)


# distance funtion
def    Feet_to_Kilometers(_Feet):
	Kilometer = (_Feet * 0.0003048)
	print "%.2f will be  %.2f (approx) Kilometers." %(_Feet, Kilometer)



#main func
def main():
	print 	"\n \nWelcome to the converter system."
	choice = get_int("\nChoose a conversion from below by typing its corresponding number: \n \t1. Celsius to Fahrenheit \n \t2. Pounds to Kilograms \n \t3. Feet to Kilometers. \n \tYour choice: ")

	if choice == 1:
		Celsius = get_int("Please Enter the temperature  to convert in Fahrenheit : ")
		Celsius_to_Fahrenheit(Celsius)
	elif choice == 2:
		Pounds  = get_int("Please Enter the weight in pounds to convert in Kilograms : ")
		Pounds_to_Kilograms(Pounds)
	elif choice == 3:
		Feet = get_int("Please Enter the length in feet to convert in Kilometers : ")
		Feet_to_Kilometers(Feet)
	else:
		print "Please try again!"

#Just trying try and catch becuase user can break the program easily!

try:	
	main()
except(TypeError,ValueError):
	print "Opps"