"""Module with variety of network utils"""

from bs4 import BeautifulSoup, Comment
import requests


def get_html_comments(url):
    """
    Fetch html commentaries located on specified source page
    :param url: URL of html page
    :return: list of fetched html comments
    """
    response = requests.get(url=url)
    if response.status_code != 200:
        raise Exception("Invalid status code != 200")
    else:
        soup = BeautifulSoup(response.content, 'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, Comment))
        return list(comments)


if __name__ == "__main__":
    get_html_comments("http://www.pythonchallenge.com/pc/def/ocr.html")