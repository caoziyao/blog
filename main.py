# coding: utf-8

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def main():
    config = {
        'host': '0.0.0.0',
        'port': 3000,
        'debug': True,
    }
    app.run(**config)

if __name__ == '__main__':
    main()