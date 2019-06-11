# NZ IRD NUMBER VALIDATOR PYTHON PACKAGE

A validator python package for New Zealand tax numbers (IRD)

## Getting Started

These instructions will get you a copy of the project up and 
running on your local machine for development and testing purposes.

if you would like to create your own package follow the following guide:
* [Packaging project](https://packaging.python.org/tutorials/packaging-projects/)

### Installing

```
pip install git+https://github.com/novahealth/nz_ird_validator.git
```

### Usage

```
import nz_ird_validator

is_ird_valid = nz_ird_validator.is_valid("123-456-789")

if is_ird_valid:
    print("IRD IS VALID")
else:
    print("IRD IS NOT VALID")
```

## Built With

* [Python](https://www.python.org/) - Programming language
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE

## Author

* **Daniel Cerezo Rodriguez**

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details