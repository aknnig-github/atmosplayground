"""Flask webapp demo."""

import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    """Return a default HTML response."""
    return "Data Magic!"


if __name__ == '__main__':
    app.debug = True
    app.run()

# hint:
# export FLASK_APP=flaskappdemo.py
# flask run
