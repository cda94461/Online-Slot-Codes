import random

# Define slot machine symbols and their payout multipliers
symbols = {
    '🍒': 2,  # 2x payout
    '🍋': 3,  # 3x payout
    '🍊': 5,  # 5x payout
    '🍉': 10, # 10x payout
    '🍇': 20  # 20x payout
}

# Player's initial balance
balance = 100  

def spin():
    """Generate a random spin result with 3 symbols"""
    return [random.choice(list(symbols.keys())) for _ in range(3)]

def main():
    global balance  
    print("🎰 Welcome to the Online Slot Machine! 🎰")
    
    while balance > 0:
        print(f"\n💰 Your balance: ${balance}")
        bet = int(input("Enter your bet amount (or 0 to quit): "))
        
        if bet == 0:
            print("Thanks for playing! 🎉")
            break
        elif bet > balance:
            print("❌ You don't have enough balance!")
            continue

        # Perform the spin
        balance -= bet
        result = spin()
        print(f"\n🎰 {result[0]} | {result[1]} | {result[2]} 🎰")

        # Check for a win
        if result[0] == result[1] == result[2]:  
            win_amount = bet * symbols[result[0]]
            balance += win_amount
            print(f"🎉 Jackpot! You win ${win_amount} 🎉")
        else:
            print("❌ No win! Try again!")

    print("\nGame over! You ran out of money! 💸")

if __name__ == "__main__":
    main()
