# -*- encoding: utf-8 -*-
# adsimulator v1.1.1
# A realistic random generator of Active Directory domains
# Copyright © 2022, Nicolas Carolo.
# See /LICENSE for licensing information.

"""
INSERT MODULE DESCRIPTION HERE.

:Copyright: © 2022, Nicolas Carolo.
:License: BSD (see /LICENSE).
"""

__all__ = ()

import sys
import os
from os import path
from adsimulator.DBCreator import MainMenu
from adsimulator.utils.file import check_file_existence


def main():
    init_path = os.path.expanduser("~") + "/.adsimulator"
    if not path.exists(init_path):
        print("ERROR: Before executing adsimulator, run the installation script!")
        exit(1)
    if check_file_existence(init_path + "/adsimulator_sw.lock"):
        print("Before executing adsimulator, run:")
        print("\t$ pip install -r " + init_path + "/adsimulator/requirements.txt")
        print("\t$ cd " + init_path + "/adsimulator")
        print("\t$ python3 setup.py install")
        print("\t$ rm " + init_path + "/adsimulator_sw.lock")
        print("\t$ adsimulator")
        exit(0)
    try:
        MainMenu().cmdloop()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit()
