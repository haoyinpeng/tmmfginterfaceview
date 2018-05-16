# -*- coding: utf-8 -*-

from flask import Flask
import db_data

app = Flask(__name__)

def tables():
    res01 = db_data.get_result('666')
    cur01 = res01.exec_sql()
    return res01.get_res_rows(cur01,5)

@app.route('/domain')
def index():
    return '<h1>hello </h1>'+tables()[0][0]

if __name__ == '__main__':
    app.run(debug=True)

