# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:25:37 2021

@author: User
"""

import datetime
import time
import os

while True:
    os.system("cls")
    dt = datetime.datetime.now()
    print(f"{dt.hour}:{dt.minute}:{dt.second}")
    time.sleep(1) # para que duerma por un segundo
    