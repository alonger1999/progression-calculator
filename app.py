from flask import Flask, request

from functions import get_an, get_summa


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color: blue;'> Kryzhanovskyi Oleksandr </h1>"


@app.route('/summa')
def summa():

    try:

        a1 = request.args.get('a1', None)
        diff = request.args.get('diff', None)
        n = request.args.get('n', None)

        if a1 is None:
            return "<p style='color: red;'> 'a1' is required </p>"
        else:
            a1 = float(a1)

        if diff is None:
            return "<p style='color: red;'> 'diff' is required </p>"
        else:
            diff = float(diff)

        if n is None:
            return "<p style='color: red;'> 'n' is required </p>"
        else:
            n = int(n)

        summa = get_summa(a1, get_an(a1, diff, n), n)

        return f"<p style='color: green;'> Summa: {summa}. </p>"

    except Exception as exception:
        return f"<p style='color: red;'> {type(exception).__name__}: {exception} </p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090, debug=True)
