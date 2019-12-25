winning_number = 20
guess_number = int(input("guess anumber between 1 to 100="))

if winning_number == guess_number:
    print("YOU WIN !!!!")
else:
    if guess_number > winning_number:
        print("too high")
    else:
        print("too low")
