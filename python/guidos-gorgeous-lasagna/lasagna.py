"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""
# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
EXPECTED_BAKE_TIME = 40

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_bake_time


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here

def preparation_time_in_minutes(num_layers):
    PREPARATION_TIME = num_layers * 2
    """ Calculate the preparation time for each layer
    :param num_layers (int): number of layers of lasagna

    Returns:
        PREPARATION_TIME (int): Number of minutes it takes to prepare lasagna
    """

    return PREPARATION_TIME
    

# TODO: define the 'elapsed_time_in_minutes()' function

# Returns the elapsed time in minutes between preparation and baking time.
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the time already spent 
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    
    elapsed_cooking_time = preparation_time_in_minutes(number_of_layers)+ elapsed_bake_time
    return  elapsed_cooking_time
    