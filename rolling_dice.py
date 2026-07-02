import random
import time

dice_faces = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

print(" 🎲Welcome to the rolling dice simulator!🎲")

while True:
    input("Press enter to roll the dice")

    print("Rolling ...", end="")
    for _ in range(3):
        face = random.choice(dice_faces)
        print(face, end="", flush=True)
        time.sleep(0.5)

    roll = random.randint(1,6)
    print(f"You rolled a {dice_faces[roll-1]}, {roll}!")
    
    choice = input("Do you want to roll again? (yes/no):").lower()
    if choice=="yes":
        continue
    else:
        print(" OkAy tHaNkYoU bYe!")
        break


