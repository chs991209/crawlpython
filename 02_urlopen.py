import urllib.request as req
from urllib.error import URLError, HTTPError

# Filename
path_list = ["./images/sample1111.jpg", "./images/index1111.html"]

target_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAzMDVfMTAw%2FMDAxNjE0OTMwMTk2OTI4.1eEVl9Gmtoca3GynyQLVUaf_AFcsceQKYpOYH2fuqUcg.L9V4w81Kaxd2MPe5bFwGeoMvfF5VAq_sdsJJ7q9czdQg.JPEG.mamy0227%2F5.jpg&type=a340",
    "https://www.naver.com",
]

for i, url in enumerate(target_url):
    # Exception
    try:
        response = req.urlopen(url)

        contents = response.read()

        print()

        print("------------------------------------")

        print("Header Info - {} : {}".format(i, response.info()))

        print("HTTP Status Code : {}".format(response.getcode()))

        print()

        print("------------------------------------")

        with open(path_list[i], "wb") as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.\nHTTPError Code : ", e.code)

    except URLError as e:
        print("Download failed.\nURLError Reason : ", e.reason)

    else:
        print()
        print("Download Succeeded.")
