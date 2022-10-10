# Algorithm 1: Recursively figuring out all the perfect couples
import random

num_people = int(input('How many people will be getting matched? '))
while round(num_people) != num_people or num_people % 2 != 0 or num_people == 0:
    num_people = int(input('Please enter an even nonzero integer. ')) # TODO: MAKE INPUT RAISE CUSTOM ERROR IF NON INTEGER IS INPUTTED

player_ids = [str(i+1) for i in range(num_people)]
random.shuffle(player_ids)

matches = dict()
def match_maker(player_ids):
    for player in player_ids:
        matches[player] == player_ids[1]
        player_ids.pop()
        player_ids.pop()