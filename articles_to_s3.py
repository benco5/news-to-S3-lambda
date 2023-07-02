""" Upload article text to S3 """
import os
import boto3
from text_extractor import get_article_text


access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


s3 = boto3.client("s3")


def process_article_urls(urls, bucket_name, ns_prefix, date_prefix):
    """
    Process a list of article URLs and upload the text files to S3.

    :param urls: List of article URLs
    :param bucket_name: Name of the S3 bucket
    :param ns_prefix: Namespace prefix for the S3 bucket
    :param date_prefix: Date prefix for the S3 bucket (e.g. "2021-01-01")

    :return: None
    """
    for url in urls:
        # Fetch the article text
        text = get_article_text(url)

        # Generate a unique file name for the text file based on the article URL
        # You can customize the file name generation logic as per your requirements
        file_name = url.replace("/", "_") + ".txt"
        full_prefix = f"{ns_prefix}/{date_prefix}/{file_name}"

        # Upload the text file to the S3 bucket
        s3.put_object(Body=text, Bucket=bucket_name, Key=full_prefix)


if __name__ == "__main__":
    # Example usage
    article_urls = [
        "https://www.example.com/news/article1",
        "https://www.example.com/news/article2",
    ]

    process_article_urls(article_urls, "pbnewsproject", "incoming", "2021-01-01")
