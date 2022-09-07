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
from zipfile import ZipFile
import pyminizip
import csv
import json
import sqlite3
import numpy as np
from datetime import datetime, timedelta
from time import time
import webbrowser

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import base64
import sys
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
    # p3 = Path('/home/pedro/PycharmProjects/lecture_7/test3.txt')
    # print(p3.stat())
    # print(ctime(p3.stat().st_ctime))
    # print(p3.read_bytes())
    # print(p3.read_text())
    # # print(p3.write_bytes(b'23'))
    # # time.sleep(5)
    # # print(p3.write_text("efgh"))
    #
    # # coping
    # source = p3
    # target = Path('/home/pedro/PycharmProjects/lecture_7/test.txt')
    # target.write_text(source.read_text())
    # # or
    # shutil.copy(source, target)

    # with ZipFile("myFile.zip", "w") as zip:
    #     for path in Path(".").rglob("*.py"):
    #         zip.write(path)

    # output zip file path

    # oupt = "./myFile.zip"
    # # set password value
    # password = "1234"
    # # compress level
    # com_lvl = 5
    # # compressing file
    # vec=[]
    # vec1=[]
    # for path in Path(".").glob("*.py"):
    #     print(path)
    #     vec.append(str(path.absolute()))
    #     vec1.append("")
    # print(vec)
    # pyminizip.compress_multiple(vec, vec1, oupt, password, com_lvl)
    # pyminizip.uncompress(oupt,password,"newDir/",3)

    # with open("data.csv", "w+") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["sadasd", "564", "asdasd"
    #                      ])
    #     writer.writerow([45, 65, 89])
    #     writer.writerow([4, "text", 8])
    #
    # with open("data.csv") as file:
    #     reader = csv.reader(file)
    #     # print(list(reader ))
    #     for row in reader:
    #         print(row)


    # movies = [
    #     {"id": 1, "title": "terminator", "year": 1985},
    #     {"id": 2, "title": "kinderton", "year": 1990}
    # ]
    # data = json.dumps(movies)
    # print(data)
    # Path("movies.json").write_text(data)
    #
    # data = Path("movies.json").read_text()
    # movies = json.loads(data)
    # print(movies)
    # print(movies[0]["title"])

    # movies = json.loads(Path("movies.json").read_text()
    #                     )
    # with sqlite3.connect("newDB.sqlite3") as conn:
    #     command = "INSERT INTO Movies VALUES(?, ?, ?)"
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    # conn.commit()

    # with sqlite3.connect("newDB.sqlite3") as conn:
    #     command = "SELECT * FROM Movies"
    #     cursor = conn.execute(command)
    #     for row in cursor:
    #         print(row)

    # arr=np.array([[1,2,3,4],[4,5,6,7]])
    # np.save("file.npy",arr,allow_pickle=False)
    #
    #
    # arr2=np.load("file.npy")
    # print(arr2)

    # print(time.time())
    # def send_email():
    #     for i in range(1000000):
    #         pass
    #
    # start = time.time()
    # send_email()
    # end = time.time()
    # print(end - start)

    # print(datetime(2020, 5, 29))
    # print(datetime.now())
    # print(datetime.strptime("2020/5/8", "%Y/%m/%d"))
    # print(datetime.fromtimestamp(time()))
    # print(datetime.now().hour)
    # print(datetime.now().strftime("%Y/%m"))
    # print(datetime.now() > datetime(2020, 5, 29, 5, 45, 36))

    # dt1 = datetime(2020, 5, 29)
    # dt2 = datetime.now()
    # duration = dt2 - dt1
    # print(duration)
    # print(duration.seconds, "seconds")
    # print(duration.days, "days")
    # print(duration.total_seconds(), "total_seconds")
    # print(dt1 + timedelta(days=1))

    # webbrowser.open("https://www.youtube.com/watch?v=4wgvhVSq644")


    # ### +++++++++++++NOT WORKING+++++++++++++======
    # message = MIMEMultipart()
    # message["from"] = "Amirhossen"
    # message["to"] = "a.sohrabi1380.fake@gmail.com"
    # message["subject"] = "Hello"
    # message.attach(MIMEText("body","plain"))
    # with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    #     smtp.ehlo()
    #     smtp.starttls()
    #     smtp.login("pedrmachado@gmail.com", "PASSWORD")
    #     smtp.send(message)
    #     print("sent!!")
    # ### ----------- NOT WORKING ----------------------
    print(sys.argv)
# ===============================================================================
#  TESTING AREA
# ===============================================================================

# ===============================================================================
# MAIN METHOD
# ===============================================================================

if __name__ == '__main__':
    main()