import random
from unittest import result

destinations = ['Chicago', 'Milwaukee', 'Detroit', 'Indianapolis']

def random_list(list_type):
    result = random.choice(list_type)
    return result

final_destination = random_list(destinations)
print(final_destination)

user_satisfied = False

while user_satisfied == False:
    user_input = input('Are you happy with your result? Please answer yes or no. ')
    if user_input == 'no':
        final_destination = random_list(destinations)
        print(final_destination)
    elif user_input =='yes':
        user_satisfied == True
        break

restaurants = ['pizza', 'beet', 'tacos', 'burgers']

final_resaurant = random_list(restaurants)
print(final_resaurant)