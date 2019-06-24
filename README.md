# Inland Revenue Department Number Validator

A validator python package for New Zealand tax numbers (IRD)

## Getting Started

These instructions will get you a copy of the project up and 
running on your local machine for development and testing purposes.

If you would like to create your own package follow the guide below:
* [Packaging project](https://packaging.python.org/tutorials/packaging-projects/)

## Installing

```
pip install git+https://github.com/danielcerezodev/NZ_IRD_Number_Validator.git
```

## Usage

```
from NZ_IRD_Number_Validator import is_valid

ird_number = "123-456-789"

is_ird_number_valid = is_valid(ird_number)

if is_ird_number_valid:
    print(ird_number + " is valid")
else:
    print(ird_number + " is not valid")
```

## How the validation is done

The following steps are performed:

* Check the valid range
    * If the IRD number is < 10-000-000 or > 150-000-000 then the number is invalid. This step ensures that the IRD number is in the already issued range, or is in the range expected to be issued in the next 10 years.
* Form the eight digit base number
    * Remove the trailing check digit.
    * If the resulting number is seven digits long, pad to eight digits by adding a leading zero.
* Calculate the check digit
    * To each of the base number’s eight digits a weight factor is assigned. From left to right these are: 3, 2, 7, 6, 5, 4, 3, 2.
    * Sum together the products of the weight factors and their associated digits.
    * Divide the sum by 11. If the remainder is 0 then the calculated check digit is 0.
    * If the remainder is not 0 then subtract the remainder from 11, giving the calculated check digit.
    * If the calculated check digit is in the range 0 to 9, go to step 5.
    * If the calculated check digit is 10, continue with step 4.
* Re-calculate the check digit
    * To each of the base number’s eight digits a secondary weight factor is assigned. From left to right these are: 7, 4, 3, 2, 5, 2, 7, 6.
    * Sum together the products of the weight factors and their associated digits.
    * Divide the sum by 11. If the remainder is 0 then the calculated check digit is 0.
    * If the remainder is not 0 then subtract the remainder from 11, giving the 00 calculated check digit.
    * If the calculated check digit is 10, the IRD number is invalid. 5. Compare the check digit :
    * Compare the calculated check digit to the last digit of the original IRD number.
    * If they match, the IRD number is valid.

## Built With

* [Python](https://www.python.org/) - Programming language
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE

## [Changelog](https://github.com/danielcerezodev/NZ_IRD_Number_Validator/blob/master/CHANGELOG.md)

## Authors

* **Daniel Cerezo**

## License

This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/danielcerezodev/NZ_IRD_Number_Validator/blob/master/LICENSE.md) file for details
