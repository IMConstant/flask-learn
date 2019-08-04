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