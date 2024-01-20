Email News Notifier
This Python script is designed to send personalized email notifications containing news updates to specified recipients based on their interests. The script utilizes the News API to fetch news articles and Yagmail for sending emails.

Prerequisites
Before running the script, ensure that you have the following prerequisites installed:

Python 3.x
Yagmail library (pip install yagmail)
Pandas library (pip install pandas)
News module containing the NewsFeed class (source not provided)
Usage
Clone the repository or download the script (email_news_notifier.py) to your local machine.

Install the required dependencies:
pip install yagmail pandas

Replace the placeholder values in the script:

Update the user and password in the SMTP connection with your Gmail credentials.
Ensure the path to the Excel file (people.xlsx) is correct.
Run the script:
python email_news_notifier.py

The script will continuously check the time, and if it's 10:30 AM, it will send personalized news emails to the specified recipients.

Configuration
Excel Data: The script reads recipient data from an Excel file (people.xlsx). Ensure that the file contains columns like 'name', 'email', 'interest', etc.

News Module: The script assumes the existence of a 'news' module containing the NewsFeed class for fetching news articles. Make sure you have the required module or replace it with your news fetching logic.
