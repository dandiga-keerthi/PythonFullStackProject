import random

def random_event_choice(options):
    return random.choice(options)

def validate_positive(value):
    return max(0, value)
