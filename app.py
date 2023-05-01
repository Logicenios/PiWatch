from flask import Flask, render_template
from video import start_video , stop_video, take_picture
#Running the webpage

app = Flask(__name__)

@app.route('/')
def index():
    start_video()
    return render_template('index.html')

if __name__ == '__main__':
    app.run()



