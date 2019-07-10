from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hi')
def hi():
    return 'hi'


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>')
# def get_lotto_1():
#     return
#     # 1회차 로또정보


@app.route('/hello/<name>')  # var routing
def hello(name):
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = ['짜장면', '짬뽕', '탕수육', '볶음밥', '사천탕면', '쟁반짜장']
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:cube_num>')
def cube(cube_num):
    cube_num = pow(cube_num, 3)  # cube_num ** 3
    return str(cube_num)


if __name__ == '__main__':
    app.run(debug=True)
