def naive_recr(amt, coins):
    n_opt = 0

    for coin in coins:
        if coin == amt: return 1 # if the value of the coin is equal to the amount, it is the best possible coin
        elif coin < amt:
            n = naive_recr(amt-coin, coins) + 1 # else if the coin is less than the amount, subtract the value of the coin from amount and run function again. +1 is to indicate the coin that was used

            if n < n_opt: # if the amount of coins needed is less than the minimum from other paths, update it
                n_opt = n
        
    return n_opt # returns optimal solution



def fewest_coins():
    pass

    

if __name__ == "__main__":
    coins = [1, 2, 3]
    assert not naive_recr(110, coins) == 2
    assert naive_recr(2, coins) == 1


