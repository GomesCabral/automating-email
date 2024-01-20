import yagmail
import pandas
from news import NewsFeed
import datetime
import time


df = pandas.read_excel('people.xlsx')

while True:
    for index, row in df.iterrows():
        if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 30:
            yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
            today = datetime.datetime.now().strftime('%Y-%m-%d')

            newsFeed = NewsFeed(row['interest'], 
                        from_date=yesterday, 
                        to_date=today)
            email = yagmail.SMTP(user="your@gmail.com", password="yourPassword")
            email.send(to=row['email'],
           subject=f"Your {row['interest']} news for today",
           contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. {newsFeed.get()}")
        time.sleep(60)