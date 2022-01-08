import random
from adsimulator.utils.time import generate_timestamp
from adsimulator.utils.boolean import generate_boolean_value


def get_user_timestamp(current_time, enabled):
    if enabled == True:
        return generate_timestamp(current_time)
    else:
        return -1


def generate_sid_history(p_true, p_false):
    if generate_boolean_value(p_true, p_false):
        return "S-1-5-21-883822822-279636685-4182209497-" +  str(random.randint(1100, 2000))
    else:
        return ""