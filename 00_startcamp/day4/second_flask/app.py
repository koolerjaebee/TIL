import datetime

from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send')
def send():
    return render_template('send.html')


@app.route('/receive', methods=['POST'])
def receive():
    my_token = 'pk_b7e8384e4a0046808ce302c81b672149'

    data = request.form.get('msg')
    stock = Stock(data, token=my_token).get_quote()
    company_name = stock['companyName']
    realtime_price = stock['iexRealtimePrice']

    return render_template(
        'receive.html',
        company_name=company_name, realtime_price=realtime_price
        )


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = ['스파이더맨:파 프롬 홈', '라이온 킹', '알라딘', '토이 스토리 4', '기생충']
    return render_template('boxoffice.html', top_5=top_5)


if __name__ == '__main__':
    app.run(debug=True)
