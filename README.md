# Email News Sender

## Overview
This Python script automates the process of sending personalized news emails to a list of recipients based on their interests. It utilizes the `yagmail` library for email functionality and assumes the existence of a `NewsFeed` class within a 'news' module to retrieve news content.

## Prerequisites
1. **Python Environment:** Ensure you have a Python environment set up on your system.
2. **Dependencies Installation:** Install the required Python libraries using the following command:
   ```bash
   pip install yagmail pandas

Getting Started
1. Clone the Repository:
git clone https://github.com/your-username/your-repo.git cd your-repo

2. Setup Excel File:

Create an Excel file named people.xlsx with the following columns:
name: Recipient's name
email: Recipient's email address
interest: Topic of interest for news updates

3. Configure Email and News Settings:

Open the script and update the following information:
Your Gmail credentials (replace "your@gmail.com" and "yourPassword").
Customize the NewsFeed initialization with your desired date range.

4.Run the Script:
python script.py


Script Details
Reads recipient data from the people.xlsx Excel file into a Pandas DataFrame.
Runs an infinite loop to check the current time and sends personalized news emails at 10:30 AM each day.
For each recipient, it creates a NewsFeed object based on their specified interest and sends an email with the latest news.
Important Notes
Ensure compliance with Google's security policies when using Gmail credentials.
The script is set to run indefinitely; modify the loop condition if you want to limit the number of iterations.
