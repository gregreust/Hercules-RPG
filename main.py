hercules_attacks = {
    #attack name : power, how many attacks available 
    'sword':['power', 'how many']
    'shield':[]
    'kick':[]
    'defend':[]
}

hercules_health = 100

lion_attacks = {
    #attack name : power, how many attacks available 
    'sword':['power', 'how many']
    'shield':[]
    'kick':[]
    'defend':[]
}

lion_health = 15

hydra_attacks : {
    #attack name : power, how many attacks available 
    'sword':['power', 'how many']
    'shield':[]
    'kick':[]
    'defend':[]
}

hyrda_health = 30

cerberus_attacks = {
    #attack name : power, how many attacks available 
    'sword':['power', 'how many']
    'shield':[]
    'kick':[]
    'defend':[]
}

ceberus_health = 50

def intro():
    print('Greetings, Hercules! \n You have been tasked by the king to complete a quest.')
    user_says_yes = ''
    while user_says_yes != 'y'
        user_says_yes = input('Do you accept the king\'s quest? Enter y to continue')
        if user_says_yes == 'y':
            print('Let\'s begin!')
        else:
            print('Are you sure? Enter y to continue, or you may leave in dishonor')

def battle(enemy_name, enemy_attacks, enemy_health):
    print(f'You see the {enemy_name} approaching up ahead. Get ready to fight!')
    


def run_game():
    intro()