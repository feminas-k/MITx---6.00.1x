print "Please think of a number between 0 and 100!"
low = 0
high = 100
ans = 50
guess = False

while guess == False:
        print "Is your secret number "+ str(ans)+"?"
        user_ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

        while (user_ans != 'h' and user_ans != 'l' and user_ans != 'c'):
                print "Sorry, I did not understand your input."
                print "Is your secret number "+ str(ans)+"?"
                user_ans = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

        if user_ans == 'h':
                high = ans
                ans = (low+high)/2
        elif user_ans == 'l':
                low = ans
                ans = (low+high)/2
        else:
                guess = True
print "Game over. Your secret number was: " + str(ans)

