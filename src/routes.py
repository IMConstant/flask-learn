from src import app
from flask import redirect, url_for, json
from .task_math import TaskMath


@app.route('/', methods=['GET'])
def start():
    return redirect(url_for('main'))


@app.route('/main', methods=['GET'])
def main():
    return 'Hello!'


@app.route('/main/factorial<int:value>', methods=['GET'])
def get_factorial(value):
    return json.dumps(TaskMath.calc_factorial(value))


@app.route('/main/fibonacci<int:value>', methods=['GET'])
def get_fibonacci(value):
    return json.dumps(TaskMath.calc_fibonacci(value))
