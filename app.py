import flask
app = flask.Flask(__name__)

@app.route ('/helloworld')
def hello_world():
    return flask.render_template ('bustimes.html')


