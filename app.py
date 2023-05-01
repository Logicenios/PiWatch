from flask import Flask, render_template
from picamera2 import PiCamera
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

#Running the webpage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

# Starting the camera live preview and the face detection

piwatch = Picamera2()
video_config = piwatch.create_video_configuration()
piwatch.configure(video_config)

encoder = H264Encoder(10000000)
output = FfmpegOutput('preview.mp4')

piwatch.start_recording(encoder, output)



