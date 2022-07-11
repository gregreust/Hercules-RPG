from random import choice

hercules_attacks = {
    #attack name : power, how many attacks available 
    'sword':[10,5],
    'shield bash':[6,6],
    'kick':[5,8],
    'defend':[0,30],
}

hercules_health = 100

lion_attacks = {
    #attack name : power, how many attacks available 
    'bite':[10,4],
    'claw':[5,8],
    'pounce':[8,5],
}

lion_health = 15

hydra_attacks = {
    #attack name : power, how many attacks available 
    'triple header':[10,4],
    'scream':[8,4],
    'bite':[6,10],
}

hyrda_health = 30

cerberus_attacks = {
    #attack name : power, how many attacks available 
    'triple header':[20,3],
    'pounce':[10,3],
    'scratch':[5,10],
}

cerberus_health = 40

empty_dict = {
    '':[]
}

def intro():
    print('Greetings, Hercules! \n You have been tasked by the king to complete a quest.')
    user_says_yes = ''
    while user_says_yes != 'y':
        user_says_yes = input('Do you accept the king\'s quest? Enter y to continue:')
        if user_says_yes == 'y':
            print('Let the quest begin!')
        else:
            print('Are you sure? Enter y to continue, or you may leave in dishonor')


def attack(enemy_name, enemy_health):
    user_attack = input('Which move will you choose? \n1 for Sword Attack \n2 for Shield Bash \n3 for Kick \n4 for Defend Yourself')
    if user_attack == 1:
        enemy_health -= hercules_attacks['sword'][0]  #enemy health decreases
        hercules_attacks['sword'][1] -= 1     #player has one less attack to use  
        print(f'You used sword attack. The {enemy_name} has {enemy_health} health points left.')
        print(f'You have {hercules_attacks['sword'][1]} sword attacks remaining')
        return False
    elif user_attack == 2:
        enemy_health -= hercules_attacks['shield bash'][0]  #enemy health decreases
        hercules_attacks['shield bash'][1] -= 1     #player has one less attack to use  
        print(f'You used shield bash. The {enemy_name} has {enemy_health} health points left.')
        print(f'You have {hercules_attacks['shield bash'][1]} shield bashes remaining')
        return False
    elif user_attack == 3:
        enemy_health -= hercules_attacks['kick'][0]  #enemy health decreases
        hercules_attacks['kick'][1] -= 1     #player has one less attack to use  
        print(f'You used kick. The {enemy_name} has {enemy_health} health points left.')
        print(f'You have {hercules_attacks['kick'][1]} kicks remaining')
        return False
    elif user_attack == 4:
        hercules_attacks['defend'][1] -= 1     #player has one less attack to use  
        print(f'You defended yourself.')
        print(f'You have {hercules_attacks['defend'][1]} defends remaining')    
        return True
    else:
        print('Error. Please enter 1, 2, 3, or 4')
        return False

        


def enemy_attack(enemy_name, enemy_attacks, did_player_defend):
    chosen_move = choice(enemy_attacks)
    enemy_attacks.chosen_move[1] -= 1 #enemy has one less attack to use
    if did_player_defend == True:
        print(f'The {enemy_name} used {chosen_move}, but you defended yourself from the attack. \nThe {enemy_name} has {enemy_attacks.chosen_move[1]} {chosen_move} remaining.')
    else:
        hercules_health -= enemy_attacks[chosen_move][0] #player loses health
        print(f'The {enemy_name} used {chosen_move}. You now have {hercules_health} health points.')



def is_able_to_attack(attack_index):
    if attack_index[1] <= 0:
        return False
    else:
        return True

def is_alive(health_int):
    if health_int <= 0:
        return False
    else:
        return True

def battle(enemy_name, enemy_attacks, enemy_health):
    print(f'You see the {enemy_name} approaching up ahead. Get ready to fight!')
    while hercules_health > 0 and enemy_health > 0:
        did_player_defend = attack(enemy_name, enemy_health)
        if is_alive(enemy_health) == False:
            print(f'You successfully defeated the {enemy_name}!')
            break
        enemy_attack(enemy_name, enemy_attacks, did_player_defend)
        if is_alive(hercules_health) == False:
            print(f'You were slain by the {enemy_name}. Better luck next time :(')
            break
    #loop until someone dies
   

def end_game():
    if is_alive(hercules_health) == True:
        print('Congratulations, Hercules! You have completed your quest. King Eurystheus has a handsome reward for you.')
    pass
    


def run_game():
    intro()
    battle('Nemean Lion', lion_attacks, lion_health)
    battle('Lernaean Hydra', hydra_attacks, hyrda_health)
    battle('Cerberus', cerberus_attacks, cerberus_health)
    end_game()

run_game()