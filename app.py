from flask import Flask, render_template
from video import start_video , stop_video, take_picture
#Running the webpage

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')
    start_video()

if __name__ == '__main__':
    app.run()



