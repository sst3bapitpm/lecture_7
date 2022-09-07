#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:ABSTRACT:
This script ...

:REQUIRES:

:TODO:

:AUTHOR: Pedro Machado
:ORGANIZATION: Nottingham Trent University
:CONTACT: pedro.machado@ntu.ac.uk
:SINCE: 07/09/2022
:VERSION: 0.1

This file is part of Python bootcamp.
the Python bootcamp can not be copied and/or distributed without the express
permission of Pedro Machado <pedro.machado@ntu.ac.uk>

Copyright (C) 2022 - All rights reserved, Nottingham Trent University

"""
# ===============================================================================
# PROGRAM METADATA
# ===============================================================================
__author__ = 'Pedro Machado'
__contact__ = 'pedro.amachado@ntu.ac.uk'
__copyright__ = 'Python bootcamp can not be copied and/or distributed \
without the express permission of Pedro Machado pedro.baptistamachado@ntu.ac.uk'
__license__ = 'Copyright (C) 2022'
__date__ = '07/09/2022'
__version__ = '0.1'
__file_name__ = 'main.py'
__description__ = 'Main python file'
# ===============================================================================
# IMPORT STATEMENTS
# ===============================================================================
import myModule as mmod
import myModule2 as mmod2
# ===============================================================================
# GLOBAL VARIABLES DECLARATIONS
# ===============================================================================

# ===============================================================================
# METHODS
# ===============================================================================
def main():
    # print("The author is", __author__)
    # print("The version is", __version__)
    mmod.greeting("Pedro")
    print(mmod.person1["age"])
    mmod.person1["age"]=12
    print(mmod.person1["age"])
    print(mmod2.person2["country"])
# ===============================================================================
#  TESTING AREA
# ===============================================================================

# ===============================================================================
# MAIN METHOD
# ===============================================================================

if __name__ == '__main__':
    main()