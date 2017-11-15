# Written by Rahisul Haque


i = 0
total = 0
counter = 0
myList = []

#myList = [-1,-2,-3,0,2,2,2,2,2,2,2,2]   #test case


while i < len(myList) :
    if myList[i] > 0:
        counter += 1
        total += myList[i]
    i += 1

print "There is ", counter, "numbers."
print "The average is ", total/counter
