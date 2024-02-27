# Here is a simple python app thet retreives a JPEG snashop image
# from a Viewtron IP Camera and saves it to disk. The app uses a
# COUNTERFILE to keep track on the name of the last image saved,
# so that the counter can be incremented. Images are named 1.jpg, 2.jpg, etc.
# This makes it easy to create a timelaspse video with the images.
# This app can also be used with Viewtron BNC security camera DVRs and
# IP camera NVRs by adding the camera number on the end of the URL. E.G. /GetSnapshot/1
# for the camera connected to channel one on the DVR / NVR
#
# Written by Mike Haldas, co-founder of CCTV Camera Pros
#
# Viewtron IP cameras can be found at https://www.Viewtron.com
#
# Mike can be reached at mike@cctvcamerapros.net

import requests

USERID = 'admin'
PASSWORD = '123456'
DOMAIN = '192.168.0.48'
PORT = '80'
COUNTERFILE = '/home/admin/snapshot/counter.txt'
IMGDIR = '/home/admin/snapshot/images/'

# Viewtron IP camera JPEG URL
url = 'http://' + USERID + ':' + PASSWORD + '@' + DOMAIN + ':' + PORT + '/GetSnapshot'

# get the JPEG image from IP camera
response = requests.get(url, allow_redirects=True)

# check the counter file to create the image name
with open (COUNTERFILE, 'r') as f:
        num = int(f.read().strip())

num = num + 1
imgname = str(num) + ".jpg"

# write the JPEG file
file = open(IMGDIR + imgname, "wb")
file.write(response.content)
file.close()

# increment the counter file
with open(COUNTERFILE, "w") as f:
        f.write(str(num) + "\n")
