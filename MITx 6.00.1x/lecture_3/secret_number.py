answer = ""
high = 100
low = 0
guess = 50

print("Please think of a number between 0 and 100!")
while answer != "c":
    print("Is your secret number " + str(guess) + "?")
    answer = raw_input("Enter 'h' to indicate guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == 'h':
        high = guess
        guess = (high + low) / 2
    elif answer == 'l':
        low = guess
        guess = (high + low) / 2
    elif answer == 'c':
        continue
    else:
        print("Sorry, I did not understand your input.")

print("Game over. Your secret number was: " + str(guess))  

