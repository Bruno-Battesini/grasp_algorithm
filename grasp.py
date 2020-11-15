import random


def random_generator(seed, lower_bound, higher_bound):
    random.seed(seed)
    return random.randint(lower_bound, higher_bound)


def grasp(alpha, iterations):
    for n in range(iterations):
        pass
