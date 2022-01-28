import random
from unittest import result

destinations = ['Chicago', 'Milwaukee', 'Detroit', 'Indianapolis']

def random_destination(destination_list):
    result = random.choice(destination_list)
    return result

final_destination = random_destination(destinations)
print(final_destination)

user_satisfied = False

while user_satisfied == False:
    user_input = input('Are you happy with your destination? Please answer yes or no. ')
    if user_input == 'no':
        final_destination = random_destination(destinations)
        print(final_destination)
    elif user_input =='yes':
        user_satisfied == True
        break

restaurants = ['pizza', 'burgers', 'tacos', 'beer']

def random_restaurant(restaurant_list):
    result = random.choice(restaurant_list)
    return result

final_restaurant = random_restaurant(restaurants)
print(final_restaurant)

user_satisfied = False

while user_satisfied == False:
    user_input = input('Are you happy with your restaurant? Please answer yes or no. ')
    if user_input == 'no':
        final_restaurant = random_restaurant(restaurants)
        print(final_restaurant)
    elif user_input == 'yes':
        user_satisfied == True
        break

transportation = ['car', 'plane', 'train', 'bus']

def random_transportation(transportation):
    result = random.choice(transportation)
    return result

final_trans = random_transportation(transportation)
print(final_trans)

user_satisfied = False

while user_satisfied == False:
    user_input = input('Are you happy with your mode of transportation? Please answer yes or no.')
    if user_input == 'no':
        final_trans = random_transportation(transportation)
        print(final_trans)
    elif user_input == 'yes':
        user_satisfied == True
        break

entertainment = ['bar', 'movie', 'play', 'sports game']

def random_entertainment(entertainment):
    result = random.choice(entertainment)
    return result

final_entertainment = random_entertainment(entertainment)
print(final_entertainment)

user_satisfied = False

while user_satisfied == False:
    user_input = input('Are you happy with your form of entertainment? Please answer yes or no.')
    if user_input == 'no':
        final_entertainment = random_entertainment(entertainment)
        print(final_entertainment)
    elif user_input == 'yes':
        user_satisfied == True
        break


print("Congratulations you're goingto: ")
print(final_destination)

print("You're eating:")
print(final_restaurant)

print("your mode of transportation is: ")
print(final_trans)

print("your entertainment event is: ")
print(final_entertainment)



