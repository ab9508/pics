# -*- coding: utf-8 -*-
# __author__ = ab
# __time__   = '2021/2/15'

from flask import Flask, render_template
import crawler

app = Flask(__name__)
app.debug = True


@app.route("/home")
def home():
    print('home')
    return render_template('home.html')


@app.route("/")
def home1():
    print("/")
    return index('')


@app.route("/<keyword>")
def index(keyword):
    print('keyword= {}'.format(keyword))
    # 获取数据
    data = crawler.get_url(keyword)
    return render_template('index.html', data=data)


def s():
    # 爬虫获取源码，数据并落库
    crawler.save('美女', 100)


if __name__ == '__main__':
    app.run(debug=True)
