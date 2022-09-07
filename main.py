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
from pathlib import Path
import time
from time import ctime
import shutil
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
#     code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("age cannot be less than 1")
# try:
#     calculate_xfactor(-1)
# except ValueError as er:
#     pass"""
#     code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     xfactor = calculate_xfactor(-1)
#     if xfactor == None:
#         pass
#     """
#     print("Code1: ", timeit(code1, number=10000)*1000, "ms")
#     print("Code2: ", timeit(code2, number=10000)*1000, "ms")
#     print("End of the program!")

#     code3="""
# from pathlib import Path
# p = Path('.')
# var = list(p.glob('*.txt'))
# for i in range(0, len(var)):
#     if (var[i] == Path("file.txt")):
#         pass
#     else:
#         pass
# """
#     code4="""
# from pathlib import Path
# try:
#     p = Path('.')
#     var = list(p.glob('*.txt'))
#     for i in range(0, len(var)):
#         if (var[i] == Path("file.txt")):
#             pass
#         else:
#             raise ValueError("should not be here!")
# except ValueError:
#     pass
# """
#     print("Code3: ", timeit(code3, number=1000)*1000, "ms")
#     print("Code4: ", timeit(code4, number=1000) * 1000, "ms")
#     print("End of the program!")

    # p = Path('/home/pedro/PycharmProjects/lecture_7')
    # var = list(p.glob('*.txt'))
    # var1 = list(p.glob('*.py'))
    # for i in range(0, len(var)):
    #     if (var[i] == Path("file.txt")):
    #         print("Found the file!")
    #     else:
    #         print("Wrong file!")
    # print(var1)
    # print("Is it a dir?: ",var1[0].is_dir(), var1[0])
    # print("Is it a file?: ", var1[0].is_file(), var1[0])
    # print(var1[0].name)
    # print(var1[0].suffix)
    # print(var1[0].parent)
    # print(p.with_name("file.txt"))
    # print(p.absolute())

    # p = Path('/home/pedro/PycharmProjects/lecture_7/test.txt')
    # print(p.joinpath("test.txt"))
    # p.exists()
    # print("Renaming file")
    # p.rename("test2.txt")
    # time.sleep(1)
    # p2 = Path('/home/pedro/PycharmProjects/lecture_7/test2.txt')
    # print("Renaming file")
    # p2.rename("test.txt")
    # time.sleep(1)
    # print("Deleting file")
    # p.unlink()
    p3 = Path('/home/pedro/PycharmProjects/lecture_7/test3.txt')
    print(p3.stat())
    print(ctime(p3.stat().st_ctime))
    print(p3.read_bytes())
    print(p3.read_text())
    # print(p3.write_bytes(b'23'))
    # time.sleep(5)
    # print(p3.write_text("efgh"))

    # coping
    source = p3
    target = Path('/home/pedro/PycharmProjects/lecture_7/test.txt')
    target.write_text(source.read_text())
    # or
    shutil.copy(source, target)

# ===============================================================================
#  TESTING AREA
# ===============================================================================

# ===============================================================================
# MAIN METHOD
# ===============================================================================

if __name__ == '__main__':
    main()