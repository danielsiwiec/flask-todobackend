import flask
import flask_cors
import uuid

app = flask.Flask(__name__)
flask_cors.CORS(app)

todos = {}

@app.route("/")
def list_todos():
  return flask.jsonify(list(todos.values()))

@app.route("/<id>")
def get_todo(id):
  return flask.jsonify(todos[id])

@app.route("/", methods=["POST"])
def add_todo():
  id = str(uuid.uuid1())
  todo = flask.request.json
  todo['completed'] = False
  todo['url'] = flask.request.base_url + id
  todos[id] = todo
  return flask.jsonify(todo)

@app.route("/<id>", methods=["PATCH"])
def patch_todo(id):
  patch = flask.request.json
  original = todos[id]
  patched = {**original, **patch}
  todos[id] = patched
  return flask.jsonify(patched)

@app.route("/", methods=["DELETE"])
def delete_all():
  todos.clear()
  return ""

@app.route("/<id>", methods=["DELETE"])
def delete_todo(id):
  del todos[id]
  return ""