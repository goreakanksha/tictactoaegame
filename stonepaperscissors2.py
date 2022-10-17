import random
import sys

stone = '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
'''

paper = '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
'''

scissors = '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''



l = [stone,paper,scissors]



while True:
    user = int(input("Press 0 for stone, 1 for Paper and 2 for Scissors.. Press -1 to exit"))

    if user < 0 or user >2:
        print("Invalid Input")
        sys.exit()
        
    computer = random.randint(0,2)
    print("User Input")
    print(l[user])
    print("Computer Input")
    print(l[computer])

    if user == computer:
        print("Both select same choice....Match Draw")
    elif user == 0 and computer ==2:
        print("Hey, You won")
    elif user == 0 and computer ==1:
        print("You Lose")
    elif user == 1 and computer ==0:
        print("Hey, You won")
    elif user == 1 and computer ==2:
        print("You Lose")
    elif user == 2 and computer ==0:
        print("You Lose")
    elif user ==2 and computer == 1:
        print("Hey, You won")
    elif user == -1:
        break
