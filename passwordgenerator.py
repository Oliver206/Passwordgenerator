import random

password_length = int(
    input("How many characters do you want in your password? : "))
password = list()

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercaseletters = [i.upper() for i in letters]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "?", "%", "&"]


def generatePassword():
    while len(password) < password_length:
        randomnum = random.randint(1, 4)
        pickedListDict = {1: letters, 2: uppercaseletters,
                          3: numbers, 4: symbols}
        randompickList = pickedListDict[randomnum]
        # print(randompickList)
        randomnumForList = random.randint(0, (len(randompickList) - 1))
        print(randomnumForList)
        password.append(randompickList[randomnumForList])


# print(__name__)
if __name__ == "__main__":
    generatePassword()
    print("Your password is:", "".join(password))

