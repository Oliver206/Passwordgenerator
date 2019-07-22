import random

randomnum = str(random.randint(1000, 9999))
print(randomnum)
randomnumList = [int(i) for i in randomnum]
print(randomnumList)
cows = 0
bulls = 0
counter = 0

while cows < 4:
    print(randomnumList[counter])
    print(counter)
    guessed_num = int(input("Give me a number: "))
    if randomnumList[counter] == guessed_num:
        cows += 1
        counter +=1
        print("Right!", cows, "cows", "+", bulls, "bulls")
    else:
        bulls +=1
        print("Right!", cows, "cows", "+", bulls, "bulls")
    if cows == 4:
        print("Finish")