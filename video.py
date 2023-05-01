from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder

picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1920, 1080),"frame_rate": 30})
picam2.configure(video_config)
encoder = JpegEncoder(q=70)
#picam2.start_preview()

def take_picture():
    picam2.capture('motion.jpg')
def start_video():
    picam2.start_recording(encoder, 'test.mjpg')
#picam2.start_recording(encoder, 'test.mjpg')
def stop_video():
    picam2.stop_recording()