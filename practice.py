restaurant_list = ['pizza', 'burgers', 'tacos', 'beer']

def random_restaurant(restaurant_list):
    result = random.choice(restaurant_list)
    return result

def random_transportation():
    import random
    transportation_list = ['car', 'plane', 'train', 'bus']
    print(random.choice(transportation_list))

def random_entertainment():
    import random
    entertainment_list = ['bar', 'movie', 'play', 'sports game']
    print(random.choice(entertainment_list))