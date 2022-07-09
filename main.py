hercules_attacks = {
    #attack name : power, how many attacks available 
    'sword':[10,4];
    'shield bash':[6,6];
    'kick':[5,8];
    'defend':[0,20];
}

hercules_health = 100

lion_attacks = {
    #attack name : power, how many attacks available 
    'bite':[10,4]
    'claw':[5,8]
    'pounce':[8, 5]
    'defend':[0, 20]
}

lion_health = 15

hydra_attacks : {
    #attack name : power, how many attacks available 
    'sword':['power', 'how many']
    'shield':[]
    'kick':[]
    'defend':[]
}

hyrda_health = 20

cerberus_attacks = {
    #attack name : power, how many attacks available 
    'sword':['power', 'how many']
    'shield':[]
    'kick':[]
    'defend':[]
}

ceberus_health = 40

def intro():
    print('Greetings, Hercules! \n You have been tasked by the king to complete a quest.')
    user_says_yes = ''
    while user_says_yes != 'y'
        user_says_yes = input('Do you accept the king\'s quest? Enter y to continue')
        if user_says_yes == 'y':
            print('Let\'s begin!')
        else:
            print('Are you sure? Enter y to continue, or you may leave in dishonor')


def attack():
    user_attack = input('Which move will you choose? \n1. Sword Attack \n2. Sheild Bash \n3. Kick \n4.Defend Yourself')

def enemy_attack(enemy_attacks):
    chosen_move = 

def is_alive(health_int):
    if health_int <= 0:
        return False
    else:
        return True

def battle(enemy_name, enemy_attacks, enemy_health):
    print(f'You see the {enemy_name} approaching up ahead. Get ready to fight!')
    while hercules_health > 0 and enemy_health > 0:
        attack():
        enemy_attack(enemy_attacks):
    #loop until someone dies

def end_game():

    pass
    


def run_game():
    intro()