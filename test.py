# import csv
# import io
# import urllib.request
#
# def csv_import(url):
#     url_open = urllib.request.urlopen(url)
#     csvfile = csv.reader(io.StringIO(url_open.read().decode('utf-8')), delimiter=',')
#     return csvfile
#
# vurl = 'http://winterolympicsmedals.com/medals.csv'
# data = csv_import(vurl)
#
# for row in data:
#    print(row)


# from PIL import Image
# import requests
# from io import BytesIO
#
# response = requests.get('https://www.gatan.com/sites/default/files/Large%20FOV_Information%20at%20Nyquiest.png')
# im = Image.open(BytesIO(response.content))
#
# width, height = im.size
#
# # Setting the points for cropped image
# left = 5
# top = height / 4
# right = 164
# bottom = 3 * height / 4
#
# # Cropped image of above dimension
# # (It will not change orginal image)
# im1 = im.crop((left, top, right, bottom))
#
# # Shows the image in image viewer
# im1.show()
