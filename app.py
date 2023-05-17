import os
from flask import Flask, jsonify, request

app = Flask(__name__)

todo_list = []

@app.route('/api/todo', methods=['GET', 'POST'])
def manage_todos():
    if request.method == 'POST':
        new_todo = request.json['todo']
        todo_list.append(new_todo)
        print(f"New todo: {new_todo} in ENV {os.environ.get('APP_ENV')}")
        response = new_todo.copy()  # Make a copy so we don't modify the original todo
        return jsonify(response), 201

    response = {
        'env': os.environ.get('APP_ENV'),
        'todo_list': todo_list,
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')
