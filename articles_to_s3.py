""" Upload article text to S3 """
import boto3
from text_extractor import get_article_text


def process_article_urls(urls, bucket_name, ns_prefix, date_prefix, secrets):
    """
    Process a list of article URLs and upload the text files to S3.

    :param urls: List of article URLs
    :param bucket_name: Name of the S3 bucket
    :param ns_prefix: Namespace prefix for the S3 bucket
    :param date_prefix: Date prefix for the S3 bucket (e.g. "2021-01-01")
    :param secrets: Dictionary containing secret values

    :return: None
    """

    s3 = boto3.client(
        "s3",
        aws_access_key_id=secrets["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=secrets["AWS_SECRET_ACCESS_KEY"],
    )

    for url in urls:
        text = get_article_text(url)
        if text:
            file_name = url.replace("/", "_") + ".txt"
            full_prefix = f"{ns_prefix}/{date_prefix}/{file_name}"

            s3.put_object(Body=text, Bucket=bucket_name, Key=full_prefix)


if __name__ == "__main__":
    from news_article_pipeline import fetch_secrets

    # Example usage
    article_urls = [
        "https://www.example.com/news/article1",
        "https://www.example.com/news/article2",
    ]

    process_article_urls(
        article_urls, "pbnewsproject", "incoming", "2021-01-01", fetch_secrets()
    )
