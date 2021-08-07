from flask import *

app = Flask(__name__)

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')