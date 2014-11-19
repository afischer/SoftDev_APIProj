from flask import Flask, render_template, request, redirect
from utils import location, restData

# Initialize the Flask application
app = Flask(__name__)

# Default route, print user's IP
@app.route('/', methods=['Post','GET'])
def home():
    if request.method == 'GET':
        ip = location.ip
        print "USER IP ADDRESS: " + ip
        return render_template('home.html')
    else:
        return redirect('/results')

@app.route('/results')
def results():
    L=restData.makeList()
    # L=[[mcd,www.mcd.com],[bking,www.bking.com]]
    # print L
    restaurants=restData.getPriceLevel(1,L)#change the 1 to reflect the radio button
    return render_template('results.html',restaurants=restaurants)
  


if __name__ == '__main__':
    app.debug == True
    app.run()
