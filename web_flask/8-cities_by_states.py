#!/usr/bin/python3
'''Flask With Python'''
from flask import Flask, request, render_template
from models import storage


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_list():
    '''9'''
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    '''8 part 2'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
