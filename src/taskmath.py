from flask import Flask, redirect, url_for, json


app = Flask(__name__)


class TaskMath(object):
    @staticmethod
    def calc_factorial(value):
        factorial = 1

        for i in range(1, value + 1):
            factorial *= i

        return factorial

    @staticmethod
    def calc_fibonacci(value):
        fib_arr = []

        for _ in range(value if value <= 2 else 2):
            fib_arr.append(1)

        for i in range(2, value):
            fib_arr.append(fib_arr[i - 1] + fib_arr[i - 2])

        return fib_arr


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
