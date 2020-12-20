#!/usr/bin/env python3

""" 
A simple desktop notificator that remember you to do anything you dont want to foget
Author: Nicolas Ribeiro
"""
from utils.functions import *
from utils.icons import *
from datetime import datetime
import schedule
import time

def take_a_rest():
    send_notification(
        title   = "Tomate un descanso",
        body    = "Aprovecha a salir afuera, tomarte un descanso, beber cafe",
        timeout = 1,
        icon    = FACE_TIRED
    )


def main():

    #First Notification to take a rest
    schedule.every(1).hours.do(take_a_rest)



    while True:
        schedule.run_pending()    
        time.sleep(1)




if __name__ == "__main__":
    main()