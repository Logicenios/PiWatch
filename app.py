from flask import Flask, render_template
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)



#Running the webpage

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run()



