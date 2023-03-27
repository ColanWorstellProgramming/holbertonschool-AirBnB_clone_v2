#!/usr/bin/python3
'''Flask With Python'''
from flask import Flask, request, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    '''8'''
    state = storage.all('State')
    return render_template("7-states_list.html", states=state)


@app.teardown_appcontext
def des():
    '''8 part 2'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
