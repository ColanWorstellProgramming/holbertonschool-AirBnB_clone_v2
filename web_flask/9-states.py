#!/usr/bin/python3
'''Flask With Python'''
from flask import Flask, request, render_template
from models import storage


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    '''9'''
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    '''10'''
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    '''8 part 2'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
