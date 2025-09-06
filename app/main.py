from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []
counter = 1

@app.route("/")
def health():
    return {"status": "ok"}

@app.route("/todos", methods=["GET", "POST"])
def handle_todos():
    global counter
    if request.method == "POST":
        data = request.json
        if not data or "title" not in data:
            return {"error": "title is required"}, 400
        todo = {"id": counter, "title": data["title"], "done": False}
        todos.append(todo)
        counter += 1
        return todo, 201
    return jsonify(todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

