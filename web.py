# -*- coding: utf-8 -*-

from flask import Flask,render_template
import dbsession
import sql_set
from flask import current_app,request
#from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#db = SQLAlchemy(app)

#启动数据库连接池
try:
    db_pool = dbsession.dbpool('B159212','github&flask-1','PERP').db_conn_pool()
except Exception as dberror:
    print('获取数据库连接池失败',dberror)

#app_ctx = app.app_context()

def sumtable_tuple(flag,rows):
    db_sum = db_pool.acquire()
    t = sql_set.ret_sql_res(db_sum,sql_set.sumtable_sql(),{'flag':flag},rows)
    db_pool.release(db_sum)
    return t

@app.route('/')
def index():
    #return '<h1>hello </h1> <h2> %s </h2>',sumtable_tuple()[0][5]
    return render_template('index.html',table = sumtable_tuple('E',10))

@app.route('/context')
def context():
    return ''+current_app.name+' '+request.url

if __name__ == '__main__':
    app.run(debug=True)

