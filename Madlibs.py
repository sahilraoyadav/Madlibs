"""
Name: Sahil Yadav
Date: October 11 2018
Assignment: Assignment 2 Madlibs
Description: Asks user to provide several words and phrases to fill in a MadLibs story.
             The result will be written to an output file.
"""
import os.path
#function to replace the fillable contents in the file
def replace(readingfile):
    replace_contents = ''
    i = 0
    #loop to find the words and replaces them with a new word
    while i < len(readingfile):
        if readingfile[i] == "<":
            new_word = ''
            i += 1
            while readingfile[i] != '>':
                new_word += readingfile[i]
                i += 1
            new_word = input('Please enter a/an ' + new_word + ': ')
            replace_contents += new_word
        else:
            replace_contents += readingfile[i]
        i += 1
    return replace_contents
#main funtion 
def main():
    #prints out descritpion of what the program will do for the user
    print("""Welcome to the game of MadLibs.\n
I will ask you to provide several words and phrases to fill in a MadLibs story.
The result will be written to an output file.\n""")
    #checks to see if the filename is valid or invalid. If invalid then ask the user again for a input.
    while True:     
        inputfile = input("Please enter a filename: ")
        if os.path.isfile(inputfile) == False:
            print("File " + inputfile + " does not exist. Try again.")
        else:
            #opens the inputfile to be read
            infile = open(inputfile, 'r')
            #reads the file
            readingfile = infile.read()
            #asks for the output file
            outputfile = input("Please enter a output file name: ")
            #opens and writes to the output file
            outfile = open(outputfile, "w")
            #replaces the replacable contents in the file
            replace_contents = replace(readingfile)
            #writes the changes to the output file
            outfile.write(replace_contents)
            break
    print("\n" + "Your Madlib story has been created." + "\n")
    #asks the user if they want to see their story
    if input("Would you like to see the resulting story? (y or n)?\n") != 'y':
        print("Your output will be saved " + outputfile + ".txt \n" )
    else:
        print("\n", replace_contents, "\n")
    #closes the inputfile and outputfile
    infile.close()
    outfile.close
main()
#checks to see if the user wants to run it again.
while True:
    if input("Do you want to play again (y or n)?\n") != 'y':
        break
    else:
        #starts the program back up again if the user presses y
        print("-"*80)
        print("\n NEW GAME \n")
        main()

