import re


# This method will take the passed IRD string
# remove all non-numeric characters and add a
# preceding 0 if the number has 8 characters
def clean_ird(ird):
    # Use regex to remove all non-numeric characters
    clean_ird_number = re.sub('[^0-9]', '', ird)

    # add preceding 0 if IRD has 8 digits
    if len(clean_ird_number) < 9:
        clean_ird_number = "0" + clean_ird_number

    # Returns the "clean" IRD number
    return str(clean_ird_number)


# This method will calculate the check digit (trailing digit of the IRD number)
# It will multiply each digit of the IRD number to the corresponding
# weight factor, then sums them up and gets the remainder when divided by 11.
# The remainder is then compared to the check digit.
def get_remainder(ird, weight_factor):
    # For checking the IRD we will need
    primary_weights = [3, 2, 7, 6, 5, 4, 3, 2]
    secondary_weights = [7, 4, 3, 2, 5, 2, 7, 6]

    # Choose weights depending on the weight factor
    if weight_factor == 1:
        weights = primary_weights
    else:
        weights = secondary_weights

    # Convert the IRD number into a list of integers
    ird_list = list(map(int, ird[:-1]))

    print(ird_list)
    print(weights)

    # Multiply each weight factor to their corresponding IRD digit
    result = map(lambda x, y: x * y, ird_list, weights)

    # Sum the result and divide it by 11 to get the remainder
    remainder = sum(result) % 11

    return int(remainder)


# This method will take the passed IRD number
# and use the official validation process to
# determine whether the IRD is valid or invalid
def is_valid(ird):
    # For "safety" reasons use the clean method to make sure
    # the IRD number only contains numerical characters before
    # validating
    ird = clean_ird(ird)

    # Check that the ird is the correct length
    # and if it is in range
    if len(ird[:-1]) == 8 and 10000000 <= int(ird) <= 150000000:
        check_digit = int(ird[8])
        remainder = get_remainder(ird, 1)

        # If remainder is 0 and the check digit (last digit of the IRD number) is 0
        # then IRD number is valid
        if remainder == 0 and check_digit == remainder:
            return True
        # If remainder is != 0, subtract it from 11
        else:
            remainder = 11 - remainder
        # If 11 - remainder = check digit, then IRD number is valid
        if 0 <= remainder <= 9 and remainder == check_digit:
            return True

        # if result is 10, recalculate weights using the secondary weight factor
        elif remainder == 10:
            # calc for each digit using the secondary weight factor
            remainder = get_remainder(ird, 2)
            # if remainder is 0 and check digit (last digit of the IRD number) is 0
            # then IRD number is valid
            if remainder == 0 and check_digit == 0:
                return True
            # if remainder is != 0, subtract it from 11
            else:
                remainder = 11 - int(remainder)
                if remainder == check_digit:
                    return True
    return False
