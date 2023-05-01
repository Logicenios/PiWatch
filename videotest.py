from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import libcamera
import time

piwatch = Picamera2()
piwatch.rotation = 180
piwatch.frame_rate = 25
piwatch.resolution = (640, 480)
video_config = piwatch.create_video_configuration()
piwatch.configure(video_config)


encoder = H264Encoder(10000000)
output = FfmpegOutput('preview.mp4')

piwatch.start_recording(encoder, output)
time.sleep(5)
piwatch.stop_recording()
