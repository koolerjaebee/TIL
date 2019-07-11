from flask import Flask, render_template
import datetime
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = ['스파이더맨:파 프롬 홈', '라이온 킹', '알라딘', '토이 스토리 4', '기생충']
    # scraping (#movieList > li:nth-child(2) > div.front-info > div.movie_info > h3 > a)
    return render_template('boxoffice.html', top_5=top_5)


if __name__ == '__main__':
    app.run(debug=True)
