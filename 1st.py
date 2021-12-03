import urllib.request as req


# File_url
img_url = 'https://postfiles.pstatic.net/MjAyMTExMThfMTIz/MDAxNjM3MjIyNTEzMjIx.1tuKSq0QSVAwpt-XYQC5324zo9Nm1SbUaHYRzXwxKKMg.ed8BjgKqvXb2StrHvEdHlo7TdojJGJX9__qC_1fQ5REg.JPEG.soravan/SE-f8502d21-8003-47b9-9f89-68853cbab66f.jpg?type=w773'
html_url = 'https://www.naver.com'


# Download path
save_path1 = '/Users/choehyeonsu/test2.jpg'
save_path2 = '/Users/choehyeonsu/index2.html'

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


