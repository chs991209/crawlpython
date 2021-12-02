import urllib.request as req


# File_url
img_url = 'https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg'
html_url = 'https://www.google.com'


# Download path
save_path1 = '~/test1.jpg'
save_path2 = '~/index.html'

# Exception
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)

except Exception as e:
    print('Download Failed')
    print(e)

    # Normal print
else:
    print(header1)
    print(header2)


