import flask

app = flask.Flask(__name__, template_folder='./flask-environment/templates', static_folder='./flask-environment/static')

@app.route('/')
def home():
    return flask.render_template('homepage.html')
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9000, threaded=True, debug=True)