import requests
import json
from flask import Flask, Response, make_response, request

import main as Main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        #flask.Flask.make_response>`.
        `make_response <http://flask.pocoo.org/docs/1.0/api/
    """
    response = Main.Emoji(request)
    return response


if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5000)
