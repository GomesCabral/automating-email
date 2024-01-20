import requests

# URL for fetching news articles, currently commented out
# url = "https://newsapi.org/v2/everything?q=bitcoin&language=en&apiKey=837db0c0c7e84c4282bb150742cc12f7"

class NewsFeed:
    """Represents a collection of news titles and links as a single string."""

    # Base URL and API key for the News API
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "837db0c0c7e84c4282bb150742cc12f7"

    def __init__(self, interest, from_date, to_date, language="en"):
        """
        Initializes a NewsFeed object with specific parameters.

        Parameters:
        - interest (str): The topic of interest for news articles.
        - from_date (str): The start date for fetching news articles (format: 'YYYY-MM-DD').
        - to_date (str): The end date for fetching news articles (format: 'YYYY-MM-DD').
        - language (str): The language of the news articles (default: 'en').
        """
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        
    def get(self):
        """
        Fetches news articles based on the specified parameters and formats them into a string.

        Returns:
        - str: A string containing news titles and links.
        """
        # Construct the URL for the News API request
        url = f"{self.base_url}qInTitle={self.interest}&from={self.from_date}&to={self.to_date}&language={self.language}&apiKey={self.api_key}"

        # Make a request to the News API and parse the JSON response
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        # Format the news articles into a string
        email_body = ""
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n" + "\n"

        return email_body
    

# Create a NewsFeed object for the topic 'bitcoin' within a specified date range and language
newsFeed = NewsFeed("bitcoin", "2024-01-01", "2024-01-20", "pt")

# Print the formatted news content
print(newsFeed.get())
