import os
import datetime
import time
from pushbullet import Pushbullet

# Replace 'YOUR_PUSHBULLET_API_KEY' with the access token from your Pushbullet account

pb = Pushbullet(os.environ.get('PUSHBULLET_API_KEY'))

# Your dictionary with dates and dollar amounts (in the "7-May-2026" format)
my_dict = {'22-Jul-2023': '$130,406.00'}

def convert_date_format(date_str):
    # Convert date from "7-May-2026" format to datetime object
    date_obj = datetime.datetime.strptime(date_str, '%d-%b-%Y').date()
    return date_obj

def send_pushbullet_notification(title, message):
    pb.push_note(title, message)

def main():
        
        notification_sent = False  # Flag to track if a notification has been sent
        today = datetime.date.today()

        for date_str, amount in my_dict.items():
           date_obj = convert_date_format(date_str)
           if today == date_obj and not notification_sent:
            title = 'Goal check in'
            message = f"Date: {date_str}\nAmount: {amount}"
            send_pushbullet_notification(title, message)
            notification_sent = True  
       
     # Reset the flag for the next day
        if today != date_obj:
           notification_sent = False      
if __name__ == "__main__":
    main()
