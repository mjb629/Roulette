def martingale(bankroll):
    bet = .01
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            bet = .01
        else:
            bankroll -= bet
            bet *=2
        bankroll_history.append(bankroll)
    return bankroll_history
    
martingale(bankroll=100)
