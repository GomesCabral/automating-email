import yagmail
import pandas
from news import NewsFeed
import datetime


df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    newsFeed = NewsFeed(row['interest'], 
                        from_date=yesterday, 
                        to_date=today)
    email = yagmail.SMTP(user="phgcabral8@gmail.com", password="zswyertmbzvmjymw")
    email.send(to=row['email'],
           subject=f"Your {row['interest']} news for today",
           contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. {newsFeed.get()}")
