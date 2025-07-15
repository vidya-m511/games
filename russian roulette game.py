
import random 
import time
def russian_roulette():
    print("welcome to russian roulette\n")
    chambers = [False]*6
    bullet_position = random.randint(0,5)
    chambers[bullet_position]= True

    print("spinning the cylinder...")
    time.sleep(1)
    print("Done.\n")

    for round_num in range(1,7):
      input(f"round{round_num}: press enter to pull the trigger...")
      print("click!")
      time.sleep(1)
      if chambers[round_num-1]:
         print("BANG! you are dead!")
         break
      else:
         print("you are safe.\n")
    else:
       print("you survived all 6 rounds!")
          
