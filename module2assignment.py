#########################################################################################################
#                                                                                                       #
#                          CS 87 A, Python Programming                                                  #
#                      This code is written by Rahisul Haque                                            #
#                           e-mail: rahisul@icloud.com                                                  #
#                                                                                                       #
#                                                                                                       #
#                                                                                                       #
#########################################################################################################


second_year_tution = 0
third_year_tution = 0 
fourth_year_tution = 0



starting_tution = input ("Please, Enter your starting tution: ")

total_tution = starting_tution

annual_increase = input ("Please, Enter your annual increase of the tution in the fraction format: ")

second_year_tution = starting_tution + starting_tution * annual_increase
total_tution += second_year_tution

third_year_tution = second_year_tution + second_year_tution * annual_increase
total_tution += third_year_tution

fourth_year_tution = third_year_tution + third_year_tution * annual_increase
total_tution += fourth_year_tution

print "With 5% increase, your second year tution will be: ", format(second_year_tution, '.2f')
print "With 5% increase, your third year tution will be: " , format(third_year_tution, '.2f')
print "With 5% increase, your fourth year tution will be: ", format(fourth_year_tution, '.2f')
print "Your total tution for 4 years will be: " ,format(total_tution, '.2f')