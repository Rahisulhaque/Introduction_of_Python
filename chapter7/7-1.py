#basic file creation





def main():
    outfile = open("ToDoList.txt", 'w')

    outfile.write('1. Enjoy life! \n')
    outfile.write('2. Code. \n')
    outfile.write('3. Repeat... \n')

    outfile.close()

main()