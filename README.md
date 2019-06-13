# NZ IRD NUMBER VALIDATOR PYTHON PACKAGE

A validator python package for New Zealand tax numbers (IRD)

## Getting Started

These instructions will get you a copy of the project up and 
running on your local machine for development and testing purposes.

if you would like to create your own package follow the guide below:
* [Packaging project](https://packaging.python.org/tutorials/packaging-projects/)

### Installing

```
pip install git+https://github.com/danielcerezodev/NZ_IRD_Number_Validator.git
```

### Usage

```
import NZ_IRD_Number_Validator as ird_validator

ird_number = "123-456-789"

is_ird_number_valid = ird_validator.check_ird(ird_number)

if is_ird_number_valid:
    print(ird_number + "is valid")
else:
    print(ird_number + "is not valid")
```

## Built With

* [Python](https://www.python.org/) - Programming language
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE

## Author

* **Daniel Cerezo Rodriguez**

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details