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
:SINCE: <date>/2022
:VERSION: 0.1
 
This file is part of Python bootcamp project.
the Python bootcamp project can not be copied and/or distributed without the express
permission of Pedro Machado <pedro.machado@ntu.ac.uk>

Copyright (C) 2022 - All rights reserved, Nottingham Trent University

"""
# ===============================================================================
# PROGRAM METADATA
# ===============================================================================
__author__ = 'Pedro Machado'
__contact__ = 'pedro.amachado@ntu.ac.uk'
__copyright__ = 'Python bootcamp project can not be copied and/or distributed \
without the express permission of Pedro Machado pedro.machado@ntu.ac.uk'
__license__ = 'Copyright (C) 2022'
__date__ = '07/09/2022'
__version__ = '0.1'
__file_name__ = 'exceptions.py'
__description__ = 'Provide examples of exceptions'
# ===============================================================================
# IMPORT STATEMENTS
# ===============================================================================

# ===============================================================================
# GLOBAL VARIABLES DECLARATIONS
# ===============================================================================

# ===============================================================================
# METHODS
# ===============================================================================
def example_exceptions():
    try:
        age = int(input("age: "))
        xfactor=10/age
        print("Age:", xfactor)
    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Cannot divide by 0")

def file_exceptions():
    try:
        file = open("file.txt","a+")
        age = int(input("age: "))
        xfactor = 10 / age
        file.write(str(xfactor)+"\n")
    except (ValueError, ZeroDivisionError) :
        print("invalid input")
    # file.close()
    else:
        print("no excpection thrown")
    # file.close()
    finally:
        file.close()

def file_exceptions1():
    try:
        with open("file1.txt","a+") as file:
            print("file oppened")
            age = int(input("age: "))
            xfactor = 10 / age
            file.write(str(xfactor) + "\n")
    except (ValueError, ZeroDivisionError):
        print("invalid input")
    else:
        print("no excpection thrown")

def exceptions2():
    try:
        ans=input(" Select a or b: ")
        if(ans=="a" or ans=="b"):
            print("OK")
        else:
            raise ValueError("Invalide value")
    except ValueError as er:
        print(er)
# ===============================================================================
#  TESTING AREA
# ===============================================================================

# ===============================================================================
# MAIN METHOD 
# ===============================================================================

# if __name__ == '__main__':
#     pass
