
import random 
import time
def russian_roulette():
   print("\n🔫 Welcome to Russian Roulette!\n")
    time.sleep(1)

    for round_num in range(1, 7):
        input(f"🔁 Round {round_num}: Press Enter to spin the cylinder & pull the trigger...")
        
    
        bullet_position = random.randint(0, 5)
        trigger_position = random.randint(0, 5)

        print("🔄 Spinning the cylinder...", end='', flush=True)
        time.sleep(1)
        print(" ✅")

        print("👉 Pulling the trigger...")
        time.sleep(1)

        if bullet_position == trigger_position:
            print("💥 BANG! You're dead!\n")
            return False
        else:
            print("😅 Click! You're safe.\n")
            time.sleep(1)
    
    print("🎉 Congratulations! You survived all 6 rounds!\n")
    return True

def play_game():
    print("🎮 Russian Roulette Game Started!")
    while True:
        survived = russian_roulette()
        again = input("🎲 Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("\n👋 Thanks for playing. Stay safe!")
            break

# Run the game
if __name__ == "__main__":
    play_game()

