import yagmail
import pandas
from news import NewsFeed


df = pandas.read_excel('people.xlsx')

for index, row in df.iterrows():
    newsFeed = NewsFeed(row['interest'], from_date="2024-01-01", to_date="2024-01-19")
    email = yagmail.SMTP(user="phgcabral8@gmail.com", password="zswyertmbzvmjymw")
    email.send(to=row['email'],
           subject=f"Your {row['interest']} news for today",
           contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. {newsFeed.get()}")
