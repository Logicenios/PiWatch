from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
import time

# Create a camera object
picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)})
picam2.configure(video_config)
encoder = JpegEncoder(q=70)

#picam2.start_preview()

def take_picture():
    picam2.capture('static/images/motion.jpg')
    while True:
        time.sleep(1)
    camera.stop_recording()
def start_video():
    picam2.start_recording(encoder, 'static/images/preview.mjpg')
#picam2.start_recording(encoder, 'test.mjpg')
def stop_video():
    picam2.stop_recording()

