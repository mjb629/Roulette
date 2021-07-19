import random

def always_red(bankroll):  
    bankroll = 100
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += 1
        else:
            bankroll -= 1
        bankroll_history.append(bankroll)
    return bankroll_history
