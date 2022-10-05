from typing import Counter


def rec_fewest_coins(coin_value_list, amt_in_cents):
    global counter
    counter += 1
    # assume we have pennies
    min_coins = amt_in_cents


    #Define the recursive base case: we need 1 coin
    if amt_in_cents in coin_value_list: return 1

    #Recursively search for a minimum number of coins
        # Build a list of valid coins
    
        # Iterate over each coin
            # Recursively call function on next smaller amount
            # Update our minimum if we have done better
    for coin in coin_value_list:
        if coin <= amt_in_cents:
            temp_min = rec_fewest_coins(coin_value_list, amt_in_cents - coin) + 1
            if temp_min < min_coins:
                min_coins = temp_min

    return min_coins

   

    # Return min_coins


################################### Quiz ###################################
# Will this give the correct answer (fewest coins) for any amount and      #
# any list of coins?                                                       #
#    1) yes                                                                #
#    2) no                                                                 #
############################################################################
    
    
if __name__ == '__main__':
    counter = 0
    print(rec_fewest_coins([1,21,25], 63))
    print(f"recursive calls: {counter}")
    
    print(rec_fewest_coins([1,5,21,25], 63))
    print(f"recursive calls: {counter}")