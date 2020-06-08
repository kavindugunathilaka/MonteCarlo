import numpy as np 
import random 

def turn_and_random(turns):
    return (random.random(), turns+1)

def duel(probability_arr):
    turns = 0
    survivor = None
    players_ref = {'A': 0, 'B': 1, 'C': 2}
    players = [ x for x in players_ref.keys() ]
  
    while len(players) > 1:
        for player in players:
            randValue, turns = turn_and_random(turns)
            opponent_player = players[:]
            opponent_player.remove(player)
            
            
            if randValue <= probability_arr[players_ref[player]]:
                players.remove(opponent_player[0])
                
        
        if len(players) == 1:
            survivor = players_ref[player[0]]
            break
        
    return (survivor, turns)


if __name__ == "__main__":
    
    num_of_simulations = 1000
    probability_arr = np.array([ 5/6, 4/6, 2/6 ])
    survivor_record = np.zeros(3)
    num_of_turns = 0

    print("Number of Simulations : {0}".format(num_of_simulations))

    for simulation in range(num_of_simulations):
        survivor, turns = duel(probability_arr)
        survivor_record[survivor] += 1
        num_of_turns += turns
    print(survivor_record)
    win_probability = np.divide(survivor_record, num_of_simulations)
    print("Winning probab  \n\t A : {0}\n\t B : {1}\n\t C : {2}".format(win_probability[0], win_probability[1], win_probability[2]))
    average_turns = (num_of_turns / num_of_simulations)

    print("Avg of Turns  : {0}".format(average_turns))