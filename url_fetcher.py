""" Fetch URLs from NewsAPI. """
import os
from datetime import datetime, timedelta
from newsapi import NewsApiClient

API_KEY = os.environ.get("NEWSAPIKEY")

newsapi = NewsApiClient(api_key=API_KEY)


def get_urls(search_query, from_date):
    """
    Get a list of URLs from NewsAPI.

    :param search_query: Search query to use for NewsAPI
    :param from_date: Start date for NewsAPI search

    :return: List of URLs
    """

    to_date = datetime.strptime(from_date, "%Y-%m-%d") + timedelta(days=1)

    all_articles = newsapi.get_everything(
        q=search_query,
        from_param=from_date,
        to=to_date,
        language="en",
        sort_by="relevancy",
        page=1,
    )

    return [
        article["url"]
        for article in all_articles["articles"]
        if article["url"] is not None
    ]


if __name__ == "__main__":
    # Example usage
    print(get_urls("+pickleball", "2021-01-01"))