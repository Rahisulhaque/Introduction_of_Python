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
	except NameError:
		print " ****   Please enter a valid input and try again!  ****"
