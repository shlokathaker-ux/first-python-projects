import random  #importing database

number = random.randint(1,20)

x = int(input("Guess a number from 1 to 20:"))
    
while True:
    if x==number:
         print("BOOM! You guessed it right!🎉")
         break
    elif x>number:
         print("Your guess is too high.")
    else:
         print("Your guess is too low.")

    print("1. Try again")
    print("2. Ragequit")
    y = input("What would you like to do?:")
    if y=="1":
        x = int(input("Guess the number again:"))
    else:
        print(f"The number was {number}! LOL you suck!😆")
        break
