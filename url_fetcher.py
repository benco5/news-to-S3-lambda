""" Fetch URLs from NewsAPI. """
from newsapi import NewsApiClient


def get_urls(search_query, from_date, api_key):
    """
    Get a list of URLs from NewsAPI.

    :param search_query: Search query to use for NewsAPI
    :param from_date: Start date for NewsAPI search
    :param api_key: NewsAPI API key

    :return: List of URLs
    """

    newsapi = NewsApiClient(api_key=api_key)

    all_articles = newsapi.get_everything(
        q=search_query,
        from_param=from_date,
        to=from_date,  # We only want articles from a single day
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
    from news_article_pipeline import fetch_secrets

    # Example usage
    print(get_urls("+pickleball", "2021-01-01", fetch_secrets()["NEWS_API_KEY"]))
