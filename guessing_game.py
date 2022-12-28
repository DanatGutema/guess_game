secret_word= "danat"
guess_word =""
guess_limit = 3
guess_count =0
no_chance_to_guess= False
while guess_word != secret_word and not(no_chance_to_guess):
    if guess_count < guess_limit:
        guess_word= input("enter your guess")
        guess_count += 1
    else:
        no_chance_to_guess = True
if no_chance_to_guess:
    print("YOU LOSE!")
else:
    print("YOU WIN!")                