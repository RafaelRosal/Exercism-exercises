
# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40


# Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    x = EXPECTED_BAKE_TIME - elapsed_bake_time
    if x < 0:
        print("Ih, queimou!")
    return x


# Define the 'preparation_time_in_minutes()' function below.
# You might also consider using 'PREPARATION_TIME' here, if you have it defined.
def preparation_time_in_minutes(number_of_layers):
    """Calculate the time (in minutes) for the amount of layers expecified
    
    :param number_of_layers: int - the number of layers the lasagna will have
    :return: int - the time (in minutes) - consider each layer need 2 min to bake
    """
    return number_of_layers * 2


# Define the 'elapsed_time_in_minutes()' function below.
# Remember to add a docstring (you can copy and then alter the one from bake_time_remaining).
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed bake time (in minutes)

    :param number_of_layers: int - .
    :param elapsed_bake_time: int - .
    :return: int - time elapsed (in minutes).
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time


print(bake_time_remaining(50))
print(preparation_time_in_minutes(2))
print(elapsed_time_in_minutes(2, 40))
