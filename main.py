import yagmail
import pandas
from news import NewsFeed  # Assuming 'news' module contains the NewsFeed class
import datetime
import time

# Read data from an Excel file ('people.xlsx') into a DataFrame
df = pandas.read_excel('people.xlsx')

# Infinite loop to continuously check the time and send emails
while True:
    # Iterate over each row in the DataFrame
    for index, row in df.iterrows():
        # Check if the current time is 10:30 AM
        if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 30:
            # Calculate the date of yesterday and today
            yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
            today = datetime.datetime.now().strftime('%Y-%m-%d')

            # Create a NewsFeed object for the specific interest and date range
            newsFeed = NewsFeed(row['interest'], 
                        from_date=yesterday, 
                        to_date=today)

            # Set up yagmail SMTP connection
            email = yagmail.SMTP(user="your@gmail.com", password="yourPassword")

            # Send an email to the specified recipient with news content
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today",
                       contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. {newsFeed.get()}")

        # Pause the execution for 60 seconds before checking the time again
        time.sleep(60)
