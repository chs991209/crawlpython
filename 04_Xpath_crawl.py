import lxml.html
import requests


def main():
    """
    Naver Scrapping
    """

    session = requests.Session()

    response = session.get("https://www.naver.com/")

    # Articles link list
    urls = scrape_news_list_page(response)

    

    for url in urls:
        print(url)
        # Write


def scrape_news_list_page(response):
    # Blank list
    urls = []

    # Tag str saving
    root = lxml.html.fromstring(response.content)

    for a in root.cssselect('.list_goods .good_item .goods_area'):
       url = a.get('href')
       urls.append(url)

    return urls


if __name__ == '__main__':
    main()