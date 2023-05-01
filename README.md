# PiWatch
Raspberry Pi based security camera

This project is a simple and easy way to stream a camera from a Raspberry Pi to a webpage using Python and Flask. The project uses the camera-streamer library to capture and encode the video frames from the camera, and Flask to serve the video stream as a Motion JPEG over HTTP. The webpage uses a HTML5 video element to display the video stream in the browser. The project can be customized to use different camera settings, encoding options, and Flask routes.

Installation

pip install flask
flask run --host 0.0.0.0