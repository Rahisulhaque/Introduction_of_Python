#########################################################################################################
#                                                                                                       #
#                          CS 87 A, Python Programming                                                  #
#                      This code is written by Rahisul Haque                                            #
#                           e-mail: rahisul@icloud.com                                                  #
#                                                                                                       #
#                                                                                                       #
#                                                                                                       #
#########################################################################################################

total = 0
max_ = 0
min_ = 0
usr_input = 0 
number_of_input = 0

while (usr_input != -1):
	usr_input = int(input("Please enter a grade:"))
	if (usr_input > 0):
		if usr_input >= max_ and usr_input >= min_ :
			
			max_ = usr_input
		elif usr_input < max_ and usr_input > min_:
			min_ = usr_input
		else :
			min_ = usr_input

		total += usr_input
		number_of_input += 1

	elif usr_input < 0 and usr_input != -1:
		print "Invalid entry!"
print "The Max is ", max_
print "and the Min is ", min_
print "The average is ", total/number_of_input