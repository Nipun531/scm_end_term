 if turn % 2 == 0:
            print("\nYOU WILL PICK A NUMBER")
            sys_random = randint(1, 51)
            guess = int(input("Pick a number:  "))
            print(f"\nYour pick: {guess}")
            print(f"Opponent guess: {sys_random}")
            if sys_random == guess:
                user_hp-= 100
                print("\nFATALITY!!!\nYour opponent guessed right.\nYou were dealt with a 100 DAMAGE")
                print("\n\t---YOU LOST---")
                break
