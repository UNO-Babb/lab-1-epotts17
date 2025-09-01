#MadLib.py
#Name: Ellery Potts
#Date: August 27, 2025
#Assignment: Lab 1 - MadLib

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a noun: ")
adjective1 = input("Enter an adjective: ")
noun2 = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
adverb1 = input("Enter an adverb: ")
verb1 = input("Enter a verb: ")
noun3 = input("Enter a noun: ")
  #Print the story with the user supplied words.
print("Once upon a time there was a " + adjective1 + " " + noun1 + ".")
print("This " + noun1 + " lived in a " + noun2 +".")
print("One day " + noun1 + " was feeling paricularly " + adjective2 + " and decided to " + adverb1 + " " + verb1 + " to the " + noun3 + ".")



#Call the main function if this is the file being run.
if __name__ == '__main__': 
    main()
