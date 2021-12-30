import requests
from lxml.html import fromstring


def main():
    """
    Naver Scrapping
    """

    session = requests.Session()

    response = session.get("https://www.naver.com/")

    # Articles link list
    print("Article link")
    # print(response.content)

    # GETTING News Link Dictionary
    urls = scrape_news_list_page(response)

    for name, url in urls.items():
        print(name, url)
        # Write File


def scrape_news_list_page(response):
    # URL Dictionary Declare
    urls = {}

    # Tag Info String Save
    root = fromstring(response.content)

    for a in root.xpath('//a[@class="thumb"]'):
        # print(tostring(a, pretty_print=True))

        # a의 구조, 메모리 주소 확인
        # print(a)

        name, url = extract_contents(a)
        #     Dictionary
        urls[name] = url

    return urls


def extract_contents(dom):
    #     Link url
    link = dom.get("href")
    name = dom.xpath("./img")[0].get("alt")

    return name, link


if __name__ == "__main__":
    main()
