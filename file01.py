def     main():
    myFile = open("Philosopers.txt", 'r')
    myNewFile = open("PhilosophersCopy.txt", 'w')
    myNewFile.write(myFile.read())
    myNewFile.close()
    myFile.close()

main()

