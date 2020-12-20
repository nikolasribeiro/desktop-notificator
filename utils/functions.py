from CORE.core import Notification


# sets all the names for import
__all__ = ['send_notification', 'timer']

def send_notification(title, body="", timeout=3, urgency="low", icon=""):
    Notification(
        title=title,
        body=body,
        timeout=timeout,
        urgency=urgency,
        icon=icon
    ).make_notification()


def timer():
    print("Este seria el timer")