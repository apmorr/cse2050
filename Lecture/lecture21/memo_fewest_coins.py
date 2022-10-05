def memo_fewest_coins(coin_value_list, amnt_in_cents, known_results):
    minCoins = amnt_in_cents
    
    # Base case 1: we can make this amount with a coin in the list

    # Base case 2: we have already solved this sub problem
    
    
    # Recursively call function on sub problems
        # Make a list of valid coins for this level
        # For each of those coins:
            # solve next sub problem
            # if a new minimum is found: update known results

    # return minimum coins for this sub problem
    
print(memo_fewest_coins([1,5,10,25],63, {}))
