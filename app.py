from flask import Flask, render_template, request
from utils import location, restData

# Initialize the Flask application
app = Flask(__name__)

# Default route, print user's IP
@app.route('/')
def home():
    ip = location.ip
    print "USER IP ADDRESS: " + ip
    
    return render_template('home.html')



if __name__ == '__main__':
    app.debug == True
    app.run()
