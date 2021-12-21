import lxml
import requests
from lxml.html import fromstring


def main():
    """
    Naver Scrapping
    """
    print('step1')

    response = requests.get("https://www.naver.com/")

    print('step2' + str(response.content) )

    # Articles link list
    urls = scrape_news_list_page(response)

    print('step3' + str(urls) )

    for url in urls:
        print(url)
        # Write


def scrape_news_list_page(response):
    # Blank list
    urls = []

    # Tag str saving
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('.group_nav .list_nav.type_fix .nth-child(1) '):
       url = a.get('href')
       urls.append(url)

    return urls


if __name__ == '__main__':
    main()