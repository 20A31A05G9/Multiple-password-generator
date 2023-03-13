# importing the random module 
import random
# implementing a generatePassword() function that will generate a password on length (n) and return it.

def generatePassword(n):
    # defining the list of choices of characters.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

    chosenLetter = random.sample(characters, n)
    
    # The random.sample() method returns a list, so we need to convert it into a string before returning it.
    
    # finally converting the list into a string to get a password as a string datatype
    password = "".join(chosenLetter)

    return password
if __name__ == "__main__":
    while True:
        usersChoice = input("Please enter 'yes' if you want to generate a password else type 'no' to exit: ")
        if usersChoice == 'no':
            break
        else:
            n = int(input("Enter the length of the password: "))
            password = generatePassword(n)
            print("A randomly selected password is:", password)