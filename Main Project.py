def random_destination():
    import random
    destination_list = ['Chicago', 'Milwaukee', 'Detroit', 'Indianapolis']
    print(random.choice(destination_list))

def random_restaurant():
    import random
    restaurant_list = ['pizza', 'burgers', 'tacos', 'beer']
    print(random.choice(restaurant_list))

def random_transportation():
    import random
    transportation_list = ['car', 'plane', 'train', 'bus']
    print(random.choice(transportation_list))

def random_entertainment():
    import random
    entertainment_list = ['bar', 'movie', 'play', 'sports game']
    print(random.choice(entertainment_list))

print('Welcome to Day Trip Generator!')
usr_response = input('would you like to use our random trip generator? please answer yes or no. ')
if(usr_response == 'yes'):
    print('Great lets get started! ')
else:
    print('Come back when you are ready!')

customer_destination = random_destination
print('Your first selection is your destination')
random_destination








