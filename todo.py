from flask import Flask, url_for, request, jsonify
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

todos = {}

@app.route("/")
def list_todos():
  return jsonify(list(todos.values()))

@app.route("/<id>")
def get_todo(id):
  return jsonify(todos[id])

@app.route("/", methods=["POST"])
def add_todo():
  id = str(uuid.uuid1())
  todo = request.json
  todo['completed'] = False
  todo['url'] = request.base_url + id
  todos[id] = todo
  return jsonify(todo)

@app.route("/<id>", methods=["PATCH"])
def patch_todo(id):
  patch = request.json
  original = todos[id]
  patched = {**original, **patch}
  todos[id] = patched
  return jsonify(patched)

@app.route("/", methods=["DELETE"])
def delete_all():
  todos.clear()
  return ""

@app.route("/<id>", methods=["DELETE"])
def delete_todo(id):
  del todos[id]
  return ""