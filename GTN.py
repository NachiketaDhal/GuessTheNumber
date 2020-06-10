secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Enter your guess between 0 to 9 : "))
    guess_count += 1
    if guess == secret_number:
        print("Congratulations, You won!")
        break
else:
    print('''Hey, You lost! 
Try Again ... ''')
