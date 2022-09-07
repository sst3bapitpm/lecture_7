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
without the express permission of Pedro Machado pedro.machado@ntu.ac.uk'
__license__ = 'Copyright (C) 2022'
__date__ = '07/09/2022'
__version__ = '0.1'
__file_name__ = 'task.py'
__description__ = 'Get the the time and the details of the OS and save it into \
                  myDetails.txt, copy the myDetails.txt to myDetails2.txt and \
                   append the current time'
# ===============================================================================
# IMPORT STATEMENTS
# ===============================================================================
import pathlib as Path
from datetime import datetime
import platform
import shutil
import time
# ===============================================================================
# GLOBAL VARIABLES DECLARATIONS
# ===============================================================================

# ===============================================================================
# METHODS
# ===============================================================================
def task():
    src = "/home/pedro/PycharmProjects/lecture_7/myDetails.txt"
    target = "/home/pedro/PycharmProjects/lecture_7/myDetails2.txt"
    now = datetime.now()
    content = now.strftime("%H:%M:%S")+"\n"
    content+=platform.system()+"\n"
    with open(src, "w+") as file:
        file.write(content)
    time.sleep(2)
    shutil.copy(src, target)
    with open(target, "a+") as file:
        file.write(datetime.now().strftime("%H:%M:%S")+"\n")
# ===============================================================================
#  TESTING AREA
# ===============================================================================

# ===============================================================================
# MAIN METHOD 
# ===============================================================================

if __name__ == '__main__':
    task()
