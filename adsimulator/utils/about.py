from tabulate import tabulate
from adsimulator.utils.colors import O, W


SW_NAME = "adsimulator"
SW_VERSION = "1.1.1"
RELEASE_DATE = "2022-06-29"
DEVELOPER = "Nicolas Carolo"


def print_software_information():
    print()
    print(tabulate([[O + 'Software name:' + W, SW_NAME],
                    [O + 'Version:' + W, SW_VERSION],
                    [O + 'Release date:' + W, RELEASE_DATE],
                    [O + 'Developer:' + W, DEVELOPER]], tablefmt='grid'))
    print()