""" This is the main script that runs the pipeline. """
from url_fetcher import get_urls
from articles_to_s3 import process_article_urls


def run_pipeline(query_term, bucket_name, ns_prefix, from_date):
    """
    Run the pipeline.

    :param query_term: Search query to use for NewsAPI
    :param bucket_name: Name of the S3 bucket
    :param ns_prefix: Namespace prefix for the S3 bucket
    :param from_date: Start date for NewsAPI search

    :return: None
    """
    article_urls = get_urls(query_term, from_date)
    process_article_urls(article_urls, bucket_name, ns_prefix, from_date)


if __name__ == "__main__":
    from datetime import datetime, timedelta

    day_before_yesterday = datetime.now() - timedelta(days=2)
    day_before_yesterday = day_before_yesterday.strftime("%Y-%m-%d")
    run_pipeline("+pickleball", "pbnewsproject", "incoming", day_before_yesterday)
