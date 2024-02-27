# IP-Camera-Snapshot
A simple Python app to get a JPEG snpashot image from a Viewtron IP camera.

All Viewtron IP cameras have a URL that returns a current snapshot image in JPEG format.
This Python app retrieves the latest snashot from the IP camera and saves it to a directory.
The file is named using a number, like 1.jpg, so that the snapshots are serealized. 
This is done using a counter file.

This app can also be used with Viewtron security camera DVRs and IP camera NVRs.
To specify which camera channel you want to get the snapshot from, add the camera's channel
number on the end of the URL.

You can find the Viewtron security camera products that work with this app here.

Viewtron IP Cameras
https://www.cctvcamerapros.com/viewtron-IP-cameras-s/1474.htm

Viewtron IP Camera NVRs
https://www.cctvcamerapros.com/IP-Camera-NVRs-s/1472.htm

Viewtron Hybrid BNC DVRs
https://www.cctvcamerapros.com/Security-Camera-DVRs-s/1467.htm

This app was written by Mike Haldas, co-founder of CCTV Camera Pros.
You can reach me at mike@cctvcamerapros.net
