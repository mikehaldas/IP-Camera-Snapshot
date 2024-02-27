# IP-Camera-Snapshot
A simple Python app to get a JPEG snpashot image from a Viewtron IP camera.

All Viewtron IP cameras have a URL that returns a current snapshot image in JPEG format.
This Python app retrieves the latest snashot from the IP camera and saves it to a directory.
The file is named using a number, like 1.jpg, so that the snapshots are serealized. 
This is done using a counter file.

This app can also be used with Viewtron security camera DVRs and IP camera NVRs.
To specify which camera channel you want to get the snapshot from, add the camera's channel
number on the end of the URL.

Viewtron IP cameras can be purchased online at http://www.Viewtron.com

This app was written by Mike Haldas, co-founder of CCTV Camera Pros.
You can reach me at mike@cctvcamerapros.net
