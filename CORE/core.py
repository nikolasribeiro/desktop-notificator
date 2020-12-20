""" 
Core of all the script, from here I can use the native Notification API of
any OS

Copyright (c) 2020 Nicolas Ribeiro
"""

__all__ = ['Notification']


class Notification:

    #urgency
    LOW     = "low"
    NORMAL  = "normal"
    HIGH    = "critical"

    def __init__(self, title, body="", timeout=3, urgency=LOW, icon=""):
        self.title      = title
        self.body       = body
        self.timeout    = timeout
        self.urgency    = urgency
        self.icon       = icon
    
    def make_notification(self):
        import subprocess
        
        promp = [
            'notify-send', 
            f'{self.title}', 
            f'{self.body}', 
            '-u', self.urgency,
            '-t', f'{ self.timeout * 1000 }'
        ]

        if self.icon != "":
            promp += ['-i', self.icon]
        
        subprocess.call(promp)