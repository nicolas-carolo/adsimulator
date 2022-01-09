# -*- encoding: utf-8 -*-
# adsimulator v1.0.0
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
from adsimulator.DBCreator import MainMenu



def main():
    try:
        MainMenu().cmdloop()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit()
