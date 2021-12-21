import requests
from lxml.html import fromstring


def main():
    """
    Naver Scrapping
    """

    session = requests.Session()

    response = session.get("https://www.naver.com/")

    # Articles link list
    print('Article link')
    # print(response.content)

    urls = scrape_news_list_page(response)

    # for url in urls:
    #     # print(url)
    #     # Write File


def scrape_news_list_page(response):
    # Blank list
    urls = {}

    # Tag str saving
    root = fromstring(response.content)

    for a in root.xpath('//a[@class="thumb"]'):
        # print(tostring(a, pretty_print=True))
        print(a)
        name, url = extract_contents(a)
        #     Dictionary
        urls[name] = url

    # return urls


def extract_contents(dom):
    #     Link url
    link = dom.get("href")
    name = dom.xpath('./img')[0].get('alt')
    print('')
    print('Name')
    print(name)
    return name, link


if __name__ == '__main__':
    main()
