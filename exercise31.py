word_to_guess = "EVAPORATE"

already_guessed = list()

word_list = ["_" for i in word_to_guess]


# ask for a letter
# consider already guessed words
# end game when all letters are guesses correctly


str1 = ""
print(str1)

print("Welcome to Hangman!")

while True:
    user_inp = input("Guess your letter: ").upper()
    if user_inp in word_to_guess and user_inp not in already_guessed:
        # multiple indexes?
        list_ind = [i for i, n in enumerate(word_to_guess) if n == user_inp]
        if len(list_ind) < 2:
            word_list[word_to_guess.index(user_inp)] = user_inp
        else:
            for x in list_ind:
                word_list[x] = user_inp
            # works for more than 2 indexes

        str1 = " ".join(word_list)

        already_guessed.append(user_inp)

        print(str1)

    elif user_inp in already_guessed:
        print("You already had that one.")
        continue
    else:
        already_guessed.append(user_inp)
        print("Wrong, adding to already guessed.")

    if list(word_to_guess) == word_list:
        print("All guessed correctly. Game finished!")
        quit()