#this is wrong as FUCK

"""def is_prime(test_num):
	if test_num > 1:
		for i in range (2, test_num):
			if(test_num% i) == 0:
				return False
			else:
				return True
	else:
		return True

userInput = int(input("Gimme a number, I will tell if it is prime or not?"))
if (is_prime(userInput)) == True:
	print "Thats prime!"
else:
	print "Nope, not a prime!"
"""



#correct solu here:

def is_prime(x):
    isPrime = False
    if (x < 2):
       isPrime = False
    elif (x == 2):
        isPrime = True
    else:
        for n in range(2,x):
            if ( x % n) == 0:
                isPrime = False
                break
            else:
                isPrime = True
    return isPrime



    