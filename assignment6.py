#########################################################################################################
#                                                                                                       #
#                          CS 87 A, Python Programming                                                  #
#                      This code is written by Rahisul Haque                                            #
#                           e-mail: rahisul@icloud.com                                                  #
#                                                                                                       #
#                                                                                                       #
#                                                                                                       #
#########################################################################################################



#get_int
#def get_int(msg):

	
	

# temperatue funtion
def    Celsius_to_Fahrenheit():

	Celsius = input("Please Enter the temperature  to convert in Fahrenheit : ")
	Fahrenheit = (Celsius * (9/5)) + 32
	print Celsius ," degree will be ", Fahrenheit, "degree Fahrenheit."



# weight function
def    Pounds_to_Kilograms():
	Pounds  = input("Please Enter the weight in pounds to convert in Kilograms : ")
	Kilogram = (Pounds / 2.2046)
	print Pounds," will be ", Kilogram, "Kilograms."


# distance funtion
def    Feet_to_Kilometers():
	Feet = input("Please Enter the length in feet to convert in Kilometers : ")
	Kilometer = (Feet * 0.0003048)
	print Feet, " will be  ", Kilometers, " Kilometers."









print 	"\n \nWelcome to the converter system."
choice = input("\nChoose a conversion from below by typing its corresponding number: \n \t1. Celsius to Fahrenheit \n \t2. Pounds to Kilograms \n \t3. Feet to Kilometers. \n \tYour choice: ")

if choice == 1:
	Celsius_to_Fahrenheit()
elif choice == 2:
	Pounds_to_Kilograms()
elif choice == 3:
	Feet_to_Kilometers()
else:
	print "Please put a valid input and try again!"
