""" Description: Extract the visible text from an article. """
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from bs4.element import Comment


def tag_visible(element):
    """
    Filter function to check if an HTML element is visible.

    :param element: HTML element

    :return: True if the element is visible, False otherwise
    """
    # Source: https://stackoverflow.com/a/1983219/9263761 (modified)
    if element.parent.name in [
        "style",
        "script",
        "head",
        "title",
        "meta",
        "[document]",
    ]:
        return False
    if isinstance(element, Comment):
        return False
    return True


def get_article_text(url):
    """
    Extract the visible text from an article.

    :param url: URL of the article

    :return: Visible text of the article
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for non-successful status codes
        soup = BeautifulSoup(response.content, "html.parser")
        texts = soup.findAll(string=True)
        visible_texts = filter(tag_visible, texts)

        return " ".join(t.strip() for t in visible_texts)
    except RequestException:
        # Handle request-related exceptions (e.g., timeout, connection error)
        return ""


if __name__ == "__main__":
    # Example usage
    print(get_article_text("https://www.example.com/news/article"))
