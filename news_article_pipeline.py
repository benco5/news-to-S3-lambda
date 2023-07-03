""" This is the main script that runs the pipeline. """
import os
import json
from datetime import datetime, timedelta
import boto3
from url_fetcher import get_urls
from articles_to_s3 import process_article_urls


def fetch_secrets():
    """
    Fetch the secrets from AWS Secrets Manager.

    :return: Dictionary containing secret values
    """
    secret_name = "pb-lambda-secrets"
    region_name = "us-west-1"

    client = boto3.client("secretsmanager", region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    secret_value = response["SecretString"]
    return json.loads(secret_value)


def run_pipeline(query_term, bucket_name, ns_prefix, from_date):
    """
    Run the pipeline.

    :param query_term: Search query to use for NewsAPI
    :param bucket_name: Name of the S3 bucket
    :param ns_prefix: Namespace prefix for the S3 bucket
    :param from_date: Start date for NewsAPI search

    :return: None
    """

    secrets = fetch_secrets()
    article_urls = get_urls(query_term, from_date, secrets["NEWS_API_KEY"])
    process_article_urls(article_urls, bucket_name, ns_prefix, from_date, secrets)


def lambda_handler(event=None, context=None):
    """
    Lambda handler function.

    :return: None
    """
    yesterday = datetime.now() - timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")

    # Check to see if FROM_DATE is set as an environment variable and if not, use yesterday's date.
    # This allows the pipeline to be run for a specific date as needed.
    if os.environ.get("FROM_DATE"):
        from_date = os.environ.get("FROM_DATE")
    else:
        from_date = yesterday

    query_term = "+pickleball"
    bucket_name = "pbnewsproject"
    ns_prefix = "incoming"

    run_pipeline(query_term, bucket_name, ns_prefix, from_date)


if __name__ == "__main__":
    lambda_handler()
