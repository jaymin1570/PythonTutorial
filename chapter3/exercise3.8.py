# modify number guessing game

import random
winning_number = random.randint(1,100)
guess = 1
num =input("enter a number between 1 and 100 :")
num = int(num)
game_over = False

while not game_over:
    if num == winning_number:
        print(f"you win, you guessed this number in {guess} times")
        game_over = True
    else:
        if num < winning_number:
             print(" Too Low ")
             guess += 1
             num = int(input("guess again : "))
        else:
            print("Too high ")
            guess += 1
            num = int(input("guess agian : "))

