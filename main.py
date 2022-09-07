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
import exceptions
from timeit import timeit
# ===============================================================================
# GLOBAL VARIABLES DECLARATIONS
# ===============================================================================
flag=False
# ===============================================================================
# METHODS
# ===============================================================================
def main():
    # print("The author is", __author__)
    # print("The version is", __version__)
    # mmod.greeting("Pedro")
    # print(mmod.person1["age"])
    # mmod.person1["age"]=12
    # print(mmod.person1["age"])
    # print(mmod2.person2["country"])
    # if flag:
    #     age = int(input("age: "))
    #     xfactor = 10 / age
    #     print("Age:", xfactor)
    # else:
    #     exceptions.example_exceptions()
    # exceptions.file_exceptions()
    # exceptions.file_exceptions1()
    #exceptions.exceptions2()


    code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be less than 1")
try:
    calculate_xfactor(-1)
except ValueError as er:
    pass"""
    code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    xfactor = calculate_xfactor(-1)
    if xfactor == None:
        pass
    """
    print("Code1: ", timeit(code1, number=10000)*1000, "ms")
    print("Code2: ", timeit(code2, number=10000)*1000, "ms")
    print("End of the program!")
# ===============================================================================
#  TESTING AREA
# ===============================================================================

# ===============================================================================
# MAIN METHOD
# ===============================================================================

if __name__ == '__main__':
    main()