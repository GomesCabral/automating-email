import requests


# url = "https://newsapi.org/v2/everything?q=bitcoin&language=en&apiKey=837db0c0c7e84c4282bb150742cc12f7"

class NewsFeed:
    """Representing multiple nesw title and link as a sigle string"""

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "837db0c0c7e84c4282bb150742cc12f7"

    def __init__(self, interest, from_date, to_date, language="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        
    def get(self):
        url = f"{self.base_url}qInTitle={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n" + "\n"

        return email_body
    

newsFeed = NewsFeed("bitcoin", "2024-01-01", "2024-01-20", "pt")
print(newsFeed.get())