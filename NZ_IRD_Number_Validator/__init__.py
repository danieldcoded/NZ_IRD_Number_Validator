import re


# This method will take the passed IRD
# and remove all non-numeric characters
def clean_ird(ird):

    # Uses regex to remove all non-numeric characters
    clean_ird_number = re.sub('[^0-9]', '', ird)

    # Returns the "clean" version of the IRD
    return clean_ird_number


def __check_digit(ird, weight_factor):

    # For checking the IRD we will need
    PRIMARY_WEIGHTS = [3, 2, 7, 6, 5, 4, 3, 2]
    SECONDARY_WEIGHTS = [7, 4, 3, 2, 5, 2, 7, 6]


# This method will take the passed IRD
# and use the official validation process
# to determine whether the IRD is valid or invalid
def check_ird(ird):

    # Initialise the boolean variable that stores
    # whether the IRD tax number is valid or invalid
    is_ird_valid = False

    # For "safety" reasons use the clean method to make sure the IRD number
    # only contains numerical characters before validating
    ird_to_validate = clean_ird(ird)

    return is_ird_valid
